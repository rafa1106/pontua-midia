# -*- coding: utf-8 -*-
"""Renderizador v2 — visual "neon roxo + WhatsApp" (padrão do feed a partir de 09/2026).

Uso: from render2 import *  ->  build([...slides...], "prefixo")  gera ../artes/<prefixo>_NN.jpg
Regras de conteúdo: ../estrategia/guia_conteudo.md
"""
import os, base64, html as _h
from pathlib import Path
from render import FONTS, OUT, HERE, ROOT, W, H, HANDLE, SITE, LOGO_CLARA, SIMBOLO

TWEMOJI = ROOT / "node_modules/@twemoji/svg"
EMOJI_CSS = ".emj{height:1.05em;width:1.05em;vertical-align:-0.18em;display:inline-block}"
import re as _re
_EMJ = _re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B50\u2764]\uFE0F?")

def _emoji(html_str):
    """Troca emoji por <img> Twemoji (o Chromium headless não desenha fonte de emoji colorida)."""
    def rep(m):
        cp = "-".join(f"{ord(c):x}" for c in m.group(0) if c != "\ufe0f")
        f = TWEMOJI / f"{cp}.svg"
        return f'<img class="emj" src="file://{f}">' if f.exists() else m.group(0)
    return _EMJ.sub(rep, html_str)

C = dict(bg="#0B0816", bg2="#140E2A", violet="#5B34E8", violet2="#7B4DFF", lilac="#B79CFF",
         amber="#FFC24D", text="#F4F1FF", muted="#A99FCB", green="#25D366", loss="#FF6B6B", gain="#2ED47A")

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:{C['bg']}}}
body{{font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased;color:{C['text']};
     font-feature-settings:'ss01','cv11'}}
