# -*- coding: utf-8 -*-
"""Qui 19/11 · Educação · Cliente que você já tem: conquistar × manter."""
from render2 import *

BIZ = "Burger do Bairro"   # negócio fictício e genérico

LEGENDA = """Quanto você paga pra trazer um cliente novo? 💸

Agora compare com o custo de fazer voltar quem já comprou. No carrossel, a conta (simulação) e o que de fato traz ele de volta. No pontua.club, o lembrete sai no WhatsApp a cada compra.

👉 Monte seu programa grátis: link na bio.

#fidelizacaodeclientes #pequenosnegocios #comerciolocal #gestaodenegocios #hamburgueria"""

S = [
cover("Cliente que você já tem",
      'Atrair custa caro.<br><span class="hl">Manter custa pouco.</span>',
      'Faça a conta dos dois lados antes<br>de aumentar a verba de anúncio.',
      cta="Arraste →",
      notif_t="Faltam 2 pro seu lanche grátis 🍔", notif_d=f"{BIZ} · +1 carimbo",
      phone_msgs=[("Oi, Léo! 🍔 Você ganhou 1 carimbo. Faltam <b>2</b> pro seu lanche grátis.", "19:40")],
      business=BIZ),

text("02", 'A conta que<br><span class="hl">quase ninguém faz</span>.',
     'Todo mundo sabe quanto gasta pra <b>atrair</b> cliente.<br><br>'
     'Quase ninguém sabe quanto custa fazer <b>voltar</b> quem já comprou.',
     eyebrow="Ponto de partida"),

stat("03", "R$ 30", C['loss'], "Simulação · cliente novo",
     '<b>R$&nbsp;300</b> de anúncio no mês ÷ 10 clientes novos.<br><br>'
     'Dá <b>R$&nbsp;30</b> por cliente — e no mês seguinte você paga de novo.',
     src="Números de exemplo, só pra ilustrar a conta. Refaça com os seus."),

text("04", 'E quem já comprou<br><span class="hl">de você?</span>',
     'Ele já conhece a sua casa, já gostou e já deixou o WhatsApp.<br><br>'
     'Não precisa de anúncio pra voltar. Precisa de <b>lembrete</b> e de um <b>motivo</b>.',
     eyebrow="O outro lado"),

compare("05", 'Trazer um novo<br>× fazer o atual voltar',
        "Cliente novo",
        ["Paga anúncio toda vez", "Ainda não confia", "Gasta menos na 1ª vez", "Depende do anúncio"],
        "Cliente que já é seu",
        ["Já conhece e já gostou", "Volta com um aviso", "Compra mais à vontade", "Fica na sua base"]),

listing("06", 'O que faz ele voltar',
     [("Ser lembrado", "Um aviso no WhatsApp na hora certa."),
      ("Ver que falta pouco", "“Faltam 2 pro prêmio” acelera a próxima visita."),
      ("Sentir que você percebeu", "Aniversário, sumiço, carimbo surpresa.")],
     eyebrow="Na prática"),

whatsapp("07", 'O lembrete chega<br><span class="hl">onde ele já está</span>.', BIZ,
     [("Oi, Léo! 🍔 Você ganhou 1 carimbo.", "19:40"),
      ("Faltam <b>2</b> pro seu lanche grátis!", "19:40"),
      ("Boa! Sexta eu passo aí 😄", "19:52")],
     caption='A cada compra, o aviso sai no <b>WhatsApp</b> de quem autorizou receber.',
     eyebrow="Exemplo"),

cta("08", 'Cuide de quem<br><span class="hl">já entrou na sua loja.</span>',
    'Monte seu programa grátis e deixe o lembrete sair no WhatsApp a cada compra.',
    ps='Salva pra refazer a conta com os números da sua loja.'),
]

if __name__ == "__main__":
    for p in build(S, "p1119_custocliente"): print(p)
