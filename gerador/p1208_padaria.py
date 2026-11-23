# -*- coding: utf-8 -*-
"""Ter 08/12 · Ramo: padaria · carrossel curto v2 (não há arte-base de padaria em fontes/inventario.json)."""
from render2 import *

BIZ = "Padaria Flor de Trigo"   # negócio fictício e genérico

LEGENDA = """Na padaria, o cliente de todo dia é o que some mais calado. 🥖

Ele vem de manhã, pega o pão na chapa, cumprimenta todo mundo. Até a rotina mudar e ninguém perceber. No pontua.club, cada compra vira carimbo e o aviso chega no WhatsApp dele.

👉 Crie o seu grátis: link na bio.

#fidelizacaodeclientes #programadefidelidade #pequenosnegocios #comerciolocal #padaria"""

S = [
cover("Para quem tem padaria",
      'Ele vinha todo dia.<br><span class="hl">E parou de vir.</span>',
      'Ele não some por preço.<br>Some porque a rotina dele mudou.',
      cta="Arraste →",
      notif_t="Faltam 2 pro seu café grátis ☕", notif_d=f"{BIZ} · +1 carimbo",
      phone_msgs=[("Bom dia, Seu Jorge! 🥖 Você ganhou 1 carimbo. Faltam <b>2</b> pro seu café grátis.", "07:05")],
      business=BIZ),

text("02", 'O freguês de manhã<br>é <span class="hl">o mais discreto</span>.',
     'Pão na chapa, café, bom dia pra todo mundo. Virou parte do balcão.<br><br>'
     'Um dia ele muda de horário, de trajeto, de trabalho — e a padaria só sente no caixa, <b>semanas depois</b>.',
     eyebrow="O que acontece"),

whatsapp("03", 'O carimbo dele<br><span class="hl">fica no WhatsApp</span>.', BIZ,
     [("Bom dia, Seu Jorge! 🥖 Você ganhou 1 carimbo hoje.", "07:05"),
      ("Faltam <b>2</b> pro seu café por nossa conta 💜", "07:05"),
      ("Amanhã eu passo aí 😄", "07:12")],
     caption='Sem baixar app.<br>Sem cartãozinho pra perder.', eyebrow="Exemplo"),

listing("04", 'Recompensas que<br>funcionam em padaria',
     [("O 6º café é por nossa conta", "Item de alta frequência e custo baixo."),
      ("Pão na chapa de presente", "O que ele já pede, sem pensar duas vezes."),
      ("Mimo no aniversário", "Chega no WhatsApp, sem ninguém precisar lembrar.")],
     eyebrow="Pra copiar"),

cta("05", 'Cliente de todo dia<br><span class="hl">merece ser lembrado</span>.',
    'Monte o programa de fidelidade da sua padaria em minutos, com aviso no WhatsApp.<br>Grátis pra começar.',
    ps='Manda pra quem tem padaria.'),
]

if __name__ == "__main__":
    for p in build(S, "p1208_padaria"): print(p)
