# -*- coding: utf-8 -*-
"""Renderiza slides HTML -> JPEG 1080x1350 usando Chromium/Playwright.

Uso:  python3 c1.py            (gera em ../artes/<prefixo>_NN.jpg)
Deps: pip install playwright ; npm install @fontsource/inter (na raiz do repo)
"""
import os, sys
from pathlib import Path
from brand import BRAND, FONT_CSS, W, H, HANDLE, SITE

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
IDIR = os.environ.get("INTER_DIR") or str(
    next((p for p in [ROOT / "node_modules/@fontsource/inter/files",
                      Path.home() / "pontua/node_modules/@fontsource/inter/files"] if p.exists()),
         ROOT / "node_modules/@fontsource/inter/files"))
LORA = os.environ.get("LORA_FONT") or next(
    (str(c) for c in [Path("/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf"),
                      ROOT / "node_modules/@fontsource/lora/files/lora-latin-400-italic.woff2"]
     if c.exists()),
    "/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf")
import base64
def _uri(n): return "data:image/png;base64," + base64.b64encode((HERE / "marca" / n).read_bytes()).decode()
LOGO_CLARA, LOGO_ESCURA, SIMBOLO = _uri("logo_clara.png"), _uri("logo_escura.png"), _uri("simbolo.png")

def brand_foot(theme):
    """Assinatura dos slides internos: símbolo + @handle."""
    return f'<span style="display:flex;align-items:center;gap:14px"><img src="{SIMBOLO}" style="height:44px;width:44px"><span>{HANDLE}</span></span>'

OUT = Path(os.environ.get("ARTES_DIR") or (ROOT / "artes"))
OUT.mkdir(parents=True, exist_ok=True)

FONTS = (FONT_CSS.replace("{IDIR}", IDIR).replace("{LORA}", LORA)
         .replace("{LORA_FMT}", "woff2" if LORA.endswith(".woff2") else "truetype"))

BASE_CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased;
      text-rendering:geometricPrecision;font-feature-settings:'ss01','cv11';}}
.slide{{position:relative;width:{W}px;height:{H}px;padding:96px 88px;
        display:flex;flex-direction:column;overflow:hidden}}
