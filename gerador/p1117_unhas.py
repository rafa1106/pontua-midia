# -*- coding: utf-8 -*-
"""Ter 17/11 · Ramo: unhas · post único com a arte-base (já traz a notificação de WhatsApp)."""
import base64, io
from render2 import *
from render2 import _page

LEGENDA = """Ela já é fiel à rotina. Falta ser fiel ao seu estúdio. 💅

Unha, esmalte, sobrancelha: cada sessão vira carimbo no celular da cliente e o WhatsApp avisa quando a próxima está perto. Sem app e sem cartãozinho pra perder.

👉 Programa de fidelidade grátis pro seu estúdio: link na bio.

#unhas #manicure #nailart #fidelizacaodeclientes #pequenosnegocios"""


def scene(path, notif_html=""):
    """Arte-base em tela cheia (1080x1350) + elementos HTML por cima."""
    im = image(str(ROOT / path)); buf = io.BytesIO(); im.save(buf, "JPEG", quality=95)
    uri = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    return _page(f'<div class="s" style="padding:0;background:#000"><img src="{uri}" style="position:absolute;inset:0;width:{W}px;height:{H}px">{notif_html}</div>')


# A arte "fontes/ramos/unhas.jpg" já traz o celular com a notificação de WhatsApp
# embutida na cena — por isso não sobrepomos outro notif() aqui.
S = [
scene("fontes/ramos/unhas.jpg"),
]

if __name__ == "__main__":
    for p in build(S, "p1117_unhas"): print(p)
