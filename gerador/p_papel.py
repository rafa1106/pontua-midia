# -*- coding: utf-8 -*-
"""Qui 01/10 · Educação/Objeção · Cartão de papel × fidelidade no WhatsApp (c2 refeito)."""
from render2 import *

S = [
cover("Comparativo honesto",
      'O cartãozinho de papel sai <span class="hl">mais caro</span> do que você imagina.',
      'Não pelo custo da impressão. Pelo que ele não faz.', cta="Ver o comparativo →",
      notif_t="Falta 1 corte pro seu grátis 💈", notif_d="Barbearia do Léo · +1 carimbo",
      phone_msgs=[("Feliz aniversário, Rafa! 🎉 Seu presente: 1 carimbo extra no próximo corte.", "08:30")], business="Barbearia do Léo"),

text("02", '“Todo mundo perde<br>o cartãozinho.”',
     'Se você já ouviu — ou já disse — isso, o problema nunca foi a ideia de fidelizar.<br><br><b>Foi o papel.</b>',
     eyebrow="A frase que todo dono de balcão conhece"),

text("03", 'O papel só faz <span class="hl">uma coisa</span>: marcar a visita.',
     'Fidelizar exige outras três: <b>lembrar</b> o cliente, <b>saber quem ele é</b> e <b>chamar de volta</b> quando ele some.<br><br>Nenhuma delas cabe num pedaço de papel.',
     eyebrow="A raiz do problema"),

compare("04", 'Lado a lado,<br>sem enfeite',
     "Cartão de papel", ["Perde, molha, amassa", "Você não sabe quem é o cliente", "Ninguém avisa que falta pouco",
                          "Impossível chamar quem sumiu", "Reimpressão sem fim"],
     "pontua.club", ["Fica no celular, sem app", "Cada cliente com nome e histórico", "Aviso no WhatsApp a cada ponto",
                     "Mensagem pra quem sumiu", "Bônus de aniversário no automático"]),

whatsapp("05", 'Enquanto isso, no WhatsApp <span class="hl">do seu cliente</span>:', "Barbearia do Léo",
     [("Bem-vindo ao clube! A cada 5 cortes, o 6º é por nossa conta 💈", "18:02"),
      ("Você ganhou 1 carimbo. Falta só <b>1</b> pro seu corte grátis 🎉", "18:40"),
      ("Seu corte grátis está liberado! É só mostrar esta mensagem.", "10:15")],
     caption="Tudo automático. Você só atende.", eyebrow="Exemplo"),

text("06", '“Meu cliente é simples,<br>não vai usar isso.”',
     'Ele já paga no Pix e conversa no WhatsApp todo dia.<br><br>O que trava é pedir pra ele <b>instalar um app</b>. No pontua.club ele não instala nada.',
     eyebrow="A objeção mais comum"),

stat("07", "88%", C['lilac'], "Abrem o WhatsApp todo dia",
     'É lá que o seu cliente já está. <b>É lá que o pontua.club fala com ele.</b>',
     src="Fonte: Panorama Mobile Time/Opinion Box — Mensageria no Brasil (2022)."),

cta("08", 'Troque o papel por<br>um <span class="hl">clube no WhatsApp</span>.',
    'Monte o seu em minutos. Grátis para começar, sem cartão de crédito.',
    ps='Manda este post pra quem ainda usa cartãozinho de papel.'),
]

if __name__ == "__main__":
    for p in build(S, "p1001_papel"): print(p)
