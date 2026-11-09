# -*- coding: utf-8 -*-
"""Sáb 21/11 · Produto · Série "No automático" #5 — carimbo surpresa."""
from render2 import *

BIZ = "Pizzaria do Bairro"   # negócio fictício e genérico

LEGENDA = """Ele não esperava ganhar nada hoje. 🎁

No automático #5: o carimbo surpresa chega no WhatsApp do cliente sem data comemorativa e sem ele pedir. Você escolhe a ação e a mensagem sai sozinha, só pra quem autorizou receber.

👉 Monte seu clube de fidelidade: link na bio.

#fidelizacaodeclientes #programadefidelidade #pizzaria #pequenosnegocios #comerciolocal"""

S = [
cover("No automático · #5",
      'Um carimbo que ele<br><span class="hl">não esperava ganhar</span>',
      'Sem data comemorativa e sem motivo. Só uma surpresa que ele lembra.',
      cta="Ver como →",
      notif_t="Carimbo surpresa pra você 🎁", notif_d=f"{BIZ} · +1 carimbo",
      phone_msgs=[("Oi, Rafa! 🎁 Hoje a casa te deu <b>1 carimbo surpresa</b>. Você ficou mais perto da próxima por nossa conta.", "19:20")],
      business=BIZ),

text("02", 'Promoção todo mundo<br><span class="hl">já espera</span>.',
     'Desconto anunciado vira preço: o cliente aprende a esperar a próxima.<br><br>'
     'O que ele não espera é ganhar algo <b>sem ter pedido</b>. É isso que vira história pra contar.',
     eyebrow="Por que funciona"),

text("03", 'Você escolhe a ação.<br><span class="hl">Ela sai sozinha.</span>',
     'Defina quem recebe o carimbo surpresa e quando: um dia parado, um grupo de clientes, uma semana inteira.<br><br>'
     'Daí em diante a mensagem chega no <b>WhatsApp</b> de quem autorizou receber, sem ninguém da equipe avisar cliente por cliente.',
     eyebrow="Como funciona"),

whatsapp("04", 'A surpresa chega<br><span class="hl">onde ele já está</span>.', BIZ,
     [("Oi, Rafa! 🎁 Hoje você ganhou <b>1 carimbo surpresa</b>, por nossa conta.", "19:20"),
      ("Ficou mais perto da sua próxima pizza 🍕", "19:20"),
      ("Opa! Não esperava essa 😄", "19:34")],
     caption='Sem app e sem cartão de papel.<br>Só pra quem autorizou receber.',
     eyebrow="Exemplo"),

listing("05", 'Quando soltar<br>a surpresa',
     [("Num dia fraco", "Terça à tarde vazia pede movimento."),
      ("Depois de um perrengue", "Demorou ou faltou item: o carimbo pede desculpa."),
      ("Em quem está quase lá", "Faltando pouco, ele vem ainda esta semana.")],
     eyebrow="Na prática"),

compare("06", 'Desconto anunciado<br>× carimbo surpresa',
        "Anunciado",
        ["Todo mundo já espera", "Mexe no seu preço", "Acaba quando acaba", "Ninguém comenta"],
        "Surpresa",
        ["Ninguém vê chegando", "Mantém o preço de pé", "Fica como lembrança", "Ele conta pra alguém"]),

cta("07", 'Surpreenda sem<br><span class="hl">baixar seu preço</span>.',
    'Monte seu clube e o carimbo surpresa chega no WhatsApp do cliente.',
    ps='Salva pra usar no próximo dia parado.'),
]

if __name__ == "__main__":
    for p in build(S, "p1121_surpresa"): print(p)
