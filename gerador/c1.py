# -*- coding: utf-8 -*-
"""CARROSSEL 1 — Aversão à perda + aritmética do próprio negócio do leitor."""
from render import cover, stat, text, listing, cta, build
from brand import BRAND as B

S = [
cover(
  eyebrow="Para quem tem comércio de bairro",
  title_html='Seu problema<br>não é atrair<br>cliente.<br><span style="color:%s">É ele não voltar.</span>' % B['accent'],
  sub_html='A conta que quase ninguém faz — e que decide se o seu mês fecha no azul.',
  cta="Arraste e faça a conta →"),

stat("02", "R$ 0", B['loss'], "O custo invisível",
  'É quanto você fatura com o cliente que entrou uma vez, <strong>gostou</strong>, '
  'e simplesmente nunca mais lembrou de você.<br><br>'
  'Ele não reclamou. Não foi pro concorrente por preço. Só esqueceu.',
  theme="dark"),

text("03",
  'Faça a conta<br>com <span class="uline">os seus números</span>.',
  'Exemplo real de uma cafeteria de bairro:<br><br>'
  '<strong>400 clientes por mês</strong><br>'
  '<strong>Ticket médio de R$ 32</strong><br><br>'
  'Se apenas <strong>15% deles</strong> voltarem <strong>uma vez a mais</strong> no mês...',
  theme="light", eyebrow="A matemática da recorrência"),

stat("04", "+R$ 23<span style=\"font-size:110px\">mil</span>", B['gain'], "No ano, sem gastar R$1 a mais em anúncio",
  '60 visitas extras por mês × R$ 32 = <strong>R$ 1.920/mês</strong>.<br><br>'
  'Mesma loja. Mesma equipe. Mesmas pessoas. '
  'Só que agora elas têm <strong>um motivo para voltar.</strong>',
  theme="dark"),

text("05",
  'Você não precisa<br>de mais gente<br>entrando.',
  'Precisa das <strong>mesmas pessoas</strong> entrando mais vezes.<br><br>'
  'Anúncio traz desconhecido. Fidelidade traz de volta quem já provou, '
  'já gostou e já confia em você. É o cliente mais barato que existe.',
  theme="light", eyebrow="A virada de chave"),

listing("06", 'Então por que o<br>cartãozinho de papel<br>não resolve?',
  [("Ele mora na carteira — e a carteira esquece",
    "Amassa, molha, some. E o cliente não vai voltar só pra pedir outro."),
   ("Você não sabe quem é quem",
    "Não tem nome, não tem histórico, não tem como saber quem sumiu há 40 dias."),
   ("Você nunca consegue chamar de volta",
    "Sem contato, sem lembrete. Você só espera e torce.")],
  theme="dark", eyebrow="O problema não é a ideia — é o suporte"),

listing("07", 'O que muda quando<br>a fidelidade é digital',
  [("O cartão fica no celular do cliente",
    "Sem instalar aplicativo nenhum. Ele abre o link e pronto."),
   ("Você enxerga quem está sumindo",
    "E consegue chamar de volta antes de perder de vez."),
   ("Carimbo, ponto ou cashback — você escolhe",
    "O modelo que faz sentido pro seu tipo de negócio.")],
  theme="light", eyebrow="A mesma ideia, sem os furos", accent=B['primary']),

cta("08",
  'Monta o seu em<br>menos de 10 minutos.',
  'Grátis para começar. Sem cartão de crédito, sem instalação, sem contrato.',
  button="pontua.club",
  ps='Ou comenta <strong>FIDELIDADE</strong> aqui embaixo que eu te mando no direct '
     'a planilha da conta acima, com os seus números.'),
]

if __name__ == "__main__":
    for p in build(S, "c1_recorrencia"):
        print(p)
