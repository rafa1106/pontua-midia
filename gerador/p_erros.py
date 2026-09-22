# -*- coding: utf-8 -*-
"""Qui 08/10 · Educação · 5 erros que matam um programa de fidelidade (c3 refeito)."""
from render2 import *

def e(n): return f'<span class="am" style="font-size:40px;letter-spacing:.02em">Erro {n}</span><br>'

S = [
cover("Antes de criar o seu",
      '5 erros que matam um programa de <span class="hl">fidelidade</span>.',
      'O quarto é o mais comum — e faz o cliente desistir já no primeiro dia.', cta="Ver os 5 →",
      notif_t="Faltam 2 pro seu açaí grátis 🍧", notif_d="Açaí da Praça · +1 ponto",
      phone_msgs=[("Oi, Bia! Você ganhou 1 ponto. Faltam 2 para o seu açaí grátis 💜", "15:20")], business="Açaí da Praça"),
text("02", e(1) + 'Recompensa<br>longe demais.',
     '“Junte 20 carimbos e ganhe um café.” Ninguém enxerga o fim da linha.<br><br><b>O ajuste:</b> primeira recompensa entre <b>4 e 6 visitas</b>. Quem chega na primeira vai atrás da segunda.'),
text("03", e(2) + 'Prêmio que não<br>desperta desejo.',
     'Desconto de 5% não move ninguém.<br><br><b>O ajuste:</b> ofereça o que ele já quer — o combo, o item mais pedido, o serviço extra. Custo parecido, valor percebido muito maior.'),
text("04", e(3) + 'A equipe<br>não oferece.',
     'O programa existe, o cartaz está na parede… e o atendente não fala nada.<br><br><b>O ajuste:</b> uma frase treinada, dita em toda venda: <b>“Quer entrar no nosso clube? É pelo WhatsApp.”</b>'),
text("05", e(4) + 'Cadastro<br>cheio de fricção.',
     'Nome completo, CPF, e-mail, data de nascimento — na fila, com gente esperando.<br><br><b>O ajuste:</b> peça o mínimo. Cada campo a mais derruba a adesão.'),
text("06", e(5) + 'Criar e<br>abandonar.',
     'Fidelidade não é cartaz. É rotina — e ninguém tem tempo pra rotina.<br><br><b>O ajuste:</b> deixe o automático trabalhar. Aviso de “falta pouco”, aniversário e cliente sumido saem sozinhos no WhatsApp.'),
listing("07", 'Checklist antes<br>de lançar o seu',
     [("Primeira recompensa em até 6 visitas", "Perto o bastante pro cliente enxergar."),
      ("Prêmio que ele já compraria", "Produto, não desconto."),
      ("Uma frase treinada pra equipe", "Dita em 100% das vendas."),
      ("Cadastro rápido", "Só o essencial."),
      ("Automações ligadas", "Falta pouco, aniversário e cliente sumido.")],
     eyebrow="Salva pra usar depois"),
cta("08", 'Monte o seu sem<br>cometer <span class="hl">nenhum dos cinco</span>.',
    'O pontua.club já vem com as automações prontas. Grátis para começar.',
    ps='Manda este post pra quem tem comércio e vive dizendo que o cliente não volta.'),
]

if __name__ == "__main__":
    for p in build(S, "p1008_erros"): print(p)
