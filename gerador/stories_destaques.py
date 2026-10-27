# -*- coding: utf-8 -*-
"""Stories (1080x1920) e capas dos destaques do perfil @pontua.club.

Saída: ../destaques/<destaque>/NN.jpg e ../destaques/capas/<destaque>.jpg
Áreas seguras: nada importante acima de y=250 (barra do story) nem abaixo de y=1640 (campo de resposta).
O último story de cada destaque deixa espaço livre (≈ y 1180–1420) para o adesivo de link.
"""
import base64, io, os
from pathlib import Path
import render2 as R
from render2 import C, phone_chat, notif, LOGO_CLARA, SIMBOLO, HANDLE, ROOT, image

SH = 1920
CSS = R.CSS.replace(f"height:{R.H}px", f"height:{SH}px")
OUT = ROOT / "destaques"

def page(inner):
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{R.FONTS}{R.EMOJI_CSS}{CSS}'
            f'.story{{padding:260px 84px 0}} .mark{{position:absolute;left:0;right:0;bottom:300px;display:flex;justify-content:center;'
            f'align-items:center;gap:14px;font-size:26px;font-weight:600;color:{C["muted"]};z-index:3}}</style>'
            f'</head><body>{R._emoji(inner)}</body></html>')

def mark():
    return f'<div class="mark"><img src="{SIMBOLO}" style="height:46px;width:46px">{HANDLE}</div>'

def st_text(eyebrow, title, body, hero=False, tsize="t2"):
    eb = f'<div class="eb z" style="color:{C["amber"] if hero else C["lilac"]}">{eyebrow}</div>' if eyebrow else ""
    return page(f"""<div class="s story {'hero' if hero else ''}">{R._bg(hero)}
  <div style="flex:1"></div>{eb}
  <div class="{tsize} z" style="margin-top:28px">{title}</div>
  <div class="bd z" style="margin-top:40px;font-size:38px">{body}</div>
  <div style="flex:1.3"></div>{mark()}</div>""")

def st_phone(eyebrow, title, business, msgs, caption=""):
    cap = f'<div class="bd z" style="margin-top:22px;font-size:34px">{caption}</div>' if caption else ""
    return page(f"""<div class="s story">{R._bg()}
  <div class="eb z">{eyebrow}</div>
  <div class="t2 z" style="margin-top:22px">{title}</div>{cap}
  {phone_chat(business, msgs, "left:305px;top:700px;height:720px;transform-origin:top center;transform:rotate(3deg) scale(1.22)")}
  {mark()}</div>""")

def st_scene(label, art_path, line):
    im = image(str(art_path)); buf = io.BytesIO(); im.save(buf, "JPEG", quality=92)
    uri = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    return page(f"""<div class="s story">{R._bg()}
  <div class="eb z" style="color:{C['amber']}">{label}</div>
  <div class="t3 z" style="margin-top:20px;font-size:52px">{line}</div>
  <img class="z" src="{uri}" style="margin-top:44px;width:912px;height:1140px;border-radius:36px;
       box-shadow:0 0 0 2px rgba(183,156,255,.35),0 30px 90px rgba(0,0,0,.55)">
  {mark()}</div>""")

def st_cta(title, body):
    return page(f"""<div class="s story hero">{R._bg(True)}
  <img class="z" src="{LOGO_CLARA}" style="height:64px;align-self:flex-start;margin-top:40px">
  <div class="t2 z" style="margin-top:150px">{title}</div>
  <div class="bd z" style="margin-top:36px;font-size:38px">{body}</div>
  <div class="z" style="margin-top:430px;text-align:center;font-size:34px;font-weight:800;color:{C['amber']}">Toque no link 👇</div>
  {mark()}</div>""")

def capa(emoji):
    return page(f"""<div class="s" style="height:{SH}px;padding:0;align-items:center;justify-content:center;
  background:radial-gradient(60% 40% at 50% 50%, #5B34E8 0%, #2A1470 55%, #0B0816 100%)">
  <div style="width:560px;height:560px;border-radius:50%;display:flex;align-items:center;justify-content:center;
       background:rgba(255,255,255,.06);box-shadow:inset 0 0 0 3px rgba(183,156,255,.45)">
    <span style="font-size:250px;line-height:1">{emoji}</span></div></div>""")

CTA_BODY = 'Grátis pra começar, sem cartão de crédito.<br>Aviso no <b>WhatsApp</b> a cada ponto.'