.s{{position:relative;width:{W}px;height:{H}px;overflow:hidden;padding:92px 84px 0;display:flex;flex-direction:column;
   background:radial-gradient(120% 80% at 85% -10%, #3A1F9A 0%, transparent 55%),
              radial-gradient(90% 70% at -10% 110%, #2A1470 0%, transparent 60%), {C['bg']}}}
.s.hero{{background:radial-gradient(110% 75% at 80% 0%, #5B34E8 0%, #3A1F9A 30%, transparent 65%),
              radial-gradient(80% 60% at 0% 100%, #4A22C8 0%, transparent 60%), #120A2A}}
.grain{{position:absolute;inset:0;pointer-events:none;opacity:.55;
  background-image:radial-gradient(circle at 1px 1px, rgba(255,255,255,.05) 1px, transparent 0);background-size:24px 24px}}
.orb{{position:absolute;border-radius:50%;filter:blur(110px);pointer-events:none}}
.z{{position:relative;z-index:2}}
.eb{{font-size:25px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C['lilac']}}}
.t1{{font-size:92px;font-weight:800;line-height:1.04;letter-spacing:-.045em}}
.t2{{font-size:70px;font-weight:800;line-height:1.08;letter-spacing:-.038em}}
.t3{{font-size:56px;font-weight:800;line-height:1.12;letter-spacing:-.03em}}
.hl{{color:{C['lilac']};text-shadow:0 0 38px rgba(155,120,255,.65)}}
.am{{color:{C['amber']};text-shadow:0 0 34px rgba(255,194,77,.35)}}
.bd{{font-size:34px;line-height:1.42;letter-spacing:-.012em;color:#D9D2F5;font-weight:400}}
.bd b{{color:#fff;font-weight:700}}
.sm{{font-size:25px;line-height:1.4;color:{C['muted']}}}
.big{{font-size:210px;font-weight:900;line-height:.95;letter-spacing:-.06em}}
.idx{{position:absolute;top:60px;right:76px;font-size:23px;font-weight:700;letter-spacing:.1em;color:{C['muted']};opacity:.8;z-index:3}}
.foot{{position:absolute;left:84px;right:84px;bottom:62px;display:flex;justify-content:space-between;align-items:center;
      font-size:23px;font-weight:600;color:{C['muted']};z-index:3}}
.foot .b{{display:flex;align-items:center;gap:14px}}
.pill{{display:inline-flex;align-items:center;gap:12px;padding:20px 34px;border-radius:999px;font-size:28px;font-weight:800;
      background:{C['amber']};color:#1A1030;box-shadow:0 10px 40px rgba(255,194,77,.25)}}
.card{{background:rgba(255,255,255,.055);border:1.5px solid rgba(183,156,255,.22);border-radius:28px;padding:34px 38px;
      backdrop-filter:blur(8px)}}
.row{{display:flex;gap:24px;align-items:flex-start}}
.num{{flex:0 0 58px;height:58px;border-radius:18px;display:flex;align-items:center;justify-content:center;
     font-size:28px;font-weight:800;background:linear-gradient(135deg,{C['violet2']},{C['violet']});color:#fff;
     box-shadow:0 0 30px rgba(123,77,255,.55)}}
/* celular */
.phone{{position:absolute;width:470px;height:960px;border-radius:70px;padding:16px;
  background:linear-gradient(145deg,#2B2250,#0E0A1E);box-shadow:0 0 0 2px rgba(183,156,255,.35),0 0 90px rgba(123,77,255,.55),0 40px 80px rgba(0,0,0,.6)}}
.scr{{width:100%;height:100%;border-radius:56px;overflow:hidden;position:relative;background:#0B141A}}
.notch{{position:absolute;top:18px;left:50%;transform:translateX(-50%);width:130px;height:36px;border-radius:20px;background:#000;z-index:5}}
.wa-h{{height:150px;background:#1F2C34;display:flex;align-items:flex-end;gap:16px;padding:0 26px 22px}}
.wa-h img{{width:56px;height:56px;border-radius:50%;background:#fff}}
.wa-h .n{{font-size:25px;font-weight:700;color:#E9EDEF}} .wa-h .st{{font-size:18px;color:#8696A0}}
.wa-b{{padding:24px 18px;display:flex;flex-direction:column;gap:16px;
  background:radial-gradient(circle at 1px 1px, rgba(255,255,255,.035) 1px, transparent 0) #0B141A;background-size:20px 20px;height:100%}}
.msg{{align-self:flex-start;max-width:92%;background:#202C33;color:#E9EDEF;border-radius:4px 22px 22px 22px;
  padding:16px 20px 30px;font-size:22.5px;line-height:1.36;position:relative}}
.msg .tm{{position:absolute;right:14px;bottom:8px;font-size:15px;color:#8696A0}}
.day{{align-self:center;background:#1F2C34;color:#8696A0;font-size:16px;padding:6px 14px;border-radius:10px}}
.notif{{position:absolute;display:flex;gap:18px;align-items:center;padding:22px 26px;border-radius:26px;
  background:rgba(245,242,255,.97);color:#141024;box-shadow:0 20px 60px rgba(0,0,0,.45),0 0 60px rgba(155,120,255,.35);z-index:6}}
.notif .ic{{flex:0 0 58px;height:58px;border-radius:16px;background:{C['green']};display:flex;align-items:center;justify-content:center}}
.notif .a{{font-size:19px;font-weight:700;color:#5B5473;letter-spacing:.02em}}
.notif .t{{font-size:25px;font-weight:800;letter-spacing:-.01em;margin-top:2px}}
.notif .d{{font-size:21px;color:#3A3450;margin-top:2px}}
.src{{font-size:19px;color:{C['muted']};opacity:.85}}
"""

WA_ICON = ('<svg width="34" height="34" viewBox="0 0 24 24" fill="#fff"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2'
           'a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1'
           'c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.2.1-.2 0-.3 0-.4l-.8-1.9c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3'
           ' 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3'
           'c-.1-.1-.3-.2-.5-.3z"/></svg>')


def _page(inner):
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{FONTS}{EMOJI_CSS}{CSS}</style>'
            f'</head><body>{_emoji(inner)}</body></html>')


def _foot(idx, big_logo=False):
    left = (f'<img src="{LOGO_CLARA}" style="height:54px">' if big_logo else
            f'<span class="b"><img src="{SIMBOLO}" style="height:44px;width:44px">{HANDLE}</span>')
    return f'<div class="foot">{left}<span>{idx or ""}</span></div>'


def _bg(hero=False):
    return (f'<div class="grain"></div>'
            f'<div class="orb" style="width:620px;height:620px;background:#7B4DFF;opacity:{.32 if hero else .18};top:-260px;right:-220px"></div>'
            f'<div class="orb" style="width:520px;height:520px;background:#4A22C8;opacity:.28;bottom:-240px;left:-200px"></div>')


def notif(app, title, desc, style):
    return (f'<div class="notif" style="{style}"><div class="ic">{WA_ICON}</div>'
            f'<div><div class="a">WHATSAPP · agora</div><div class="t">{title}</div><div class="d">{desc}</div></div></div>')


def phone_chat(business, msgs, style, day="Hoje"):
    """msgs: lista de (texto, hora)."""
    bubbles = "".join(f'<div class="msg">{m}<span class="tm">{t}</span></div>' for m, t in msgs)
    return (f'<div class="phone" style="{style}"><div class="scr"><div class="notch"></div>'
            f'<div class="wa-h"><img src="{SIMBOLO}"><div><div class="n">{business}</div><div class="st">conta comercial</div></div></div>'
            f'<div class="wa-b"><div class="day">{day}</div>{bubbles}</div></div></div>')


# ---------------- layouts ----------------

def cover(eyebrow, title, sub, cta="Arraste →", notif_t=None, notif_d=None, phone_msgs=None, business="Seu negócio"):
    art = ""
    if phone_msgs:
        art = phone_chat(business, phone_msgs, "right:-60px;bottom:-440px;transform:rotate(-8deg)")
    if notif_t:
        art += notif("", notif_t, notif_d, "right:110px;bottom:455px;width:610px;transform:rotate(-3deg)")
    return _page(f"""<div class="s hero">{_bg(True)}
  <img class="z" src="{LOGO_CLARA}" style="height:58px;align-self:flex-start">
  <div class="eb z" style="margin-top:56px;color:{C['amber']}">{eyebrow}</div>
  <div class="t1 z" style="margin-top:30px;max-width:900px">{title}</div>
  <div class="bd z" style="margin-top:34px;max-width:{600 if art else 820}px">{sub}</div>
  {art}
  <div class="foot"><span class="pill">{cta}</span><span>{HANDLE}</span></div>
</div>""")


def text(idx, title, body, eyebrow="", tsize="t2"):
    eb = f'<div class="eb z">{eyebrow}</div>' if eyebrow else ""
    return _page(f"""<div class="s">{_bg()}<div class="idx">{idx}</div>{eb}
  <div style="flex:1"></div>
  <div class="{tsize} z">{title}</div>
  <div class="bd z" style="margin-top:42px;max-width:860px">{body}</div>
  <div style="flex:1.45"></div>{_foot(idx)}</div>""")


def stat(idx, big, color, kicker, body, src=""):
    s = f'<div class="src z" style="margin-top:30px">{src}</div>' if src else ""
    return _page(f"""<div class="s">{_bg()}<div class="idx">{idx}</div>
  <div class="eb z">{kicker}</div><div style="flex:1"></div>
  <div class="big z" style="color:{color};text-shadow:0 0 60px {color}55">{big}</div>
  <div class="bd z" style="margin-top:48px;max-width:860px">{body}</div>{s}
  <div style="flex:1.45"></div>{_foot(idx)}</div>""")


def listing(idx, title, items, eyebrow=""):
    eb = f'<div class="eb z">{eyebrow}</div>' if eyebrow else ""
    rows = "".join(f"""<div class="row z" style="margin-top:40px"><div class="num">{i}</div><div>
      <div style="font-size:37px;font-weight:700;letter-spacing:-.02em;line-height:1.18">{h}</div>
      <div class="sm" style="margin-top:10px;max-width:720px;font-size:27px">{s}</div></div></div>"""
                   for i, (h, s) in enumerate(items, 1))
    return _page(f"""<div class="s">{_bg()}<div class="idx">{idx}</div>{eb}
  <div style="flex:.6"></div><div class="t3 z">{title}</div><div style="margin-top:16px">{rows}</div>
  <div style="flex:1"></div>{_foot(idx)}</div>""")


def compare(idx, title, lt, litems, rt, ritems):
    def col(t, items, color, sign, border):
        li = "".join(f'<div style="display:flex;gap:14px;margin-top:22px"><span style="color:{color};font-weight:900;font-size:28px">{sign}</span>'
                     f'<span style="font-size:27px;line-height:1.3;color:#E4DEFA">{x}</span></div>' for x in items)
        return (f'<div class="card" style="flex:1;border-color:{border}"><div style="font-size:31px;font-weight:800;color:{color}">{t}</div>'
                f'<div style="height:2px;background:{border};margin-top:20px;opacity:.6"></div>{li}</div>')
    return _page(f"""<div class="s">{_bg()}<div class="idx">{idx}</div>
  <div class="t3 z" style="margin-top:20px">{title}</div>
  <div class="z" style="display:flex;gap:24px;margin-top:48px">
    {col(lt, litems, C['loss'], "✕", "rgba(255,107,107,.45)")}
    {col(rt, ritems, C['gain'], "✓", "rgba(46,212,122,.5)")}</div>
  <div style="flex:1"></div>{_foot(idx)}</div>""")


def whatsapp(idx, title, business, msgs, caption="", eyebrow=""):
    eb = f'<div class="eb z">{eyebrow}</div>' if eyebrow else ""
    cap = f'<div class="bd z" style="margin-top:26px;max-width:470px;font-size:30px">{caption}</div>' if caption else ""
    return _page(f"""<div class="s">{_bg()}<div class="idx">{idx}</div>{eb}
  <div class="t3 z" style="margin-top:{24 if eyebrow else 40}px;max-width:520px">{title}</div>{cap}
  {phone_chat(business, msgs, "right:48px;top:230px;transform:rotate(4deg)")}
  {_foot(idx)}</div>""")


def cta(idx, title, body, button="Crie o seu grátis · link na bio", ps=""):
    p = f'<div class="sm z" style="margin-top:30px;max-width:820px">{ps}</div>' if ps else ""
    return _page(f"""<div class="s hero">{_bg(True)}<div class="idx">{idx}</div>
  <div style="flex:1"></div><div class="t2 z">{title}</div>
  <div class="bd z" style="margin-top:38px;max-width:840px">{body}</div>
  <div class="z" style="margin-top:54px"><span class="pill" style="font-size:31px;padding:26px 42px">{button}</span></div>{p}
  <div style="flex:1.2"></div>
  <div class="foot"><img src="{LOGO_CLARA}" style="height:58px"><span style="color:#D9D2F5">fidelidade que aproxima clientes e negócios</span></div>
</div>""")


def image(path, erase_br=False):
    """Slide a partir de uma arte pronta (PNG/JPG): encaixa em 1080x1350. erase_br apaga o canto inferior direito (marca d'água)."""
    from PIL import Image, ImageFilter
    im = Image.open(path).convert("RGB")
    sc = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    l, t = (im.width - W) // 2, (im.height - H) // 2
    im = im.crop((l, t, l + W, t + H))
    if erase_br:
        box = (W - 150, H - 150, W, H)
        patch = im.crop((W - 300, H - 150, W - 150, H)).filter(ImageFilter.GaussianBlur(6))
        im.paste(patch, box[:2])
    return im


def build(slides, prefix):
    """slides: HTML (str) ou PIL.Image (de image())."""
    from playwright.sync_api import sync_playwright
    paths = []
    with sync_playwright() as p:
        exe = os.environ.get("CHROMIUM_PATH") or next((str(c) for c in [Path("/opt/pw-browsers/chromium")] if c.exists()), None)
        b = p.chromium.launch(executable_path=exe, args=["--font-render-hinting=none", "--force-color-profile=srgb"])
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        for i, s in enumerate(slides, 1):
            out = OUT / f"{prefix}_{i:02d}.jpg"
            if isinstance(s, str):
                f = OUT / f"{prefix}_{i:02d}.html"
                f.write_text(s, encoding="utf-8")
                pg.goto(f"file://{f}"); pg.evaluate("document.fonts.ready.then(()=>Promise.all([...document.fonts].filter(f=>f.status!=='loaded' && f.family.includes('Emoji')).map(f=>f.load().catch(()=>0))))"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(600)
                pg.screenshot(path=str(out), type="jpeg", quality=93)
                f.unlink()
            else:
                s.save(out, quality=93)
            paths.append(str(out))
        b.close()
    return paths
