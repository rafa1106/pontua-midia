# -*- coding: utf-8 -*-
"""Reel 1080x1920 — "Carimbo no balcão" (fluxo 03 do material bruto).

Uso: python3 reel_carimbo.py <pasta_trabalho>
  <pasta>/fl/NNNN.jpg  quadros do lojista.mp4 (30 fps)
  <pasta>/fc/NNNN.jpg  quadros do cliente.mp4 (30 fps)
  <pasta>/audio/N1..N6.mp3  narração (opcional; sem ela usa durações estimadas)
Saída: <pasta>/reel_carimbo.mp4
"""
import json, subprocess, sys
from pathlib import Path
from render2 import FONTS, EMOJI_CSS, C, WA_ICON, LOGO_CLARA, SIMBOLO, _emoji

FPS = 30
W, H = 1080, 1920
PW = 600
SH = round((PW - 32) * 2532 / 1170)
PH = SH + 32

# narração: id, texto, duração estimada (s) se não houver áudio
NARR = [
    ("N1", "Cartão de papel some. E o cliente some junto. Olha como é dar um carimbo no pontua.", 4.6),
    ("N2", "No balcão, a atendente busca a cliente pelo telefone.", 3.2),
    ("N3", "Confirma… e pronto: carimbo dado.", 2.6),
    ("N4", "Na mesma hora, a cliente recebe no WhatsApp quanto falta pro café grátis.", 4.0),
    ("N5", "E o cartão fica no celular dela. Sem baixar aplicativo, sem papel.", 3.8),
    ("N6", "Crie o seu grátis. Link na bio.", 2.2),
]
GAP = 0.35   # respiro entre falas
HEAD = 0.3   # silêncio inicial
TAIL = 1.6   # segura o CTA no fim


def dur(path):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                   "-of", "default=nw=1:nk=1", str(path)])
    return float(out)


def timeline(work):
    """Com audio/narracao.mp3 + audio/marcas.json (tempos medidos no áudio), usa as marcas;
    senão, usa N1..N6.mp3 ou as durações estimadas."""
    mj = work / "audio" / "marcas.json"
    if mj.exists() and (work / "audio" / "narracao.mp3").exists():
        m = json.loads(mj.read_text())
        segs = {k: (HEAD + a, HEAD + b) for k, (a, b) in m["segs"].items()}
        subs = {k: HEAD + v for k, v in m.get("subs", {}).items()}
        return segs, segs["N6"][1] + TAIL, subs
    t, segs = HEAD, {}
    for nid, _, est in NARR:
        a = work / "audio" / f"{nid}.mp3"
        d = dur(a) if a.exists() else est
        segs[nid] = (t, t + d)
        t += d + GAP
    total = segs["N6"][1] + TAIL
    a, b = segs["N1"]
    subs = {"s2": a + 1.1, "s3": a + 2.4, "dado": None, "link": segs["N6"][0] + 1.0}
    return segs, total, subs


