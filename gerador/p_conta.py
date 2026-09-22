# -*- coding: utf-8 -*-
"""Qui 24/09 · Educação · A conta do cliente que não volta (c1 refeito, visual v2)."""
from render2 import *

S = [
cover("Para quem tem comércio de bairro",
      'Seu problema não é atrair cliente.<br><span class="hl">É ele não voltar.</span>',
      'Faça esta conta com os números da sua loja. Leva 30 segundos.',
      cta="Arraste e faça a conta →",
      notif_t="Faltam 2 pro seu café grátis ☕", notif_d="Café da Esquina · +1 carimbo",
      phone_msgs=[("Ana, faz 20 dias que a gente não te vê 👀 Seu café grátis está quase lá!", "10:05")], business="Café da Esquina"),

stat("02", "R$ 0", C['loss'], "O cliente que some em silêncio",
     'É quanto rende o cliente que entrou, <b>gostou</b>… e nunca mais lembrou de você.<br><br>'
     'Ele não reclamou. Não foi pelo preço. <b>Só esqueceu.</b>'),

text("03", 'Faça a conta<br>com <span class="hl">os seus números</span>.',
     'Simulação de uma cafeteria de bairro:<br><br><b>400 clientes por mês</b><br><b>Ticket médio de R$ 32</b><br><br>'
     'E se só <b>15% deles</b> voltassem <b>uma vez a mais</b> no mês?', eyebrow="A matemática da recorrência"),

stat("04", '+R$ 23<span style="font-size:104px;margin-left:14px;letter-spacing:-.03em">mil</span>', C['gain'], "Por ano · com os mesmos clientes",
     '60 visitas extras × R$ 32 = <b>R$ 1.920 por mês</b>.<br>Mesma loja, mesma equipe, <b>zero real a mais em anúncio</b>.',
     src="Simulação ilustrativa. Refaça com os números do seu negócio."),

text("05", 'Anúncio traz desconhecido.<br><span class="hl">Fidelidade traz de volta quem já confia em você.</span>',
     'O cliente que já comprou é o mais barato que existe. Só falta um motivo — e um lembrete — para ele voltar.',
     eyebrow="A virada de chave", tsize="t3"),

whatsapp("06", 'O lembrete que o cartão de papel <span class="hl">nunca deu</span>.', "Café da Esquina",
     [("Oi, Ana! ☕ Você ganhou 1 carimbo. Faltam <b>2</b> para o seu café grátis.", "09:12"),
      ("Ana, faz 20 dias que a gente não te vê 👀 Seu café grátis está quase lá — passa aqui essa semana?", "10:05")],
     caption='Automático, no <b>WhatsApp</b> que ele já usa. Sem baixar app.', eyebrow="Exemplo"),

listing("07", 'Como funciona<br>no pontua.club',
     [("Você cria o programa em minutos", "Carimbo, ponto ou cashback — do jeito do seu negócio."),
      ("O cliente entra pelo celular", "Sem baixar aplicativo e sem cartão pra perder."),
      ("O WhatsApp faz o resto", "Avisa cada ponto, lembra quem está perto do prêmio e chama quem sumiu.")],
     eyebrow="Simples assim"),

cta("08", 'Cada compra pode ser<br><span class="hl">o início da próxima.</span>',
    'Crie seu programa de fidelidade grátis. Sem cartão de crédito, sem instalar nada.',
    ps='Salva este post pra refazer a conta com os seus números.'),
]

if __name__ == "__main__":
    for p in build(S, "p0924_conta"):
        print(p)
