# -*- coding: utf-8 -*-
"""CARROSSEL 2 — Comparativo (formato de alto índice de salvamento/compartilhamento)."""
from render import cover, stat, text, listing, compare, quote, cta, build
from brand import BRAND as B

S = [
cover(
  eyebrow="Comparativo honesto",
  title_html='O cartãozinho<br>de papel sai<br><span style="color:%s">mais caro</span> do que<br>você imagina.' % B['accent'],
  sub_html='Não é o custo da impressão. É o custo do que ele <strong>não</strong> te entrega.',
  cta="Comparativo completo →"),

quote("02",
  'Todo mundo perde o cartãozinho.<br>Eu já parei de dar.',
  'A frase que a gente mais escuta de dono de cafeteria, barbearia e petshop.',
  theme="dark"),

text("03",
  'O papel não<br>falhou por acaso.',
  'Ele foi projetado para uma coisa só: <strong>marcar uma visita.</strong><br><br>'
  'O problema é que fidelizar cliente exige outras três: <strong>lembrar, identificar e chamar de volta.</strong> '
  'Nenhuma delas cabe num pedaço de papel.',
  theme="light", eyebrow="A raiz do problema"),

compare("04", 'Lado a lado,<br>sem enfeite',
  "Cartão de papel",
  ["Perde, molha, amassa",
   "Você não sabe quem é o cliente",
   "Nada impede o cliente de carimbar sozinho",
   "Zero dado sobre frequência",
   "Custo recorrente de impressão",
   "Impossível avisar quem sumiu"],
  "Fidelidade digital",
  ["Fica no celular, não se perde",
   "Cada cliente tem nome e histórico",
   "Só você libera o carimbo",
   "Você vê quem volta e quem parou",
   "Sem impressão, sem reposição",
   "Dá pra chamar de volta quem sumiu"],
  theme="light"),

listing("05", 'O dado que o papel<br>nunca te deu',
  [("Quem são seus 20 melhores clientes",
    "Os que sustentam o caixa. Hoje você provavelmente só reconhece de cara."),
   ("Quem estava vindo e parou",
    "O sinal mais barato de recuperar — e o mais fácil de perder de vista."),
   ("Quanto tempo leva entre uma visita e outra",
    "É esse número que diz se o seu negócio está crescendo ou só girando.")],
  theme="dark", eyebrow="Informação vale mais que carimbo"),

text("06",
  '"Meu cliente é<br>simples, não vai<br>usar isso."',
  'Ele já usa. Pede Uber, paga por Pix, recebe boleto no WhatsApp.<br><br>'
  'O que trava não é o cliente — é <strong>pedir pra ele instalar um aplicativo.</strong> '
  'Por isso o pontua.club funciona por link: abre no navegador, sem instalar nada.',
  theme="light", eyebrow="A objeção que a gente mais escuta"),

listing("07", 'Como fica na prática',
  [("Você cria o programa", "Escolhe carimbo, ponto ou cashback e define a recompensa."),
   ("O cliente entra pelo link ou QR", "Sem baixar app. Leva menos de 30 segundos no balcão."),
   ("Você carimba pelo painel", "E passa a enxergar quem volta, quem sumiu e quanto isso vale.")],
  theme="dark", eyebrow="Três passos"),

cta("08",
  'Salva esse post<br>e testa hoje.',
  'Dá pra montar seu programa e atender o primeiro cliente no mesmo dia. Grátis para começar.',
  button="pontua.club",
  ps='Tem dúvida se serve pro seu tipo de negócio? Comenta o seu ramo aqui embaixo '
     'que eu respondo com o formato que funciona melhor.'),
]

if __name__ == "__main__":
    for p in build(S, "c2_comparativo"):
        print(p)
