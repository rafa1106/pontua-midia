# -*- coding: utf-8 -*-
"""Sáb 05/12 · Produto · Série "No automático" — objeção: "dá trabalho pra equipe"."""
from render2 import *

BIZ = "Barbearia Nove"   # negócio fictício e genérico

LEGENDA = """“Minha equipe não vai dar conta disso.” 💬

No balcão, entrar no clube é pedir o WhatsApp e registrar a compra. O aviso de ponto, de falta pouco e de recompensa liberada sai sozinho — ninguém precisa lembrar nem digitar nada.

👉 Monte seu programa de fidelidade grátis: link na bio.

#fidelizacaodeclientes #programadefidelidade #pequenosnegocios #comerciolocal #barbearia"""

S = [
cover("No automático · objeções",
      'Isso não vai dar<br><span class="hl">trabalho pra equipe?</span>',
      'No balcão são segundos. O resto roda sozinho.',
      cta="Ver como →",
      notif_t="Recompensa liberada 🎉", notif_d=f"{BIZ} · aviso automático",
      phone_msgs=[("Oi, Diego! 💈 Sua recompensa está liberada: a próxima barba é por nossa conta.", "10:15")],
      business=BIZ),

text("02", 'O medo é real:<br><span class="hl">fila não espera.</span>',
     'Movimento cheio, equipe atendendo, cliente com pressa. Ninguém vai parar pra explicar o clube.<br><br>'
     'Se depender de alguém <b>lembrar</b>, não acontece.',
     eyebrow="O que acontece"),

listing("03", 'O que a equipe<br>faz de verdade',
     [("Pede o WhatsApp", "Uma vez só, no primeiro atendimento."),
      ("Registra a compra", "O ponto ou carimbo entra na hora."),
      ("Volta a atender", "Pronto. Acabou a parte dela.")],
     eyebrow="No balcão"),

compare("04", 'Cartão de papel<br>× pontua.club',
        "No papel",
        ["Procurar o cartãozinho", "Carimbo que borra", "Cliente esquece em casa", "Ninguém avisa nada"],
        "No pontua",
        ["Só o número do cliente", "Registro na hora", "Cartão no WhatsApp", "O aviso sai sozinho"]),

whatsapp("05", 'Essa mensagem<br><span class="hl">ninguém digitou</span>.', BIZ,
     [("Oi, Diego! 💈 Você ganhou 1 carimbo no corte de hoje.", "10:15"),
      ("Faltam <b>2</b> pra barba grátis 💜", "10:15"),
      ("Boa! Volto semana que vem 😄", "10:41")],
     caption='Sai no WhatsApp de quem autorizou receber.', eyebrow="Exemplo"),

listing("06", 'O que roda sem<br>ninguém mexer',
     [("Boas-vindas", "Quando o cliente entra no programa."),
      ("Falta pouco", "Quando ele está perto do prêmio."),
      ("Recompensa liberada", "Na hora em que ele completa."),
      ("Cliente sumido", "Quando passa tempo sem aparecer.")],
     eyebrow="No automático"),

cta("07", 'A equipe atende.<br><span class="hl">O pontua lembra.</span>',
    'Monte seu programa de fidelidade em minutos, com aviso no WhatsApp do cliente.',
    ps='Manda pra quem atende no balcão.'),
]

if __name__ == "__main__":
    for p in build(S, "p1205_equipe"): print(p)
