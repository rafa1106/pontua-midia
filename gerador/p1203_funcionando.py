# -*- coding: utf-8 -*-
"""Qui 03/12 · Educação · Como saber se o clube de fidelidade está funcionando."""
from render2 import *

BIZ = "Salão Bela Vista"   # negócio fictício e genérico

LEGENDA = """Seu clube de fidelidade está funcionando mesmo? 🤔

A resposta não está no caixa do dia: está em quantos clientes entram, voltam e chegam no prêmio. No carrossel, os 4 sinais pra olhar uma vez por mês. No pontua.club, cada carimbo e cada recompensa avisam o cliente no WhatsApp.

👉 Monte o seu grátis: link na bio.

#fidelizacaodeclientes #programadefidelidade #pequenosnegocios #comerciolocal #salaodebeleza"""

S = [
cover("Educação",
      'Seu clube está<br><span class="hl">funcionando mesmo?</span>',
      '4 sinais pra olhar uma vez por mês.<br>Nenhum deles é planilha.',
      cta="Arraste →",
      notif_t="Sua recompensa está liberada 🎁", notif_d=f"{BIZ} · resgate no balcão",
      phone_msgs=[("Oi, Carla! 💜 Sua escova de presente está liberada. Pode resgatar na próxima visita.", "10:05")],
      business=BIZ),

text("02", 'O caixa de hoje não diz<br><span class="hl">quem volta amanhã</span>.',
     'Um sábado cheio conta como foi o sábado. E só.<br><br>'
     'Fidelidade se mede na <b>volta</b>: quantos dos seus clientes vieram de novo, e com que frequência.',
     eyebrow="O engano"),

listing("03", '4 sinais pra olhar',
     [("Quantos entraram no clube", "Se quase ninguém se cadastra, o problema está no balcão, não no prêmio."),
      ("Quantos voltaram depois", "A segunda visita é o sinal mais honesto de que o clube funciona."),
      ("Quantos chegaram no prêmio", "Resgate é ciclo fechado: ele voltou as vezes combinadas e ganhou."),
      ("Quantos estão quase lá", "Quem falta pouco é o seu movimento das próximas semanas.")],
     eyebrow="O que olhar"),

compare("04", 'Sinal fraco<br>× sinal forte',
        "Fraco",
        ["Ninguém se cadastra",
         "Entra e não volta",
         "Prêmio nunca chega",
         "Só o caderno sabe"],
        "Forte",
        ["A equipe já oferece",
         "Entrou hoje, voltou",
         "Tem resgate no mês",
         "Você vê o histórico"]),

text("05", 'Olhe uma vez por mês.<br><span class="hl">Não todo dia.</span>',
     'Fidelidade se move em semanas, não em horas.<br><br>'
     'Se a recompensa é de 5 ou 6 visitas, o primeiro resgate leva semanas pra aparecer. Dar tempo faz parte do plano.',
     eyebrow="O ritmo"),

whatsapp("06", 'O sinal mais forte<br><span class="hl">chega no WhatsApp</span>.', BIZ,
     [("Oi, Carla! 💜 Você ganhou 1 carimbo hoje.", "16:40"),
      ("Falta <b>1</b> pra sua escova de presente!", "16:40"),
      ("Aaah, então eu passo aí sexta 😄", "16:52")],
     caption='Cada aviso que vira visita é o clube <b>funcionando</b>.', eyebrow="Exemplo"),

cta("07", 'Montar é rápido.<br><span class="hl">Acompanhar é simples.</span>',
    'Crie seu programa grátis e veja quem entra, quem volta e quem está perto do prêmio.',
    ps='Salva pra conferir os 4 sinais no fim do mês.'),
]

if __name__ == "__main__":
    for p in build(S, "p1203_funcionando"): print(p)
