# -*- coding: utf-8 -*-
"""Posts montados a partir das artes prontas (pasta 02_posts/a_postar do PC)."""
import sys
from pathlib import Path
from render2 import *

SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

COMO = [
  (SRC / "Gemini_Generated_Image_yteh10yteh10yteh.png", False),   # Cartão fidelidade de papel ainda?
  (SRC / "Gemini_Generated_Image_8ek91f8ek91f8ek9.png", False),   # 1 Você cria a campanha
  (SRC / "Gemini_Generated_Image_h35xmkh35xmkh35x.png", False),   # 2 Seu cliente pontua pelo celular
  (SRC / "Gemini_Generated_Image_978c89978c89978c.png", False),   # 3 Recebe a recompensa no WhatsApp
  (SRC / "Gemini_Generated_Image_bxbie3bxbie3bxbi.png", False),   # Não vai baixar mais um app
  (SRC / "Gemini_Generated_Image_ynsd47ynsd47ynsd.png", False),   # Simples assim
]

if __name__ == "__main__":
    slides = [image(p, e) for p, e in COMO] + [
        cta("07", 'Seu programa de fidelidade<br><span class="hl">pronto em minutos</span>.',
            'Carimbo, ponto ou cashback — com aviso no WhatsApp. Grátis para começar.',
            ps='Salva pra mostrar pro seu sócio.')]
    for p in build(slides, "p0926_comofunciona"): print(p)
    for p in build([image(SRC / "business0.png")], "p0929_barbearia"): print(p)
    for p in build([image(SRC / "business5.png")], "p1006_hamburgueria"): print(p)
