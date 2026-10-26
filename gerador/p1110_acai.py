# -*- coding: utf-8 -*-
"""Ter 10/11 · Ramo: açaí · post único com a arte-base em tela cheia.

A arte-base já traz a notificação de WhatsApp desenhada (“Você ganhou 1 ponto /
Faltam 2 para o próximo grátis”), por isso NÃO sobrepomos outra notif() como em
p1103_lavajato.py — duas notificações na mesma peça poluiriam a leitura.
Ver fontes/inventario.json: a contagem do cartão não bate com “faltam 2”,
então a legenda não cita números.
"""
import base64, io
from render2 import *
from render2 import _page

LEGENDA = """No açaí, o cliente é de quem lembra dele. 🍧

Cada copo vira carimbo no celular e o WhatsApp avisa quando a recompensa está perto. Sem app e sem cartãozinho pra perder — e você enxerga quem anda sumido.

👉 Programa de fidelidade grátis pra sua loja de açaí: link na bio.

#acai #acaiteria #fidelizacaodeclientes #pequenosnegocios #comerciolocal"""


def scene(path, notif_html=""):
    """Arte-base em tela cheia (1080x1350) + elementos HTML por cima."""
    im = image(str(ROOT / path)); buf = io.BytesIO(); im.save(buf, "JPEG", quality=95)
    uri = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    return _page(f'<div class="s" style="padding:0;background:#000"><img src="{uri}" style="position:absolute;inset:0;width:{W}px;height:{H}px">{notif_html}</div>')

S = [
scene("fontes/ramos/acai.jpg"),
]

if __name__ == "__main__":
    for p in build(S, "p1110_acai"): print(p)
