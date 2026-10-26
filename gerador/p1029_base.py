# -*- coding: utf-8 -*-
"""Qui 29/10 · Educação · Série "Cliente que você já tem": base própria × depender de anúncio/delivery."""
from render2 import *

BIZ = "Restaurante da Praça"   # negócio fictício e genérico

S = [
cover("Cliente que você já tem",
      'O cliente é seu<br><span class="hl">ou do aplicativo?</span>',
      'Quem tem o contato do cliente vende de novo sem pagar outra vez.',
      cta="Arraste →",
      notif_t="Sua recompensa está liberada 🎉", notif_d=f"{BIZ} · 10º pedido",
      phone_msgs=[("Oi, Marcos! Seu 10º pedido liberou a sobremesa por nossa conta 🎉", "19:42")], business=BIZ),

text("02", 'Você vende todo dia<br>e <span class="hl">não sabe pra quem</span>.',
     'O app de delivery sabe.<br>A rede social sabe. O anúncio sabe.<br><br>'
     'Você paga a taxa — e fica <b>sem o contato</b><br>de quem comprou.', eyebrow="O problema"),

compare("03", 'Quem é o dono<br>do seu cliente?',
        "Audiência alugada",
        ["Pagar de novo pra falar com o mesmo cliente", "O alcance muda quando a plataforma muda",
         "Você não tem o contato de quem comprou", "Promoção vira a única forma de vender"],
        "A sua base",
        ["Falar direto com quem já comprou de você", "Um canal que é seu, não da plataforma",
         "Histórico de cada cliente no seu painel", "Vender sem precisar derrubar o preço"]),

stat("04", "88%", C['lilac'], "Uso diário do WhatsApp no Brasil",
     'dos usuários abrem o WhatsApp <b>todo dia</b> — e o app está em <b>99%</b> dos smartphones do país.<br><br>'
     'É onde o seu recado <b>é visto</b>.',
     src="Fonte: Mobile Time/Opinion Box — Mensageria no Brasil (ago/2022)."),

text("05", 'A base se constrói<br><span class="hl">uma compra por vez</span>.',
     'O cliente entra no clube pelo celular,<br>em segundos, ali no balcão.<br><br>'
     'A cada visita o histórico fica mais completo — <b>sem papelada e sem app</b>.', eyebrow="Como se faz"),

whatsapp("06", 'Falar com ele<br><span class="hl">fica simples</span>.', BIZ,
     [("Oi, Marcos! Seu 10º pedido liberou a sobremesa por nossa conta 🎉", "19:42"),
      ("Pode pedir direto com a gente que já vai na conta 😉", "19:43"),
      ("Boa! Peço hoje mesmo", "19:55")],
     caption='Só para quem autorizou receber. <b>É relacionamento, não disparo.</b>', eyebrow="Exemplo"),

listing("07", 'O que você passa<br>a saber e a fazer',
     [("Quem são seus melhores clientes", "Quem volta e com que frequência."),
      ("Quem está sumindo", "E dá pra chamar de volta antes de perder de vez."),
      ("Quando falar", "Aniversário, prêmio e falta pouco: no automático.")],
     eyebrow="Com a base na mão"),

cta("08", 'Pare de alugar<br><span class="hl">o seu próprio cliente</span>.',
    'Crie seu clube de fidelidade grátis e comece a montar a base que é sua — com aviso no WhatsApp.',
    ps='Salva pra montar o seu.'),
]

if __name__ == "__main__":
    for p in build(S, "p1029_base"): print(p)