def html(work, segs, total, subs):
    S = {k: [round(a, 3), round(b, 3)] for k, (a, b) in segs.items()}
    U = {k: (round(v, 3) if v is not None else None) for k, v in subs.items()}
    fl, fc = (work / "fl").as_uri(), (work / "fc").as_uri()
    nfl = len(list((work / "fl").glob("*.jpg")))
    nfc = len(list((work / "fc").glob("*.jpg")))
    notif_txt = ("Olá, Sabrina Alves.<br><br>Você recebeu um novo carimbo de Café da Esquina.<br><br>"
                 "No momento, faltam 2 carimbos para completar o cartão.")
    body = f"""
<div id="bg"><div class="grain"></div>
  <div class="orb" id="o1" style="width:900px;height:900px;background:#7B4DFF;top:-380px;right:-360px;opacity:.34"></div>
  <div class="orb" id="o2" style="width:800px;height:800px;background:#4A22C8;bottom:-360px;left:-320px;opacity:.30"></div>
</div>

<div id="top"><img src="{LOGO_CLARA}"></div>

<!-- gancho -->
<div class="cap" id="hook">
  <div class="l" id="h1">Cartão de papel <span class="am">some.</span></div>
  <div class="l" id="h2">E o cliente <span class="hl">some junto.</span></div>
</div>
<div class="cap" id="hook2"><div class="l small">Um carimbo no pontua, de verdade 👇</div></div>

<!-- legendas dos passos -->
<div class="cap step" id="c2"><span class="n">1</span><div>Busca a cliente<br><span class="hl">pelo telefone</span></div></div>
<div class="cap step" id="c3"><span class="n">2</span><div>Confirma<br><span class="am">e pronto: +1 carimbo</span></div></div>
<div class="cap step" id="c4"><span class="n wa">{WA_ICON}</span><div>Na hora, aviso<br><span class="hl">no WhatsApp</span></div></div>
<div class="cap step" id="c5"><span class="n">✓</span><div>Cartão no celular<br><span class="hl">sem app, sem papel</span></div></div>

<!-- celular -->
<div id="phone"><div class="scr"><img id="sv" src="{fl}/0001.jpg"><img id="sv2" src="{fc}/0001.jpg"></div>
  <div id="ring"></div>
</div>
<div id="who">celular da cliente</div>

<div class="badge" id="found">✓ Sabrina encontrada</div>
<div id="plus"><span>+1</span><small>carimbo</small></div>
<div id="burst"></div>

<!-- notificação WhatsApp -->
<div id="wa">
  <div class="hd"><span class="ic">{WA_ICON}</span><span class="ap">WhatsApp</span><span class="tm">agora</span></div>
  <div class="ti">Café da Esquina</div>
  <div class="tx">{notif_txt}</div>
  <div class="bt">Ver meu cartão</div>
</div>

<!-- CTA -->
<div id="cta">
  <img src="{LOGO_CLARA}" class="lg">
  <div class="t">Fidelidade que acontece<br>no <span class="hl">WhatsApp</span> do seu cliente.</div>
  <div class="pill">Crie o seu grátis · link na bio</div>
  <div class="hd2">@pontua.club</div>
</div>
"""
    css = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:{C['bg']}}}
body{{font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased;color:{C['text']};position:relative}}
#bg{{position:absolute;inset:0;background:radial-gradient(110% 60% at 80% 0%, #4A28C8 0%, #2A1470 35%, transparent 70%),
  radial-gradient(80% 50% at 0% 100%, #3A1BA8 0%, transparent 60%), #0E0822}}
.grain{{position:absolute;inset:0;opacity:.5;background-image:radial-gradient(circle at 1px 1px, rgba(255,255,255,.05) 1px, transparent 0);background-size:24px 24px}}
.orb{{position:absolute;border-radius:50%;filter:blur(130px)}}
#top{{position:absolute;top:120px;left:0;right:0;display:flex;justify-content:center}}
#top img{{height:54px}}
.cap{{position:absolute;left:70px;right:70px;top:250px;text-align:center;opacity:0}}
.cap .l{{font-size:92px;font-weight:800;letter-spacing:-.045em;line-height:1.05}}
.cap .l.small{{white-space:nowrap;font-size:50px;font-weight:700;letter-spacing:-.025em;color:#E6E0FF}}
#hook{{top:640px}} #hook2{{top:290px}}
.hl{{color:{C['lilac']};text-shadow:0 0 38px rgba(155,120,255,.65)}}
.am{{color:{C['amber']};text-shadow:0 0 34px rgba(255,194,77,.4)}}
.step{{display:flex;align-items:center;justify-content:center;gap:30px;text-align:left;top:240px}}
.step div{{font-size:64px;font-weight:800;letter-spacing:-.035em;line-height:1.06}}
.step .n{{flex:0 0 104px;height:104px;border-radius:30px;display:flex;align-items:center;justify-content:center;
  font-size:56px;font-weight:900;background:linear-gradient(135deg,{C['violet2']},{C['violet']});box-shadow:0 0 44px rgba(123,77,255,.7)}}
.step .n.wa{{background:{C['green']};box-shadow:0 0 44px rgba(37,211,102,.55)}}
.step .n.wa svg{{width:58px;height:58px}}
#phone{{position:absolute;left:{(W-PW)//2}px;top:470px;width:{PW}px;height:{PH}px;border-radius:78px;padding:16px;
  background:linear-gradient(145deg,#30265A,#0E0A1E);box-shadow:0 0 0 2px rgba(183,156,255,.4),0 0 110px rgba(123,77,255,.55),0 50px 90px rgba(0,0,0,.6);
  transform-origin:50% 30%}}
.scr{{width:100%;height:100%;border-radius:62px;overflow:hidden;position:relative;background:#111521}}
.scr img{{position:absolute;left:0;top:0;width:100%;height:auto}}
#sv2{{opacity:0}}
#who{{position:absolute;left:0;right:0;top:1745px;text-align:center;font-size:32px;font-weight:700;color:{C['muted']};opacity:0}}
#ring{{position:absolute;left:30px;right:30px;height:86px;border-radius:24px;border:5px solid {C['amber']};
  box-shadow:0 0 40px rgba(255,194,77,.7), inset 0 0 30px rgba(255,194,77,.25);opacity:0}}
.badge{{position:absolute;right:40px;top:1120px;padding:22px 30px;border-radius:22px;background:#E9FBEF;color:#0F5A2E;
  font-size:36px;font-weight:800;box-shadow:0 20px 50px rgba(0,0,0,.45),0 0 50px rgba(46,212,122,.45);opacity:0}}
#plus{{position:absolute;right:30px;top:1020px;width:400px;height:400px;border-radius:50%;display:flex;flex-direction:column;
  align-items:center;justify-content:center;background:radial-gradient(circle,#FFD777 0%,#FFC24D 55%,#E8A020 100%);color:#1A1030;
  box-shadow:0 0 0 14px rgba(255,194,77,.22),0 0 120px rgba(255,194,77,.75);opacity:0}}
#plus span{{font-size:170px;font-weight:900;letter-spacing:-.06em;line-height:.9}}
#plus small{{font-size:44px;font-weight:800;margin-top:6px}}
#burst{{position:absolute;left:850px;top:1220px;width:0;height:0}}
#burst i{{position:absolute;width:22px;height:22px;border-radius:50%;background:{C['amber']};opacity:0}}
#wa{{position:absolute;left:70px;right:70px;top:470px;padding:34px 38px 34px;border-radius:40px;background:rgba(248,246,255,.98);color:#141024;
  box-shadow:0 30px 80px rgba(0,0,0,.55),0 0 90px rgba(155,120,255,.45);opacity:0}}
