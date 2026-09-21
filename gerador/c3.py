# -*- coding: utf-8 -*-
"""CARROSSEL 3 — Autoridade + checklist (conteúdo desenhado para ser enviado no direct)."""
from render import cover, stat, text, listing, compare, quote, cta, build
from brand import BRAND as B

def erro(n):
    return '<span style="font-size:40px;color:%s;letter-spacing:.02em">Erro %d</span><br>' % (B['accent'], n)

S = [
cover(
  eyebrow="Antes de criar o seu",
  title_html='5 erros que<br>matam um<br>programa de<br><span style="color:%s">fidelidade.</span>' % B['accent'],
  sub_html='O quarto é o mais comum — e é o que faz o cliente desistir na primeira semana.',
  cta="Ver os 5 →"),

text("02", erro(1) + 'Recompensa<br>longe demais.',
  '"Junte 20 carimbos e ganhe um café."<br><br>'
  'Ninguém enxerga o fim da linha. O cliente abandona antes do quinto.<br><br>'
  '<strong>O ajuste:</strong> a primeira recompensa precisa estar a 4–6 visitas. '
  'Quem chega na primeira quase sempre vai atrás da segunda.',
  theme="dark", eyebrow="O cliente desiste no meio"),

text("03", erro(2) + 'Prêmio que não<br>desperta desejo.',
  'Desconto de 5% não move ninguém. Todo mundo já viu, todo mundo já ignorou.<br><br>'
  '<strong>O ajuste:</strong> ofereça o produto que a pessoa realmente quer — o combo, '
  'o item mais pedido, o serviço extra. Custo parecido, valor percebido muito maior.',
  theme="light", eyebrow="Desconto não é recompensa"),

text("04", erro(3) + 'A equipe não<br>oferece.',
  'O programa existe, o cartaz está na parede, e o atendente não fala nada.<br><br>'
  '<strong>O ajuste:</strong> uma frase única, treinada, dita em toda venda. '
  '"Quer que eu já registre seu carimbo?" É a diferença entre 8% e 60% de adesão.',
  theme="dark", eyebrow="O furo mais silencioso"),

text("05", erro(4) + 'Fricção no<br>cadastro.',
  'Pedir nome completo, CPF, e-mail, data de nascimento e o time do coração — na fila, '
  'com gente esperando.<br><br>'
  '<strong>O ajuste:</strong> nome e WhatsApp. Só. Cada campo a mais derruba a adesão '
  'e você ainda não conquistou o direito de pedir nada.',
  theme="light", eyebrow="O erro mais comum de todos"),

text("06", erro(5) + 'Criar e<br>abandonar.',
  'Programa de fidelidade não é cartaz. É rotina.<br><br>'
  '<strong>O ajuste:</strong> 10 minutos por semana olhando quem parou de vir e mandando '
  'uma mensagem. É o que transforma o programa em faturamento de verdade.',
  theme="dark", eyebrow="Fidelidade é operação, não campanha"),

listing("07", 'Checklist antes<br>de lançar o seu',
  [("Primeira recompensa em até 6 visitas", "Curta o suficiente para o cliente enxergar o fim."),
   ("Prêmio que ele já compraria", "Não desconto — produto."),
   ("Uma frase treinada pra equipe", "Dita em 100% das vendas."),
   ("Cadastro de dois campos", "Nome e WhatsApp."),
   ("10 min/semana olhando quem sumiu", "A parte que quase ninguém faz.")],
  theme="light", eyebrow="Salva pra usar depois", accent=B['primary']),

cta("08",
  'Monta o seu<br>sem errar nenhum<br>dos cinco.',
  'O pontua.club já vem com esses ajustes no padrão. Grátis para começar, sem cartão.',
  button="pontua.club",
  ps='Manda esse post pra quem tem comércio e vive reclamando que o cliente não volta.'),
]

if __name__ == "__main__":
    for p in build(S, "c3_erros"):
        print(p)
