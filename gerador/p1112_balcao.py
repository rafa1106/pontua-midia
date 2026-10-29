# -*- coding: utf-8 -*-
"""Qui 12/11 · Educação · A frase de balcão para a equipe oferecer o clube."""
from render2 import *

BIZ = "Barbearia Central"   # negócio fictício e genérico

LEGENDA = """Sua equipe sabe o que dizer pra oferecer o clube? 🗣️

A frase do balcão está no carrossel: uma pergunta curta, só o WhatsApp do cliente e pronto. Sem parecer venda e sem travar a fila.

👉 Monte seu programa de fidelidade grátis: link na bio.

#fidelizacaodeclientes #pequenosnegocios #barbearia #atendimentoaocliente #comerciolocal"""

S = [
cover("No balcão",
      'A frase que faz<br><span class="hl">ele entrar no clube</span>',
      'Seu clube só cresce se<br>alguém oferecer. E a equipe<br>precisa saber como.',
      cta="Arraste →",
      notif_t="Você ganhou 1 carimbo ✂️", notif_d=f"{BIZ} · bem-vindo ao clube",
      phone_msgs=[("Oi, Marcos! ✂️ Você entrou no nosso clube e já ganhou <b>1 carimbo</b> no corte de hoje.", "18:05")],
      business=BIZ),

text("02", 'O clube não se<br><span class="hl">oferece sozinho</span>.',
     'A plataforma pontua, avisa e traz o cliente de volta. Mas o cadastro começa no balcão.<br><br>'
     'E é aí que a equipe trava: ninguém quer <b>parecer vendedor</b> na hora de fechar a conta.',
     eyebrow="O gargalo"),

text("03", '“Quer entrar<br>no nosso clube?<br><span class="hl">É só o WhatsApp.”</span>',
     'Uma pergunta. Um dado. Sem explicação longa, sem folheto, sem fila parada.',
     eyebrow="A frase de balcão"),

listing("04", 'Por que essa<br>frase funciona',
     [("Pede uma coisa só", "O WhatsApp que ele já usa todo dia."),
      ("Diz o que ele ganha", "O próximo corte fica mais perto."),
      ("Não parece venda", "É um convite, não uma oferta.")],
     eyebrow="O que está por trás"),

compare("05", 'O que trava<br>× o que entra',
        "Trava",
        ["“Temos fidelidade aqui”", "Explicar tudo de uma vez", "Pedir um monte de dado", "Esperar ele perguntar"],
        "Entra",
        ["“Quer entrar no clube?”", "Uma frase e pronto", "Pedir só o WhatsApp", "Oferecer em toda conta"]),

whatsapp("06", 'Ele diz sim e<br><span class="hl">já sente o clube</span>.', BIZ,
     [("Oi, Marcos! ✂️ Você entrou no nosso clube.", "18:05"),
      ("O corte de hoje já virou <b>1 carimbo</b> 💜", "18:05"),
      ("Boa! Qual que é o prêmio? 😄", "18:11")],
     caption='A confirmação chega no <b>WhatsApp</b>.<br>Sem app, sem cartão de papel.',
     eyebrow="Logo depois"),

listing("07", 'Como treinar<br>a equipe hoje',
     [("Cole a frase no balcão", "Uma só, igual pra todo mundo."),
      ("Combine o momento", "Sempre na hora de fechar a conta."),
      ("Acompanhe quem cadastra", "Você vê os novos clientes entrando na sua base.")],
     eyebrow="Pra fazer hoje"),

cta("08", 'Uma frase no balcão.<br><span class="hl">O clube faz o resto.</span>',
    'Monte o seu grátis e o aviso de cada carimbo chega no WhatsApp do cliente.',
    ps='Salva pra treinar sua equipe.'),
]

if __name__ == "__main__":
    for p in build(S, "p1112_balcao"): print(p)
