# -*- coding: utf-8 -*-
"""Ter 24/11 · Ramo: posto / conveniência · post único com a arte-base em tela cheia.

A arte-base já traz o celular com a notificação de WhatsApp desenhada na cena,
por isso NÃO sobrepomos outra notif() como em p1103_lavajato.py — duas
notificações na mesma peça poluiriam a leitura.
Ver fontes/inventario.json: a contagem do cartão não bate com "faltam 2",
então a legenda não cita números.
"""
import base64, io
from render2 import *
from render2 import _page

LEGENDA = """Ele abastece toda semana. Mas sempre no seu posto? ⛽

Na pista e na conveniência, cada visita vira carimbo no celular do cliente e o WhatsApp avisa quando a recompensa está perto. Sem app e sem cartãozinho pra perder.

👉 Programa de fidelidade grátis pro seu posto: link na bio.

#posto #lojadeconveniencia #fidelizacaodeclientes #pequenosnegocios #comerciolocal"""


def scene(path, notif_html=""):
    """Arte-base em tela cheia (1080x1350) + elementos HTML por cima."""
    im = image(str(ROOT / path)); buf = io.BytesIO(); im.save(buf, "JPEG", quality=95)
    uri = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    return _page(f'<div class="s" style="padding:0;background:#000"><img src="{uri}" style="position:absolute;inset:0;width:{W}px;height:{H}px">{notif_html}</div>')

S = [
scene("fontes/ramos/posto.jpg"),
]

if __name__ == "__main__":
    for p in build(S, "p1124_posto"): print(p)
