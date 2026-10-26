# -*- coding: utf-8 -*-
"""Qui 05/11 · Educação · Como escolher a recompensa certa."""
from render2 import *

BIZ = "Café da Esquina"   # negócio fictício e genérico

LEGENDA = """Qual recompensa faz o cliente voltar de verdade? 🎁

Não é a mais cara: é a que ele já quer e enxerga de perto. No carrossel, 3 perguntas pra escolher a sua e exemplos por ramo. No pontua.club, o aviso de que falta pouco chega no WhatsApp do cliente.

👉 Monte o seu programa grátis: link na bio.

#fidelizacaodeclientes #programadefidelidade #pequenosnegocios #comerciolocal #cafeteria"""

S = [
cover("Antes de montar o seu",
      'Qual recompensa<br><span class="hl">faz ele voltar?</span>',
      'Não é a mais cara. É a que ele já quer<br>e enxerga de perto.',
      cta="Arraste →",
      notif_t="Falta 1 pro seu café grátis ☕", notif_d=f"{BIZ} · +1 carimbo",
      phone_msgs=[("Oi, Ana! ☕ Você ganhou 1 carimbo. Falta só <b>1</b> pro seu café grátis.", "09:12")], business=BIZ),

text("02", 'Desconto pequeno<br><span class="hl">não move ninguém</span>.',
     '“5% na próxima compra” some da cabeça antes de o cliente chegar em casa.<br><br>'
     'A recompensa precisa dar <b>vontade</b><br>e parecer <b>perto</b>.', eyebrow="O erro comum"),

listing("03", '3 perguntas antes<br>de escolher',
     [("Ele já compra isso?", "O item que ele pediria de qualquer jeito."),
      ("Custa pouco pra você?", "Valor alto pra ele, custo baixo pro seu caixa."),
      ("Dá pra chegar logo?", "Primeira recompensa entre 4 e 6 visitas.")],
     eyebrow="O teste"),

compare("04", 'Recompensa fraca<br>× recompensa forte',
        "Fraca",
        ["5% de desconto", "Brinde que ninguém usa", "Prêmio na 20ª visita", "Regra complicada"],
        "Forte",
        ["Item mais pedido grátis", "Extra que ele já quer", "Prêmio em até 6 visitas", "Regra de uma frase"]),

listing("05", 'Exemplos por ramo',
     [("Cafeteria", "O 6º café é por nossa conta."),
      ("Barbearia", "No 5º corte, a barba sai grátis."),
      ("Pet shop", "A cada 5 banhos, uma hidratação de presente."),
      ("Açaí", "No 6º copo, o adicional é por nossa conta.")],
     eyebrow="Pra copiar"),

text("06", 'Carimbo, ponto<br><span class="hl">ou cashback?</span>',
     '<b>Carimbo:</b> café, corte, banho.<br><br>'
     '<b>Ponto:</b> valores variados, cada compra soma.<br><br>'
     '<b>Cashback:</b> parte da compra vira crédito.', eyebrow="O formato"),

whatsapp("07", 'E ele precisa saber<br><span class="hl">que está perto</span>.', BIZ,
     [("Oi, Ana! ☕ Você ganhou 1 carimbo.", "09:12"),
      ("Falta só <b>1</b> pro seu café grátis!", "09:12"),
      ("Amanhã eu passo aí 😄", "09:20")],
     caption='O aviso de “falta pouco” sai sozinho no <b>WhatsApp</b>.', eyebrow="Exemplo"),

cta("08", 'Escolha a recompensa.<br><span class="hl">O pontua faz o resto.</span>',
    'Monte seu programa grátis, com aviso no WhatsApp a cada ponto.',
    ps='Salva pra escolher a sua com calma.'),
]

if __name__ == "__main__":
    for p in build(S, "p1105_recompensa"): print(p)
