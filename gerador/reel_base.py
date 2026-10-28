# -*- coding: utf-8 -*-
"""Base comum dos Reels 1080x1920 (visual neon roxo + WhatsApp).

Cada Reel define: corpo HTML, CSS extra e a função JS R(t) (deterministica por tempo).
A narração (audio/narracao.mp3) e as marcas medidas (audio/marcas.json) definem a linha do tempo.
"""
import json, subprocess
from pathlib import Path
from render2 import FONTS, EMOJI_CSS, C, WA_ICON, LOGO_CLARA, SIMBOLO, _emoji

FPS = 30
W, H = 1080, 1920
HEAD = 0.3   # silêncio antes da 1ª fala
TAIL = 1.6   # segura o CTA no fim


def marcas(work):
    m = json.loads((work / "audio" / "marcas.json").read_text())
    segs = {k: [round(HEAD + a, 3), round(HEAD + b, 3)] for k, (a, b) in m["segs"].items()}
    subs = {k: round(HEAD + v, 3) for k, v in m.get("subs", {}).items()}
    return segs, subs, segs["N6"][1] + TAIL


BASE_CSS = f"""
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
.hl{{color:{C['lilac']};text-shadow:0 0 38px rgba(155,120,255,.65)}}
.am{{color:{C['amber']};text-shadow:0 0 34px rgba(255,194,77,.4)}}
.step{{display:flex;align-items:center;justify-content:center;gap:30px;text-align:left;top:240px}}
.step div{{font-size:64px;font-weight:800;letter-spacing:-.035em;line-height:1.06}}
.step .n{{flex:0 0 104px;height:104px;border-radius:30px;display:flex;align-items:center;justify-content:center;
  font-size:56px;font-weight:900;background:linear-gradient(135deg,{C['violet2']},{C['violet']});box-shadow:0 0 44px rgba(123,77,255,.7)}}
.step .n.wa{{background:{C['green']};box-shadow:0 0 44px rgba(37,211,102,.55)}}
.step .n.wa svg{{width:58px;height:58px}}
.badge{{position:absolute;padding:22px 30px;border-radius:22px;background:#E9FBEF;color:#0F5A2E;white-space:nowrap;
  font-size:38px;font-weight:800;box-shadow:0 20px 50px rgba(0,0,0,.45),0 0 50px rgba(46,212,122,.45);opacity:0}}
.chip{{position:absolute;padding:26px 40px;border-radius:999px;background:{C['amber']};color:#1A1030;white-space:nowrap;
  font-size:44px;font-weight:900;box-shadow:0 14px 60px rgba(255,194,77,.45);opacity:0}}
.wa{{position:absolute;left:70px;right:70px;padding:34px 38px 34px;border-radius:40px;background:rgba(248,246,255,.98);color:#141024;
  box-shadow:0 30px 80px rgba(0,0,0,.55),0 0 90px rgba(155,120,255,.45);opacity:0}}
.wa .hd{{display:flex;align-items:center;gap:16px;font-size:28px;color:#5B5473;font-weight:600}}
.wa .ic{{width:52px;height:52px;border-radius:15px;background:{C['green']};display:flex;align-items:center;justify-content:center}}
.wa .ic svg{{width:32px;height:32px}}
.wa .tm{{margin-left:auto;font-size:26px}}
.wa .ti{{font-size:40px;font-weight:800;margin-top:20px;letter-spacing:-.015em}}
.wa .tx{{font-size:35px;line-height:1.36;margin-top:12px;color:#2A2440}}
.wa .bt{{margin-top:22px;padding:22px;border-radius:20px;background:#EDE8FF;color:#4A2BC8;text-align:center;font-size:32px;font-weight:800}}
#cta{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:56px;opacity:0;padding-bottom:160px}}
#cta .lg{{height:96px}}
#cta .t{{font-size:74px;font-weight:800;letter-spacing:-.04em;line-height:1.08;text-align:center}}
#cta .pill{{padding:34px 56px;border-radius:999px;background:{C['amber']};color:#1A1030;font-size:46px;font-weight:900;
  box-shadow:0 14px 60px rgba(255,194,77,.4)}}
#cta .hd2{{font-size:36px;font-weight:700;color:{C['muted']}}}
"""

BG = """<div id="bg"><div class="grain"></div>
  <div class="orb" style="width:900px;height:900px;background:#7B4DFF;top:-380px;right:-360px;opacity:.34"></div>
  <div class="orb" style="width:800px;height:800px;background:#4A22C8;bottom:-360px;left:-320px;opacity:.30"></div>
</div>"""

