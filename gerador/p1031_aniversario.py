# -*- coding: utf-8 -*-
"""Sáb 31/10 · Produto · Série "No automático" #2 — bônus de aniversário."""
from render2 import *

BIZ = "Padaria do Bairro"   # negócio fictício e genérico

S = [
cover("No automático · #2",
      'É aniversário dela.<br><span class="hl">O pontua já lembrou.</span>',
      'Você não anota nada. A mensagem sai sozinha.', cta="Ver como →",
      notif_t="Feliz aniversário, Letícia! 🎂", notif_d=f"{BIZ} · mimo liberado",
      phone_msgs=[("Feliz aniversário, Letícia! 🎂 Hoje o seu cafezinho é por nossa conta.", "08:30")], business=BIZ),

text("02", 'Ninguém esquece<br><span class="hl">de ser lembrado</span>.',
     'Aniversário é um dos poucos dias em que o cliente <b>gosta</b> de receber mensagem de uma loja.<br><br>'
     'Um parabéns com um mimo vira visita — e vira lembrança boa do seu negócio.', eyebrow="Por que funciona"),

text("03", 'Você liga a automação<br><span class="hl">uma vez</span>.',
     'Quando o cliente informa a data de aniversário no clube, ela fica salva.<br><br>'
     'Todo ano, no dia certo, a mensagem sai no <b>WhatsApp</b> — sem ninguém da equipe precisar lembrar.', eyebrow="Como funciona"),

whatsapp("04", 'No dia, ela<br><span class="hl">sai sozinha</span>.', BIZ,
     [("Feliz aniversário, Letícia! 🎂", "08:30"),
      ("Hoje o seu cafezinho é por nossa conta — vale até domingo ☕", "08:30"),
      ("Que fofos! Passo aí hoje 😍", "08:41")],
     caption='Com um benefício de verdade e <b>prazo pra usar</b>.', eyebrow="Exemplo"),

listing("05", 'Mimos de aniversário<br>que trazem o cliente',
     [("Um item por nossa conta", "Café, sobremesa ou adicional — custo baixo."),
      ("Pontos em dobro na semana", "Premia a visita sem precisar dar desconto."),
      ("Benefício com prazo", "“Vale até domingo” é o que faz a pessoa sair de casa.")],
     eyebrow="Pra copiar"),

text("06", 'Só quem <span class="hl">autorizou</span> recebe.',
     'A mensagem vai apenas para clientes que aceitaram receber contato.<br><br>'
     'Por isso ela chega como <b>carinho</b> — e não como spam.', eyebrow="Do jeito certo"),

cta("07", 'Este mês tem aniversário<br><span class="hl">na sua base</span>.',
    'Ligue a automação de aniversário no seu clube. Grátis para começar, com aviso no WhatsApp.',
    ps='Salva pra ligar a sua.'),
]

if __name__ == "__main__":
    for p in build(S, "p1031_aniversario"): print(p)
