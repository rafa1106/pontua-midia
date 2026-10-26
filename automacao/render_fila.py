# -*- coding: utf-8 -*-
"""Ponte sem credenciais entre a rotina do Claude e o GitHub.

A rotina grava cada post novo no data store do Make com status "renderizar" e o código do
gerador no campo `gerador`. Esta script (rodada pela GitHub Action .github/workflows/renderizar.yml):
  1. pede ao webhook do Make o próximo post pendente (acao=pendentes),
  2. grava gerador/<key>.py e renderiza as artes (mesmo código que a rotina aprovou no QA),
  3. faz commit/push com o GITHUB_TOKEN da própria Action,
  4. espera as URLs raw.githubusercontent.com responderem 200,
  5. avisa o Make (acao=pronto) — o Make confere as imagens e muda o status para "agendado".
Em qualquer falha avisa acao=falhou (status "erro_render"); a rotina seguinte corrige.
"""
import base64, glob, json, os, re, subprocess, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = base64.b64decode(os.environ["PONTE_B64"]).decode().strip()
RAW = "https://raw.githubusercontent.com/rafa1106/pontua-midia/main/artes/"
KEY_RE = re.compile(r"p\d{4}_[a-z0-9]+")


def ponte(acao, **kw):
    q = urllib.parse.urlencode({"acao": acao, **kw})
    req = urllib.request.Request(f"{URL}?{q}", headers={"User-Agent": "pontua-render-action"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.headers.get("X-Post-Key"), r.read().decode("utf-8", "replace")


def sh(*cmd, cwd=ROOT, timeout=900):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    if r.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd[:3])} falhou: {(r.stderr or r.stdout)[-600:]}")
    return r.stdout


def url_ok(u):
    try:
        with urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30) as r:
            return r.status == 200 and r.headers.get("Content-Type", "").startswith("image/")
    except Exception:
        return False


def marcar_inventario(key, codigo):
    p = os.path.join(ROOT, "fontes", "inventario.json")
    inv = json.load(open(p, encoding="utf-8"))
    for grupo, nome in re.findall(r"fontes/(ramos|gerais)/([a-z0-9-]+)\.jpg", codigo):
        item = inv.get(grupo, {}).get(nome)
        if item is not None and key not in item.setdefault("usada_em", []):
            item["usada_em"].append(key)
            if item.get("status") == "disponivel":
                item["status"] = "usada"
    json.dump(inv, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def processar(key, codigo):
    if not KEY_RE.fullmatch(key):
        raise ValueError(f"key inválida: {key!r}")
    if f'build(S, "{key}")' not in codigo:
        raise ValueError(f'o gerador precisa chamar build(S, "{key}")')
    for f in glob.glob(os.path.join(ROOT, "artes", f"{key}_*.jpg")):
        os.remove(f)
    open(os.path.join(ROOT, "gerador", f"{key}.py"), "w", encoding="utf-8").write(codigo)
    sh(sys.executable, f"{key}.py", cwd=os.path.join(ROOT, "gerador"))
    from PIL import Image
    arts = sorted(glob.glob(os.path.join(ROOT, "artes", f"{key}_*.jpg")))
    if not arts:
        raise RuntimeError("nenhuma arte gerada")
    for a in arts:
        if Image.open(a).size != (1080, 1350):
            raise RuntimeError(f"tamanho errado em {os.path.basename(a)}")
    marcar_inventario(key, codigo)
    sh("git", "add", f"gerador/{key}.py", "fontes/inventario.json", *[os.path.relpath(a, ROOT) for a in arts])
    sh("git", "commit", "-m", f"Artes {key} (renderizadas pela Action a partir da fila do Make)\n\n"
       "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>")
    for tentativa in range(4):
        try:
            sh("git", "pull", "--rebase", "origin", "main")
            sh("git", "push", "origin", "HEAD:main")
            break
        except RuntimeError:
            if tentativa == 3:
                raise
            time.sleep(10)
    urls = [RAW + os.path.basename(a) for a in arts]
    for _ in range(40):
        if all(url_ok(u) for u in urls):
            break
        time.sleep(15)
    else:
        raise RuntimeError("as URLs raw não ficaram públicas em 10 min")
    _, resp = ponte("pronto", key=key)
    if not resp.startswith("agendado"):
        raise RuntimeError(f"Make não confirmou (imagens do registro não batem com as geradas?): {resp[:200]}")
    print(f"OK {key}: {len(arts)} artes publicadas e agendadas")


def main():
    vistos, falhas = set(), 0
    for _ in range(10):
        key, codigo = ponte("pendentes")
        if not key or key in vistos:
            break
        vistos.add(key)
        try:
            processar(key, codigo)
        except Exception as e:
            falhas += 1
            print(f"FALHA {key}: {e}", file=sys.stderr)
            subprocess.run(["git", "reset", "--hard", "origin/main"], cwd=ROOT)
            try:
                ponte("falhou", key=key, erro=str(e)[:400])
            except Exception as e2:
                print(f"não consegui avisar o Make: {e2}", file=sys.stderr)
    print(f"fim: {len(vistos)} post(s) pendente(s), {falhas} falha(s)")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
