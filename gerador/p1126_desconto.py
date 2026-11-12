# -*- coding: utf-8 -*-
"""Qui 26/11 · Educação · Desconto vende hoje, fidelidade vende de novo."""
from render2 import *

BIZ = "Padaria do Bairro"   # negócio fictício e genérico

LEGENDA = """Tem cliente que só volta quando tem desconto? 🤔

Os 10% você paga em toda visita, inclusive na de quem já ia comprar. O carimbo você entrega só depois que ele voltou, e cada compra vira um aviso no WhatsApp dele.

👉 Monte o seu grátis: link na bio.

#fidelizacaodeclientes #programadefidelidade #pequenosnegocios #comerciolocal #padaria"""

S = [
cover("Educação",
      'Desconto hoje.<br><span class="hl">E amanhã?</span>',
      'Por que 10% em toda compra<br>não faz ninguém voltar.',
      cta="Arraste →",
      notif_t="Faltam 2 pro seu café grátis ☕", notif_d=f"{BIZ} · +1 carimbo",
      phone_msgs=[("Oi, Marina! 🥐 Você ganhou 1 carimbo. Faltam <b>2</b> pro seu café grátis.", "08:20")], business=BIZ),

text("02", 'O desconto sai da loja<br><span class="hl">junto com o cliente</span>.',
     '“10% pra você hoje” resolve a venda de agora.<br><br>'
     'No mês seguinte ele vai pra onde tiver desconto. Ou simplesmente não vai.', eyebrow="O problema"),

compare("03", 'Desconto × programa<br>de fidelidade',
        "Desconto de 10%",
        ["Você paga em toda visita", "Vale pra quem já vinha", "Ensina a esperar oferta", "Acaba na porta da loja"],
        "Carimbo ou ponto",
        ["Só paga quando ele volta", "Premia a visita extra", "Dá motivo pra voltar", "Segue no WhatsApp dele"]),

text("04", 'A conta das<br><span class="hl">6 visitas</span>',
     'Ticket de R$ 30, só como exemplo.<br><br>'
     '<b>10% sempre:</b> desconto nas 6 visitas, inclusive nas que ele já faria.<br><br>'
     '<b>Carimbo:</b> o 6º só sai depois de 5 voltas.', eyebrow="Simulação · exemplo"),

text("05", 'Desconto não é<br><span class="hl">o inimigo</span>.',
     'Ele serve pra <b>trazer</b> gente nova.<br><br>'
     'O programa de fidelidade serve pra essa gente <b>voltar</b>.<br><br>'
     'Um abre a porta. O outro traz de novo.', eyebrow="O ajuste"),

listing("06", 'Como trocar desconto<br>por volta',
     [("Escolha o item mais pedido", "Ele já quer. E custa pouco pro seu caixa."),
      ("Deixe o prêmio perto", "Primeira recompensa entre 4 e 6 visitas."),
      ("Avise a cada compra", "Progresso que ele não vê, ele esquece.")],
     eyebrow="Na prática"),

whatsapp("07", 'O que faz ele<br><span class="hl">marcar a próxima</span>.', BIZ,
     [("Oi, Marina! 🥐 Você ganhou 1 carimbo.", "08:20"),
      ("Faltam <b>2</b> pro seu café grátis.", "08:20"),
      ("Amanhã eu passo aí 😄", "08:41")],
     caption='O cliente acompanha tudo pelo <b>WhatsApp</b>, sem baixar app.', eyebrow="Exemplo"),

cta("08", 'Desconto some.<br><span class="hl">Carimbo lembra.</span>',
    'Monte o seu programa grátis em minutos e deixe o WhatsApp avisar cada carimbo.',
    ps='Salva pra montar o seu com calma.'),
]

if __name__ == "__main__":
    for p in build(S, "p1126_desconto"): print(p)
