# -*- coding: utf-8 -*-
"""Ter 27/10 · Ramo: salão de beleza · carrossel curto (a arte-base do salão tem erro de texto, ver fontes/inventario.json)."""
from render2 import *

BIZ = "Studio da Vila"   # negócio fictício e genérico

S = [
cover("Para quem tem salão",
      'Ela amou a escova.<br><span class="hl">Vai voltar quando?</span>',
      'No salão, cliente não some por preço. Some por falta de lembrete.',
      cta="Arraste →",
      notif_t="Faltam 2 pra sua escova grátis ✨", notif_d=f"{BIZ} · +1 carimbo",
      phone_msgs=[("Oi, Juliana! ✨ Você ganhou 1 carimbo hoje. Faltam <b>2</b> pra sua escova grátis.", "18:20")], business=BIZ),

text("02", 'No salão, quem volta<br>é <span class="hl">quem foi lembrada</span>.',
     'Ela saiu feliz, elogiou o resultado e disse “te vejo mês que vem”.<br><br>'
     'Passaram seis semanas. Ela não voltou — e <b>ninguém falou com ela</b>.', eyebrow="O que acontece"),

whatsapp("03", 'O lembrete sai<br><span class="hl">no WhatsApp dela</span>.', BIZ,
     [("Oi, Juliana! ✨ Você ganhou 1 carimbo na escova de hoje.", "18:20"),
      ("Faltam <b>2</b> carimbos pra sua escova grátis 💜", "18:20"),
      ("Ai, amei! Já quero marcar a próxima 😍", "18:32")],
     caption='Sem baixar app.<br>Sem cartãozinho pra perder.', eyebrow="Exemplo"),

listing("04", 'Recompensas que<br>funcionam em salão',
     [("A 5ª escova é por nossa conta", "Serviço de entrada, de alta frequência."),
      ("Hidratação de presente", "Um extra que ela já compraria — custo baixo, valor alto."),
      ("Mimo no aniversário", "Chega no WhatsApp, sem você precisar lembrar.")],
     eyebrow="Pra copiar"),

cta("05", 'Sua cliente volta<br><span class="hl">porque foi lembrada</span>.',
    'Seu programa de fidelidade em minutos,<br>com aviso no WhatsApp. Grátis pra começar.',
    ps='Manda pra quem tem salão.'),
]

if __name__ == "__main__":
    for p in build(S, "p1027_salao"): print(p)
