# -*- coding: utf-8 -*-
"""Ter 03/11 · Ramo: lava-jato · post único com a arte-base + notificação de WhatsApp sobreposta."""
import base64, io
from render2 import *
from render2 import _page

def scene(path, notif_html):
    """Arte-base em tela cheia (1080x1350) + elementos HTML por cima."""
    im = image(str(ROOT / path)); buf = io.BytesIO(); im.save(buf, "JPEG", quality=95)
    uri = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    return _page(f'<div class="s" style="padding:0;background:#000"><img src="{uri}" style="position:absolute;inset:0;width:{W}px;height:{H}px">{notif_html}</div>')

S = [
scene("fontes/ramos/lavajato.jpg",
      notif("", "Você ganhou 1 carimbo 🚗", "Faltam 2 pra sua lavagem grátis",
            "left:64px;top:925px;width:560px;transform:rotate(-2deg)")),
]

if __name__ == "__main__":
    for p in build(S, "p1103_lavajato"): print(p)
