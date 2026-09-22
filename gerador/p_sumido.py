# -*- coding: utf-8 -*-
"""Sáb 03/10 · Produto · Série "No automático" #1 — o cliente sumido."""
from render2 import *

S = [
cover("No automático · #1",
      'Ele sumiu há 30 dias.<br><span class="hl">O pontua chamou de volta.</span>',
      'Sem você lembrar. Sem você digitar.', cta="Ver como →",
      notif_t="Sentimos sua falta 🐶", notif_d="Pet Feliz · carimbo em dobro até sexta",
      phone_msgs=[("Oi, Carla! Sentimos falta do Thor por aqui 🐶 No próximo banho, o carimbo vale em dobro — até sexta!", "09:00")], business="Pet Feliz"),
text("02", 'Cliente que some<br><span class="hl">não avisa</span>.',
     'Ele não reclama. Não se despede. Só para de vir.<br><br>E quando você percebe, <b>já faz meses</b>.', eyebrow="O problema"),
text("03", 'O pontua.club percebe <span class="hl">por você</span>.',
     'Você define a regra: <b>“quem não volta há 30 dias”</b>.<br><br>O painel mostra essas pessoas — e a mensagem pode sair sozinha ou com um clique seu.', eyebrow="Como funciona"),
whatsapp("04", 'E manda a mensagem <span class="hl">na hora certa</span>.', "Pet Feliz",
     [("Oi, Carla! Sentimos falta do Thor por aqui 🐶", "09:00"),
      ("No próximo banho, o carimbo vale em dobro — até sexta!", "09:00"),
      ("Oba! Vou marcar pra quinta 😊", "09:14")],
     caption="Automático ou com 1 clique — você escolhe.", eyebrow="Exemplo"),
listing("05", 'Ideias de mensagem<br>que trazem de volta',
     [("Carimbo em dobro", "Na próxima visita, com data limite."),
      ("Lembrete do prêmio", "“Falta só 1 pro seu grátis.”"),
      ("Um mimo simples", "Um adicional, um upgrade, um brinde.")],
     eyebrow="Pra copiar"),
text("06", 'Só para quem <span class="hl">autorizou</span>.',
     'As mensagens vão apenas para clientes que aceitaram receber.<br><br><b>É relacionamento, não spam</b> — e é por isso que funciona.', eyebrow="Do jeito certo"),
cta("07", 'Seu cliente sumido pode<br><span class="hl">voltar essa semana</span>.',
    'Crie seu programa grátis e ligue o “cliente sumido” no automático.',
    ps='Salva este post pra lembrar de ligar o seu.'),
]

if __name__ == "__main__":
    for p in build(S, "p1003_sumido"): print(p)
