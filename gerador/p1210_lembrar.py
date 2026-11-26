# -*- coding: utf-8 -*-
"""Qui 10/12 · Educação · Lembrar o cliente sem virar chato."""
from render2 import *

BIZ = "Café da Esquina"   # negócio fictício e genérico

LEGENDA = """Ninguém volta por causa de mensagem chata. 📱

A diferença não está em quantas você manda: está no que elas dizem. Aviso que fala do cliente ele lê. Propaganda genérica ele silencia. No carrossel, os 3 momentos que valem uma mensagem no WhatsApp.

👉 Monte o seu clube: link na bio.

#fidelizacaodeclientes #pequenosnegocios #comerciolocal #programadefidelidade #cafeteria"""

S = [
cover("Educação",
      'Lembrar o cliente<br><span class="hl">sem virar chato</span>',
      'A diferença não está em quantas<br>mensagens você manda.',
      cta="Arraste →",
      notif_t="Falta 1 pro seu café grátis ☕", notif_d=f"{BIZ} · +1 carimbo",
      phone_msgs=[("Oi, Ana! ☕ Você ganhou 1 carimbo. Falta só <b>1</b> pro seu café grátis.", "09:12")], business=BIZ),

text("02", 'O que incomoda<br><span class="hl">não é a mensagem</span>.',
     'É a mensagem que só fala de você.<br><br>'
     '“Promoção imperdível hoje!” é propaganda.<br>'
     '“Falta 1 carimbo pro seu café” é <b>notícia boa</b> sobre ele.', eyebrow="O ponto"),

compare("03", 'Mensagem chata<br>× mensagem esperada',
        "Chata",
        ["Fala só de você", "Vai igual pra todo mundo", "Chega sem motivo", "Pede algo do cliente"],
        "Esperada",
        ["Fala do que ele já tem", "Sai pelo que ele fez", "Chega na hora certa", "Entrega algo pra ele"]),

listing("04", '3 momentos que valem<br>uma mensagem',
     [("Falta pouco pro prêmio", "Ele está perto e esqueceu. O aviso traz de volta."),
      ("Recompensa liberada", "Conquistou. Avisar é o que faz ele usar."),
      ("Aniversário", "Um benefício no dia certo é lembrado o ano todo.")],
     eyebrow="Na hora certa"),

stat("05", "88%", C['amber'], "Por que no WhatsApp",
     'dos usuários de WhatsApp no Brasil<br>abrem o app <b>todo dia</b>.<br><br>'
     'Sua mensagem não precisa de app novo: chega onde ele já está.',
     src="Fonte: Mobile Time/Opinion Box"),

whatsapp("06", 'Na prática,<br><span class="hl">é assim</span>.', BIZ,
     [("Oi, Ana! ☕ Você ganhou 1 carimbo.", "09:12"),
      ("Falta só <b>1</b> pro seu café grátis!", "09:12"),
      ("Boa, amanhã eu passo aí 😄", "09:20")],
     caption='Cada aviso sai sozinho e só para quem <b>autorizou</b> receber.', eyebrow="Exemplo"),

cta("07", 'Mensagem certa.<br><span class="hl">Na hora certa.</span>',
    'Monte seu clube em minutos e deixe os avisos do WhatsApp trabalharem enquanto você atende.',
    ps='Salva pra montar o seu com calma.'),
]

if __name__ == "__main__":
    for p in build(S, "p1210_lembrar"): print(p)