TOP = f'<div id="top"><img src="{LOGO_CLARA}"></div>'

CTA = f"""<div id="cta">
  <img src="{LOGO_CLARA}" class="lg">
  <div class="t">Fidelidade que acontece<br>no <span class="hl">WhatsApp</span> do seu cliente.</div>
  <div class="pill">Crie o seu grátis · link na bio</div>
  <div class="hd2">@pontua.club</div>
</div>"""


def wa_card(id_, title, text_html, buttons=(), top=470):
    bts = "".join(f'<div class="bt">{b}</div>' for b in buttons)
    return (f'<div class="wa" id="{id_}" style="top:{top}px"><div class="hd"><span class="ic">{WA_ICON}</span>'
            f'<span>WhatsApp</span><span class="tm">agora</span></div><div class="ti">{title}</div>'
            f'<div class="tx">{text_html}</div>{bts}</div>')


JS_HELPERS = """
const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const ease=x=>1-Math.pow(1-cl(x),3);
const back=x=>{x=cl(x);const c=1.9;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);};
const io=(t,a,b,fi=.35,fo=.3)=>cl((t-a)/fi)*(1-cl((t-(b-fo))/fo));
const lerp=(a,b,x)=>a+(b-a)*cl(x);
const pad=n=>String(n).padStart(4,'0');
// piecewise: [[t0,v0],[t1,v1],...] -> v(t)
const pw=(pts,t)=>{if(t<=pts[0][0])return pts[0][1];for(let i=1;i<pts.length;i++){if(t<=pts[i][0]){const [a,va]=pts[i-1],[b,vb]=pts[i];return va+(vb-va)*(t-a)/(b-a);}}return pts[pts.length-1][1];};
const swaps={};
function setImg(el,src,ps){ if(swaps[el.id]!==src){ el.src=src; swaps[el.id]=src; ps.push(el.decode().catch(()=>{})); } }
function show(id,t,a,b,dy=30){ const e=$(id); e.style.opacity=io(t,a,b); e.style.transform=`translateY(${(1-ease((t-a)/.35))*dy}px)`; }
function pop(id,t,a,b,rot=0){ const e=$(id); const k=back((t-a)/.4); const o=cl((t-a)/.12)*(1-cl((t-(b-.25))/.25));
  e.style.opacity=o; e.style.transform=`scale(${k}) rotate(${rot}deg)`; }
function cta(t,a){ const ci=ease((t-a)/.5); $('cta').style.opacity=ci; $('cta').style.transform=`translateY(${(1-ci)*50}px)`; return ease((t-(a-.15))/.5); }
"""


def page(body, css_extra, js):
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{FONTS}{EMOJI_CSS}{BASE_CSS}{css_extra}</style>'
            f'</head><body>{_emoji(body)}<script>{JS_HELPERS}{js}</script></body></html>')


def render(work, html_str, total, only=None):
    (work / "reel.html").write_text(html_str, encoding="utf-8")
    fdir = work / "frames"
    fdir.mkdir(exist_ok=True)
    for f in fdir.glob("*.jpg"):
        f.unlink()
    from playwright.sync_api import sync_playwright
    idx = range(int(total * FPS)) if only is None else only
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


def encode(work, total, out_name):
    vid = work / "video_only.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", str(work / "frames/%05d.jpg"),
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", str(vid)], check=True)
    out = work / out_name
    full = work / "audio" / "narracao.mp3"
    if not full.exists():
        vid.replace(out)
        return out
    ms = int(HEAD * 1000)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(vid), "-i", str(full), "-filter_complex",
                    f"[1:a]adelay={ms}|{ms},loudnorm=I=-14:TP=-1.5:LRA=11,apad,atrim=0:{total:.3f}[aout]",
                    "-map", "0:v", "-map", "[aout]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                    "-ar", "48000", "-shortest", "-movflags", "+faststart", str(out)], check=True)
    return out


def main(build, out_name, argv):
    """build(work) -> (html, total). argv: <pasta> [preview t1,t2,...]"""
    work = Path(argv[1]).resolve()
    html_str, total = build(work)
    if len(argv) > 3 and argv[2] == "preview":
        render(work, html_str, total, only=[int(float(x) * FPS) for x in argv[3].split(",")])
        print(json.dumps({"total": total}))
    else:
        render(work, html_str, total)
        print(encode(work, total, out_name))
