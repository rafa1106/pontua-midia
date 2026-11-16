# -*- coding: utf-8 -*-
"""Sáb 28/11 · Produto · Série "No automático" #6 — a IA monta a campanha e escreve a mensagem."""
from render2 import *

BIZ = "Pizzaria da Praça"   # negócio fictício e genérico

LEGENDA = """Trava na hora de escrever a mensagem pro cliente? 🤖

No automático #6: você diz o que quer (trazer quem sumiu, avisar que falta pouco) e a IA do pontua monta a campanha e escreve o texto. Você lê, ajusta e o aviso sai no WhatsApp de quem autorizou.

👉 Monte seu clube de fidelidade: link na bio.

#fidelizacaodeclientes #programadefidelidade #pequenosnegocios #comerciolocal #pizzaria"""

S = [
cover("No automático · #6",
      'Você sabe atender.<br><span class="hl">Escrever é que trava.</span>',
      'A IA do pontua monta a campanha e escreve a mensagem. Você só revisa.',
      cta="Ver como →",
      notif_t="Sua campanha está pronta ✨", notif_d=f"{BIZ} · texto sugerido pela IA",
      phone_msgs=[("Saudade de você! 🍕 Seu cartão continua guardado aqui e falta pouco pro prêmio.", "18:40")],
      business=BIZ),

text("02", 'O programa no ar.<br><span class="hl">E a folha em branco.</span>',
     'Você montou o clube, o cliente se cadastrou — e aí vem a parte que ninguém gosta: '
     'escrever o que mandar, pra quem e quando.<br><br>'
     'É aí que a campanha fica <b>pra semana que vem</b>. E depois pro mês que vem.',
     eyebrow="O que acontece"),

text("03", 'Você diz o objetivo.<br><span class="hl">Ela escreve o resto.</span>',
     '“Quero trazer de volta quem não aparece há um mês.”<br><br>'
     'A IA do pontua monta a campanha a partir disso e já entrega o texto pronto, '
     'no tom do seu negócio, pra sair no <b>WhatsApp</b>.',
     eyebrow="Como funciona"),

whatsapp("04", 'O texto que ela<br><span class="hl">entrega pronto</span>.', BIZ,
     [("Oi, Camila! 🍕 Faz um tempo que a gente não te vê.", "18:40"),
      ("Seu cartão continua guardado e <b>falta pouco</b> pro seu prêmio.", "18:40"),
      ("Te espero essa semana 💜", "18:40"),
      ("Opa! Sexta eu apareço 😄", "19:05")],
     caption='Sai no WhatsApp de quem autorizou receber.', eyebrow="Exemplo"),

listing("05", 'O que você confere<br>antes de aprovar',
     [("O tom", "Se fala como você fala no balcão."),
      ("O nome certo", "Do seu negócio e do prêmio que ele ganha."),
      ("Quem recebe", "Só a lista de quem autorizou o contato."),
      ("A hora", "O horário em que seu cliente costuma comprar.")],
     eyebrow="Fica com você"),

compare("06", 'No improviso<br>× com a IA',
        "No improviso",
        ["Fica pra depois", "Texto diferente toda vez", "Cada um faz do seu jeito", "Preguiça de recomeçar"],
        "Com a IA do pontua",
        ["Sai no mesmo dia", "Começo, meio e fim", "Um padrão pro negócio", "Você só lê e ajusta"]),

cta("07", 'Não precisa entender<br><span class="hl">de marketing.</span>',
    'Monte seu programa de fidelidade no pontua.club e deixe a IA escrever a mensagem que vai no WhatsApp.',
    button='Crie o seu grátis · link na bio',
    ps='Salva pra montar a sua primeira campanha.'),
]

if __name__ == "__main__":
    for p in build(S, "p1128_ia"): print(p)
