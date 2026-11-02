# -*- coding: utf-8 -*-
"""Sáb 14/11 · Produto · Série "No automático" #4 — boas-vindas automáticas."""
from render2 import *

BIZ = "Padaria Bom Dia"   # negócio fictício e genérico

LEGENDA = """Ele entrou no seu clube. E ficou no vácuo? 👋

No automático #4: assim que o cliente se cadastra, a mensagem de boas-vindas sai sozinha no WhatsApp, com o nome do seu negócio e o que ele ganha na próxima visita. Só pra quem autorizou receber.

👉 Monte seu clube de fidelidade: link na bio.

#fidelizacaodeclientes #programadefidelidade #padaria #pequenosnegocios #comerciolocal"""

S = [
cover("No automático · #4",
      'Ele entrou no clube.<br><span class="hl">E ficou no vácuo.</span>',
      'As boas-vindas saem sozinhas no WhatsApp, no minuto do cadastro.',
      cta="Ver como →",
      notif_t="Bem-vindo ao clube 💜", notif_d=f"{BIZ} · seu cartão já está ativo",
      phone_msgs=[("Bem-vindo ao clube, Marcos! Seu cartão já está ativo e você começa com 1 carimbo.", "08:12")],
      business=BIZ),

text("02", 'O primeiro minuto<br><span class="hl">é o que ele lembra</span>.',
     'O cliente deixou o WhatsApp no balcão e saiu sem saber o que acontece depois.<br><br>'
     'Se a primeira mensagem demora, o clube vira uma <b>promessa vaga</b>. Se chega na hora, '
     'ele já sai sabendo que vale a pena voltar.', eyebrow="Por que importa"),

text("03", 'Você liga uma vez.<br><span class="hl">Ela recebe sempre.</span>',
     'Escreva o recado de boas-vindas uma única vez — ou deixe a IA do pontua escrever pra você.<br><br>'
     'A partir daí, todo mundo que entra no clube recebe no <b>WhatsApp</b>, sem ninguém da equipe lembrar disso.',
     eyebrow="Como funciona"),

whatsapp("04", 'O recado que<br><span class="hl">abre o cartão</span>.', BIZ,
     [("Bem-vindo ao clube, Marcos!", "08:12"),
      ("Seu cartão já está ativo e você começa com <b>1 carimbo</b> de presente.", "08:12"),
      ("A cada visita eu te aviso por aqui quanto falta pro pão de queijo por nossa conta.", "08:12"),
      ("Boa! Já volto amanhã 😄", "08:30")],
     caption='Chega no WhatsApp dele.<br>Sem app, sem cartão de papel.', eyebrow="Exemplo"),

listing("05", 'O que uma boa<br>boas-vindas diz',
     [("Quem está falando", "O nome do seu negócio, não um número estranho."),
      ("O que ele já tem", "Um carimbo de presente dá o primeiro empurrão."),
      ("O que vem depois", "Qual é o prêmio e quantas visitas faltam."),
      ("Como sair", "Quem autorizou pode pedir pra parar quando quiser.")],
     eyebrow="No texto"),

compare("06", 'Cadastro calado<br>× boas-vindas na hora',
        "Calado",
        ["Ele esquece que entrou", "Não sabe o que ganha", "Volta sem saber do cartão", "A equipe explica tudo de novo"],
        "Com boas-vindas",
        ["Já começa engajado", "Sabe qual é o prêmio", "Guarda a conversa no WhatsApp", "Roda sozinho a cada cadastro"]),

cta("07", 'O clube começa<br><span class="hl">no primeiro oi</span>.',
    'Monte seu programa de fidelidade no pontua.club e deixe as boas-vindas saírem sozinhas no WhatsApp.',
    button='Conheça os planos · link na bio',
    ps='Salva pra montar o seu.'),
]

if __name__ == "__main__":
    for p in build(S, "p1114_boasvindas"): print(p)