#wa .hd{{display:flex;align-items:center;gap:16px;font-size:28px;color:#5B5473;font-weight:600}}
#wa .ic{{width:52px;height:52px;border-radius:15px;background:{C['green']};display:flex;align-items:center;justify-content:center}}
#wa .ic svg{{width:32px;height:32px}}
#wa .tm{{margin-left:auto;font-size:26px}}
#wa .ti{{font-size:40px;font-weight:800;margin-top:20px;letter-spacing:-.015em}}
#wa .tx{{font-size:35px;line-height:1.36;margin-top:12px;color:#2A2440}}
#wa .bt{{margin-top:26px;padding:22px;border-radius:20px;background:#EDE8FF;color:#4A2BC8;text-align:center;font-size:32px;font-weight:800}}
#cta{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:56px;opacity:0;padding-bottom:160px}}
#cta .lg{{height:96px}}
#cta .t{{font-size:74px;font-weight:800;letter-spacing:-.04em;line-height:1.08;text-align:center}}
#cta .pill{{padding:34px 56px;border-radius:999px;background:{C['amber']};color:#1A1030;font-size:46px;font-weight:900;
  box-shadow:0 14px 60px rgba(255,194,77,.4)}}
#cta .hd2{{font-size:36px;font-weight:700;color:{C['muted']}}}
"""
    js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f}, FL="{fl}", FC="{fc}", NFL={nfl}, NFC={nfc};
const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const ease=x=>1-Math.pow(1-cl(x),3);
const back=x=>{{x=cl(x);const c=1.9;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);}};
const io=(t,a,b,fi=.35,fo=.3)=>cl((t-a)/fi)*(1-cl((t-(b-fo))/fo));   // fade in/out
const lerp=(a,b,x)=>a+(b-a)*cl(x);
const pad=n=>String(n).padStart(4,'0');
// burst particles
for(let i=0;i<14;i++){{const e=document.createElement('i');$('burst').appendChild(e);}}
let lastA='',lastB='';
window.R=async function(t){{
  const [n1a,n1b]=S.N1,[n2a,n2b]=S.N2,[n3a,n3b]=S.N3,[n4a,n4b]=S.N4,[n5a,n5b]=S.N5,[n6a,n6b]=S.N6;
  const tp=U.dado!=null?U.dado:n3a+(16.2-12.3)/(17.6-12.3)*(n3b-n3a);
  // gancho
  const h1=ease((t-(n1a-.05))/.45), h2=ease((t-(U.s2-.1))/.45);
  $('h1').style.cssText=`opacity:${{h1}};transform:translateY(${{(1-h1)*40}}px)`;
  $('h2').style.cssText=`opacity:${{h2}};transform:translateY(${{(1-h2)*40}}px)`;
  const hookOut=cl((t-(U.s3-.35))/.35);
  $('hook').style.opacity=1-hookOut;
  $('hook').style.transform=`translateY(${{-hookOut*60}}px)`;
  $('hook2').style.opacity=io(t,U.s3-.05,n2a+.15,.35,.25);
  // celular entra
  const pe=ease((t-(U.s3-.1))/.6);
  const ctaK=ease((t-(n6a-.15))/.5);
  $('phone').style.opacity=pe*(1-ctaK);
  const dip=1-.04*cl(1-Math.abs(t-(n4a-.2))/.25);
  $('phone').style.transform=`translateY(${{(1-pe)*700 + ctaK*300}}px) scale(${{(1-ctaK*.1)*dip}})`;
  $('who').style.opacity=io(t,n4a-.2,n6a-.1,.3,.25)*(1-ctaK);
  $('top').style.opacity=1-ctaK;
  // tela: lojista — busca (5.0→12.3s do vídeo) durante N2; confirma (12.3→17.6s) durante N3
  let src=FL, fr=1, cli=0;
  if(t<n2a) fr=4.0*30;
  else if(t<n3a) fr=lerp(5.0,12.3,(t-n2a)/(n3a-n2a-.1))*30;
  else if(t<n4a-.2) fr=(t<tp? lerp(12.3,16.15,(t-n3a)/(tp-n3a)) : lerp(16.15,17.6,(t-tp)/.6))*30;
  else {{ fr=17.6*30; }}
  // cliente: 7/10 durante N4, 8/10 a partir de N5
  if(t>=n4a-.3){{ cli=ease((t-(n4a-.3))/.18); }}
  const fcN = t<n5a ? 30 : 650;
  const a=`${{FL}}/${{pad(Math.min(NFL,Math.max(1,Math.round(fr)+1)))}}.jpg`;
  const b=`${{FC}}/${{pad(fcN)}}.jpg`;
  const ps=[];
  if(a!==lastA){{ $('sv').src=a; lastA=a; ps.push($('sv').decode().catch(()=>{{}})); }}
  if(b!==lastB){{ $('sv2').src=b; lastB=b; ps.push($('sv2').decode().catch(()=>{{}})); }}
  $('sv').style.opacity=1-cli; $('sv2').style.opacity=cli;
  // flash ao trocar 7→8
  const fl8=cl(1-Math.abs(t-n5a)/.25);
  $('sv2').style.filter=`brightness(${{1+fl8*.6}})`;
  // anel em "8 de 10 carimbos" (52% da altura da tela)
  const rg=io(t,n5a+.35,n6a-.1,.3,.25);
  $('ring').style.cssText=`opacity:${{rg}};top:${{16+0.52*{SH}-43}}px;transform:scale(${{lerp(1.15,1,(t-n5a-.35)/.3)}})`;
  // legendas
  $('c2').style.opacity=io(t,n2a,n3a+.05); $('c2').style.transform=`translateY(${{(1-ease((t-n2a)/.35))*30}}px)`;
  $('c3').style.opacity=io(t,n3a+.05,n4a-.1); $('c3').style.transform=`translateY(${{(1-ease((t-n3a)/.35))*30}}px)`;
  $('c4').style.opacity=io(t,n4a-.1,n5a); $('c4').style.transform=`translateY(${{(1-ease((t-n4a)/.35))*30}}px)`;
  $('c5').style.opacity=io(t,n5a,n6a-.1); $('c5').style.transform=`translateY(${{(1-ease((t-n5a)/.35))*30}}px)`;
  // selo "encontrada" (no vídeo aparece em ~10.5s)
  const tf=n2a+(10.6-5.0)/(12.3-5.0)*(n3a-n2a-.1);
  const fb=back((t-tf)/.4);
  $('found').style.cssText=`opacity:${{cl((t-tf)/.15)*(1-cl((t-(n3a+.4))/.3))}};transform:scale(${{fb}}) rotate(-3deg)`;
  // +1 (no vídeo: tela de sucesso ~16.2s)
  const pb=back((t-tp)/.45);
  const pOut=cl((t-(n4a-.45))/.2);
  $('plus').style.cssText=`opacity:${{cl((t-tp)/.12)*(1-pOut)}};transform:scale(${{pb*(1-pOut*.3)}}) rotate(${{-8+pb*4}}deg)`;
  // partículas
  [...$('burst').children].forEach((e,i)=>{{
    const k=cl((t-tp)/.8), ang=i/14*Math.PI*2, r=80+k*330;
    e.style.cssText=`opacity:${{t>tp?(1-k):0}};transform:translate(${{Math.cos(ang)*r}}px,${{Math.sin(ang)*r}}px) scale(${{1-k*.5}})`;
  }});
  // WhatsApp
  const wi=back((t-(n4a+.15))/.5), wo=cl((t-(n5a-.1))/.35);
  $('wa').style.cssText=`opacity:${{cl((t-(n4a+.15))/.2)*(1-wo)}};transform:translateY(${{(1-wi)*-260 - wo*200}}px) scale(${{.96+wi*.04}})`;
  // telefone desce um pouco quando a notificação está na tela
  // CTA
  const ci=ease((t-n6a)/.5);
  $('cta').style.opacity=ci;
  $('cta').style.transform=`translateY(${{(1-ci)*50}}px)`;
  await Promise.all(ps);
}};
"""
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{FONTS}{EMOJI_CSS}{css}</style>'
            f'</head><body>{_emoji(body)}<script>{js}</script></body></html>')


