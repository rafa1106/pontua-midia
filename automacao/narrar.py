# -*- coding: utf-8 -*-
"""Gera a narração de um Reel na ElevenLabs (roda no GitHub Action, chave no segredo ELEVENLABS_API_KEY).

Entrada: reels/<id>/roteiro.txt  (uma fala por parágrafo, separados por linha em branco)
Saída:   reels/<id>/narracao.mp3 e reels/<id>/alinhamento.json (início/fim de cada fala e frase, em segundos)
"""
import base64, json, os, re, sys, urllib.request, urllib.error
from pathlib import Path

VOZ_PADRAO = "ORgG8rwdAiMYRug8RJwR"   # Ana Alice - Friendly & Clear (pt-BR)


def pronuncia(t):
    """Ajustes só para a voz (o roteiro fica como está). "pontua" se fala como o verbo pontuar
    (pon-TU-a): o acento em "pontúa" força a tônica no "tu". Mesmo tamanho, não desalinha os tempos."""
    return re.sub(r"\b([Pp])ontua\b(?!\.club)", lambda m: m.group(1) + "ontúa", t)


def tts(texto, voz, modelo):
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voz}/with-timestamps?output_format=mp3_44100_128",
        data=json.dumps({"text": texto, "model_id": modelo}).encode(),
        headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"], "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)


def main(rid, voz, modelo):
    pasta = Path("reels") / rid
    texto = (pasta / "roteiro.txt").read_text(encoding="utf-8").strip()
    falas = [p.strip() for p in re.split(r"\n\s*\n", texto) if p.strip()]
    falas_voz = [pronuncia(f) for f in falas]
    texto = "\n\n".join(falas_voz)
    try:
        out = tts(texto, voz, modelo)
    except urllib.error.HTTPError as e:
        corpo = e.read().decode(errors="replace")[:500]
        print("ElevenLabs", e.code, corpo)
        if modelo != "eleven_multilingual_v2":
            print("tentando eleven_multilingual_v2")
            out = tts(texto, voz, "eleven_multilingual_v2")
        else:
            sys.exit(1)
    (pasta / "narracao.mp3").write_bytes(base64.b64decode(out["audio_base64"]))
    al = out.get("normalized_alignment") or out["alignment"]
    chars, ini, fim = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
    # mapeia cada fala/frase para o intervalo dos seus caracteres
    full = "".join(chars)
    res, pos = {"falas": [], "frases": []}, 0
    for i, (f0, f) in enumerate(zip(falas, falas_voz), 1):
        k = full.find(f[:12], pos)
        if k < 0:
            k = pos
        e = min(len(chars) - 1, k + len(f) - 1)
        res["falas"].append({"id": f"N{i}", "texto": f0, "ini": round(ini[k], 3), "fim": round(fim[e], 3)})
        for m in re.finditer(r"[^.!?…]+[.!?…]*", f):
            s = m.group(0).strip()
            if not s:
                continue
            a = full.find(s[:10], k)
            if a < 0:
                continue
            b = min(len(chars) - 1, a + len(s) - 1)
            res["frases"].append({"fala": f"N{i}", "texto": s, "ini": round(ini[a], 3), "fim": round(fim[b], 3)})
        pos = e + 1
    (pasta / "alinhamento.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(res["falas"], ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] else VOZ_PADRAO,
         sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else "eleven_v4")
