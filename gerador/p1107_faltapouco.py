# -*- coding: utf-8 -*-
"""Sáb 07/11 · Produto · Série "No automático" #3 — aviso de "falta pouco"."""
from render2 import *

BIZ = "Pet Feliz"   # negócio fictício e genérico

LEGENDA = """Falta 1 pro prêmio. Será que seu cliente sabe? 🐶

No automático #3: o pontua.club avisa no WhatsApp quando ele está perto da recompensa. Você liga uma vez e a mensagem passa a sair sozinha, pra cada cliente que chega lá.

👉 Crie o seu programa grátis: link na bio.

#programadefidelidade #petshop #fidelizacaodeclientes #pequenosnegocios #comerciolocal"""

S = [
cover("No automático · #3",
      'Falta 1 pro prêmio.<br><span class="hl">Ele precisa saber.</span>',
      'O aviso de “falta pouco” sai sozinho no WhatsApp do cliente.',
      cta="Ver como →",
      notif_t="Falta 1 pro banho grátis 🐶", notif_d=f"{BIZ} · +1 carimbo",
      phone_msgs=[("Oi, Camila! 🐶 O Thor ganhou 1 carimbo hoje. Falta só <b>1</b> pro próximo banho grátis.", "10:40")],
      business=BIZ),

text("02", 'O prêmio só puxa<br><span class="hl">quando está perto</span>.',
     'Recompensa longe demais ninguém persegue.<br><br>'
     'Quando o cliente descobre que falta <b>pouco</b>, a próxima visita deixa de ser “qualquer dia” '
     'e vira <b>esta semana</b>.', eyebrow="Por que funciona"),

text("03", 'Você liga uma vez.<br><span class="hl">Ela avisa sempre.</span>',
     'Escolha em que ponto o aviso dispara: faltando um ou dois carimbos para a recompensa.<br><br>'
     'Daí em diante, cada cliente que chega nesse ponto recebe a mensagem no <b>WhatsApp</b> — '
     'sem ninguém da equipe conferir cartão.', eyebrow="Como funciona"),

whatsapp("04", 'A mensagem que<br><span class="hl">traz ele de volta</span>.', BIZ,
     [("Oi, Camila! 🐶 O Thor ganhou 1 carimbo no banho de hoje.", "10:40"),
      ("Falta só <b>1</b> pro próximo ser por nossa conta 💜", "10:40"),
      ("Sério? Então marco pra sábado 😄", "10:52")],
     caption='Chega no WhatsApp dele.<br>Sem app, sem cartão de papel.', eyebrow="Exemplo"),

listing("05", 'O que faz<br>o aviso funcionar',
     [("Diga quanto falta", "“Falta 1” é concreto. “Volte sempre” não é."),
      ("Diga qual é o prêmio", "Ele precisa enxergar o que ganha na próxima."),
      ("Facilite o próximo passo", "Deixe claro como marcar ou onde ir.")],
     eyebrow="No texto"),

compare("06", 'Clube calado<br>× clube que avisa',
        "Calado",
        ["Não sabe onde está", "Prêmio vira promessa", "Depende da equipe", "Volta um dia desses"],
        "Que avisa",
        ["Sabe quanto falta", "Prêmio fica visível", "Roda no automático", "Volta esta semana"]),

cta("07", 'Tem cliente seu quase<br><span class="hl">fechando o cartão</span>.',
    'Ligue o aviso de “falta pouco” no seu clube. Grátis pra começar, com mensagem no WhatsApp.',
    ps='Salva pra ligar o seu.'),
]

if __name__ == "__main__":
    for p in build(S, "p1107_faltapouco"): print(p)