DESTAQUES = {
"1_como_usar": ("✨", [
    st_text("Como funciona", 'Cartão fidelidade de papel?<br><span class="hl">Ficou pra trás.</span>',
            'Veja em 3 passos como o pontua.club funciona.', hero=True),
    st_text("Passo 1", 'Você cria o programa<br><span class="hl">em minutos</span>.',
            'Carimbo, ponto ou cashback — do jeito do seu negócio.'),
    st_text("Passo 2", 'O cliente entra<br><span class="hl">pelo celular</span>.',
            'Sem baixar aplicativo.<br>Sem cartão pra perder.'),
    st_phone("Passo 3", 'E o <span class="hl">WhatsApp</span> avisa.', "Café da Esquina",
             [("Oi, Ana! ☕ Você ganhou 1 carimbo.", "09:12"), ("Falta só <b>1</b> pro seu café grátis!", "09:12")]),
    st_cta('Crie o seu<br><span class="hl">programa grátis</span>.', CTA_BODY),
]),
"2_seu_ramo": ("🛍️", [
    st_text("Para o seu negócio", 'Funciona pra quem vive de<br><span class="hl">cliente que volta</span>.',
            'Alimentação, beleza, pet e serviços.', hero=True),
    st_scene("Barbearia", ROOT / "artes/p0929_barbearia_01.jpg", "Cada corte vira carimbo."),
    st_scene("Hamburgueria", ROOT / "artes/p1006_hamburgueria_01.jpg", "Cada pedido vira ponto."),
    st_scene("Pet shop", ROOT / "fontes/ramos/petshop.jpg", "Cada banho conta."),
    st_scene("Açaí", ROOT / "fontes/ramos/acai.jpg", "Cada copo aproxima o prêmio."),
    st_scene("Lava-jato", ROOT / "artes/p1103_lavajato_01.jpg", "Cada lavagem vira carimbo."),
    st_scene("Unhas e estética", ROOT / "fontes/ramos/unhas.jpg", "A rotina dela, no seu clube."),
    st_cta('E no seu ramo,<br><span class="hl">também funciona</span>.', CTA_BODY),
]),
"3_automatico": ("⚡", [
    st_text("No automático", 'Seu clube trabalha<br><span class="hl">enquanto você atende</span>.',
            '4 mensagens que saem sozinhas no <b>WhatsApp</b> — só para quem autorizou receber.', hero=True),
    st_phone("Boas-vindas", 'Quem entra no clube<br><span class="hl">é bem recebido</span>.', "Açaí da Praça",
             [("Oi, Bia! 💜 Bem-vinda ao clube do Açaí da Praça. A cada visita, 1 ponto.", "15:20")]),
    st_phone("Falta pouco", 'Quem está perto<br><span class="hl">fica sabendo</span>.', "Pet Feliz",
             [("Oi, Camila! 🐶 Falta só <b>1</b> pro próximo banho grátis do Thor.", "10:40")]),
    st_phone("Aniversário", 'No dia certo,<br><span class="hl">um parabéns</span>.', "Padaria do Bairro",
             [("Feliz aniversário, Letícia! 🎂 Hoje o cafezinho é por nossa conta.", "08:30")]),
    st_phone("Cliente sumido", 'Quem sumiu<br><span class="hl">é chamado de volta</span>.', "Pet Feliz",
             [("Oi, Carla! Sentimos falta do Thor 🐶 No próximo banho, o carimbo vale em dobro.", "09:00")]),
    st_cta('Liga uma vez.<br><span class="hl">Funciona sempre.</span>', CTA_BODY),
]),
"4_duvidas": ("💬", [
    st_text("Dúvidas", 'O que todo dono<br>de negócio<br><span class="hl">pergunta antes</span>.', 'Toque para ver as respostas.', hero=True),
    st_text("Pergunta", 'Meu cliente precisa<br><span class="hl">baixar app?</span>',
            '<b>Não.</b> Ele entra pelo celular e recebe tudo no WhatsApp que já usa.', tsize="t3"),
    st_text("Pergunta", 'Tem custo<br><span class="hl">pra começar?</span>',
            'Tem <b>plano grátis</b> pra começar, sem cartão de crédito.', tsize="t3"),
    st_text("Pergunta", 'Vou mandar spam<br><span class="hl">pros meus clientes?</span>',
            '<b>Não.</b> As mensagens vão só para quem aceitou receber. É relacionamento, não disparo.', tsize="t3"),
    st_text("Pergunta", 'Não entendo de marketing.<br><span class="hl">Consigo usar?</span>',
            '<b>Consegue.</b> A IA do pontua ajuda a montar a campanha e a escrever as mensagens.', tsize="t3"),
    st_text("Pergunta", 'Serve pro meu<br><span class="hl">tipo de negócio?</span>',
            'Se você vive de cliente que volta — café, salão, barbearia, pet, açaí — <b>serve</b>.', tsize="t3"),
    st_cta('Ficou alguma dúvida?<br><span class="hl">Teste grátis.</span>', CTA_BODY),
]),
}

def build_all():
    from playwright.sync_api import sync_playwright
    exe = os.environ.get("CHROMIUM_PATH") or next((str(c) for c in [Path("/opt/pw-browsers/chromium")] if c.exists()), None)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe, args=["--font-render-hinting=none", "--force-color-profile=srgb"])
        pg = b.new_page(viewport={"width": 1080, "height": SH}, device_scale_factor=1)
        def shot(html, out):
            out.parent.mkdir(parents=True, exist_ok=True)
            f = out.with_suffix(".html"); f.write_text(html, encoding="utf-8")
            pg.goto(f"file://{f}"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(500)
            pg.screenshot(path=str(out), type="jpeg", quality=92); f.unlink(); print(out)
        for nome, (emo, stories) in DESTAQUES.items():
            for i, s in enumerate(stories, 1):
                shot(s, OUT / nome / f"{i:02d}.jpg")
            shot(capa(emo), OUT / "capas" / f"{nome}.jpg")
        b.close()

if __name__ == "__main__":
    build_all()