def render(work, only=None):
    segs, total, subs = timeline(work)
    (work / "reel.html").write_text(html(work, segs, total, subs), encoding="utf-8")
    fdir = work / "frames"
    fdir.mkdir(exist_ok=True)
    for f in fdir.glob("*.jpg"):
        f.unlink()
    from playwright.sync_api import sync_playwright
    n = int(total * FPS)
    idx = range(n) if only is None else only
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H})
        pg.goto((work / "reel.html").as_uri())
        pg.wait_for_timeout(500)
        pg.evaluate("document.fonts.ready")
        for i in idx:
            pg.evaluate(f"R({i / FPS})")
            pg.screenshot(path=str(fdir / f"{i:05d}.jpg"), type="jpeg", quality=92)
        b.close()
    return segs, total, subs


def encode(work, segs, total):
    vid = work / "video_only.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", str(work / "frames/%05d.jpg"),
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", str(vid)], check=True)
    full = work / "audio" / "narracao.mp3"
    if (work / "audio" / "marcas.json").exists() and full.exists():
        out = work / "reel_carimbo.mp4"
        ms = int(HEAD * 1000)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(vid), "-i", str(full), "-filter_complex",
                        f"[1:a]adelay={ms}|{ms},loudnorm=I=-14:TP=-1.5:LRA=11,apad,atrim=0:{total:.3f}[aout]",
                        "-map", "0:v", "-map", "[aout]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                        "-ar", "48000", "-shortest", "-movflags", "+faststart", str(out)], check=True)
        return out
    auds = [(k, work / "audio" / f"{k}.mp3") for k, *_ in NARR]
    auds = [(k, a) for k, a in auds if a.exists()]
    out = work / "reel_carimbo.mp4"
    if not auds:
        vid.rename(out)
        return out
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(vid)]
    flt = []
    for j, (k, a) in enumerate(auds, 1):
        cmd += ["-i", str(a)]
        ms = int(segs[k][0] * 1000)
        flt.append(f"[{j}:a]adelay={ms}|{ms}[a{j}]")
    sfx = work / "audio" / "sfx"
    mix_in = "".join(f"[a{j}]" for j in range(1, len(auds) + 1))
    n_in = len(auds)
    extra = []
    for name, at in (("pop", None), ("ding", None)):
        pass
    flt.append(f"{mix_in}amix=inputs={n_in}:normalize=0,apad,atrim=0:{total:.3f}[aout]")
    cmd += ["-filter_complex", ";".join(flt), "-map", "0:v", "-map", "[aout]",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", str(out)]
    subprocess.run(cmd, check=True)
    return out


if __name__ == "__main__":
    work = Path(sys.argv[1]).resolve()
    if len(sys.argv) > 2 and sys.argv[2] == "preview":
        segs, total, subs = timeline(work)
        ts = [float(x) for x in sys.argv[3].split(",")]
        render(work, only=[int(x * FPS) for x in ts])
        print(json.dumps({"total": total, "segs": segs}))
    else:
        segs, total, subs = render(work)
        print(encode(work, segs, total))