.dark{{background:{BRAND['ink']};color:#fff}}
.light{{background:{BRAND['paper']};color:{BRAND['ink']}}}
.violet{{background:linear-gradient(155deg,{BRAND['primary']} 0%,#3D1FA8 55%,#25105F 100%);color:#fff}}
.grain{{position:absolute;inset:0;opacity:.5;pointer-events:none;
  background-image:radial-gradient(circle at 1px 1px, rgba(255,255,255,.055) 1px, transparent 0);
  background-size:26px 26px}}
.grain.on-light{{background-image:radial-gradient(circle at 1px 1px, rgba(13,10,24,.055) 1px, transparent 0)}}
.glow{{position:absolute;border-radius:50%;filter:blur(120px);pointer-events:none}}
.eyebrow{{font-size:26px;font-weight:700;letter-spacing:.16em;text-transform:uppercase}}
.h1{{font-size:94px;font-weight:800;line-height:1.05;letter-spacing:-.042em;padding-top:.06em}}
.h2{{font-size:72px;font-weight:800;line-height:1.1;letter-spacing:-.035em;padding-top:.06em}}
.h3{{font-size:54px;font-weight:700;line-height:1.18;letter-spacing:-.027em;padding-top:.06em}}
.body{{font-size:34px;font-weight:400;line-height:1.42;letter-spacing:-.012em}}
.body strong{{font-weight:700}}
.small{{font-size:26px;font-weight:500;line-height:1.4;letter-spacing:-.005em}}
.serif{{font-family:'Lora',serif;font-style:italic;font-weight:400}}
.mark{{background:{BRAND['accent']};color:{BRAND['ink']};padding:.02em .16em;border-radius:6px;
       box-decoration-break:clone;-webkit-box-decoration-break:clone}}
.uline{{background:linear-gradient(transparent 62%, {BRAND['accent']}55 62%)}}
.spacer{{flex:1}}
.spacer.b{{flex:1.5}}
.foot{{display:flex;justify-content:space-between;align-items:center;font-size:24px;font-weight:600;letter-spacing:.02em}}
.pill{{display:inline-flex;align-items:center;gap:14px;padding:16px 30px;border-radius:999px;font-size:26px;font-weight:700;letter-spacing:-.01em}}
.num{{font-size:224px;font-weight:900;line-height:.96;letter-spacing:-.06em}}
.idx{{position:absolute;top:64px;right:78px;font-size:24px;font-weight:700;letter-spacing:.1em;opacity:.42}}
.row{{display:flex;gap:26px;align-items:flex-start}}
.bullet{{width:56px;height:56px;flex:0 0 56px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:800}}
.card{{border-radius:26px;padding:38px 40px}}
.divider{{height:2px;width:100%;opacity:.16;background:currentColor}}
"""


def page(inner, extra_css=""):
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<style>{FONTS}{BASE_CSS}{extra_css}</style></head><body>{inner}</body></html>"""


def _theme(theme):
    col = BRAND['muted_d'] if theme == "dark" else BRAND['muted_l']
    grain = "grain" if theme == "dark" else "grain on-light"
    return col, grain


def cover(eyebrow, title_html, sub_html, cta="Arraste →", idx=None):
    return page(f"""
<div class="slide violet">
  <div class="grain"></div>
  <div class="glow" style="width:760px;height:760px;background:{BRAND['accent']};opacity:.22;top:-300px;right:-260px"></div>
  <div class="glow" style="width:620px;height:620px;background:{BRAND['primary_lt']};opacity:.35;bottom:-280px;left:-220px"></div>
  <img src="{LOGO_CLARA}" style="position:relative;height:62px;width:auto;align-self:flex-start">
  <div class="eyebrow" style="color:{BRAND['accent']};position:relative;margin-top:54px">{eyebrow}</div>
  <div class="spacer"></div>
  <div class="h1" style="position:relative">{title_html}</div>
  <div class="body" style="margin-top:40px;max-width:800px;color:#E4DDFF;position:relative">{sub_html}</div>
  <div class="spacer"></div>
  <div class="foot" style="position:relative">
    <span class="pill" style="background:{BRAND['accent']};color:{BRAND['ink']}">{cta}</span>
    <span style="opacity:.72">{HANDLE}</span>
  </div>
</div>""")


def stat(idx, big, big_color, kicker, body_html, theme="dark"):
    col, grain = _theme(theme)
    return page(f"""
<div class="slide {theme}">
  <div class="{grain}"></div>
  <div class="idx">{idx}</div>
  <div class="eyebrow" style="color:{col}">{kicker}</div>
  <div class="spacer"></div>
  <div class="num" style="color:{big_color}">{big}</div>
  <div class="body" style="margin-top:52px;max-width:830px">{body_html}</div>
  <div class="spacer b"></div>
  <div class="foot" style="color:{col}">{brand_foot(theme)}<span>{idx}</span></div>
</div>""")


def text(idx, title_html, body_html, theme="dark", eyebrow=""):
    col, grain = _theme(theme)
    eb = f'<div class="eyebrow" style="color:{col}">{eyebrow}</div>' if eyebrow else ""
    return page(f"""
<div class="slide {theme}">
  <div class="{grain}"></div>
  <div class="idx">{idx}</div>
  {eb}
  <div class="spacer"></div>
  <div class="h2">{title_html}</div>
  <div class="body" style="margin-top:44px;max-width:840px;color:{col}">{body_html}</div>
  <div class="spacer b"></div>
  <div class="foot" style="color:{col}">{brand_foot(theme)}<span>{idx}</span></div>
</div>""")


def listing(idx, title_html, items, theme="dark", eyebrow="", accent=None):
    accent = accent or BRAND['accent']
    col, grain = _theme(theme)
    rows = ""
    for i, (h, s) in enumerate(items, 1):
        rows += f"""<div class="row" style="margin-top:46px">
          <div class="bullet" style="background:{accent};color:{BRAND['ink']}">{i}</div>
          <div><div style="font-size:38px;font-weight:700;letter-spacing:-.02em;line-height:1.18">{h}</div>
          <div class="small" style="color:{col};margin-top:10px;max-width:700px">{s}</div></div></div>"""
    eb = f'<div class="eyebrow" style="color:{col}">{eyebrow}</div>' if eyebrow else ""
    return page(f"""
<div class="slide {theme}">
  <div class="{grain}"></div>
  <div class="idx">{idx}</div>
  {eb}
  <div class="spacer" style="flex:.55"></div>
  <div class="h3">{title_html}</div>
  <div style="margin-top:22px">{rows}</div>
  <div class="spacer"></div>
  <div class="foot" style="color:{col}">{brand_foot(theme)}<span>{idx}</span></div>
</div>""")


def compare(idx, title_html, left_title, left_items, right_title, right_items, theme="light"):
    col, grain = _theme(theme)
    def col_html(t, items, color, sign, bg, bd):
        li = "".join(f"""<div style="display:flex;gap:16px;margin-top:24px;align-items:flex-start">
            <span style="color:{color};font-size:30px;font-weight:800;line-height:1.2">{sign}</span>
            <span style="font-size:29px;font-weight:500;line-height:1.32;letter-spacing:-.012em">{x}</span></div>""" for x in items)
        return f"""<div class="card" style="flex:1;background:{bg};border:2px solid {bd}">
          <div style="font-size:32px;font-weight:800;letter-spacing:-.02em;color:{color}">{t}</div>
          <div class="divider" style="margin-top:22px"></div>{li}</div>"""
    return page(f"""
<div class="slide {theme}">
  <div class="{grain}"></div>
  <div class="idx">{idx}</div>
  <div class="h3" style="margin-top:26px">{title_html}</div>
  <div style="display:flex;gap:26px;margin-top:52px;align-items:stretch">
    {col_html(left_title, left_items, BRAND['loss'], "✕", "#FFF0F0", "#FFD4D4")}
    {col_html(right_title, right_items, "#12A45B", "✓", "#EDFBF3", "#BEEFD4")}
  </div>
  <div class="spacer"></div>
  <div class="foot" style="color:{col}">{brand_foot(theme)}<span>{idx}</span></div>
</div>""")


def quote(idx, quote_html, attrib, theme="dark"):
    col, grain = _theme(theme)
    return page(f"""
<div class="slide {theme}">
  <div class="{grain}"></div>
  <div class="idx">{idx}</div>
  <div class="spacer"></div>
  <div style="font-size:180px;line-height:.6;color:{BRAND['accent']};font-weight:900">"</div>
  <div class="h3 serif" style="margin-top:34px;font-size:60px;line-height:1.22">{quote_html}</div>
  <div class="small" style="margin-top:40px;color:{col}">{attrib}</div>
  <div class="spacer"></div>
  <div class="foot" style="color:{col}">{brand_foot(theme)}<span>{idx}</span></div>
</div>""")


def cta(idx, title_html, body_html, button, ps=""):
    return page(f"""
<div class="slide violet">
  <div class="grain"></div>
  <div class="glow" style="width:820px;height:820px;background:{BRAND['accent']};opacity:.2;bottom:-360px;right:-300px"></div>
  <div class="idx">{idx}</div>
  <div class="spacer"></div>
  <div class="h2" style="position:relative">{title_html}</div>
  <div class="body" style="margin-top:38px;max-width:820px;color:#E7E1FF;position:relative">{body_html}</div>
  <div style="margin-top:56px;position:relative">
    <span class="pill" style="background:{BRAND['accent']};color:{BRAND['ink']};font-size:32px;padding:26px 44px">{button}</span>
  </div>
  <div class="small" style="margin-top:30px;color:#C9BEF5;position:relative">{ps}</div>
  <div class="spacer"></div>
  <div class="foot" style="position:relative;color:#fff">
    <img src="{LOGO_CLARA}" style="height:58px;width:auto">
    <span style="opacity:.75">{HANDLE}</span>
  </div>
</div>""")


def build(slides, prefix):
    from playwright.sync_api import sync_playwright
    paths = []
    with sync_playwright() as p:
        exe = os.environ.get("CHROMIUM_PATH") or next(
            (str(c) for c in [Path("/opt/pw-browsers/chromium")] if c.exists()), None)
        b = p.chromium.launch(executable_path=exe,
                              args=["--font-render-hinting=none", "--force-color-profile=srgb"])
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        for i, html in enumerate(slides, 1):
            f = OUT / f"{prefix}_{i:02d}.html"
            f.write_text(html, encoding="utf-8")
            pg.goto(f"file://{f}")
            pg.wait_for_timeout(320)
            out = OUT / f"{prefix}_{i:02d}.jpg"
            pg.screenshot(path=str(out), type="jpeg", quality=93)
            paths.append(str(out))
            f.unlink()
        b.close()
    return paths
