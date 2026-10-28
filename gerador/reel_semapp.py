# -*- coding: utf-8 -*-
"""Reel 03 — "Sem aplicativo" (fluxo 02 do material bruto: cliente entra no clube pelo celular).

Uso: python3 reel_semapp.py <pasta> [preview t1,t2,...]
  <pasta>/fc/NNNN.jpg  quadros do cliente.mp4 (30 fps, 620 px de largura)
  <pasta>/audio/narracao.mp3 + marcas.json
"""
import json, random, sys
from reel_base import *

PW = 600
SH = round((PW - 32) * 2532 / 1170)
PH = SH + 32
PT = 470


def qr_falso(n=21, seed=7):
    """Padrão decorativo com cara de QR Code (não codifica nada — ninguém escaneia um link de demonstração)."""
    random.seed(seed)
    cells = []
    for y in range(n):
        for x in range(n):
            on = None
            for x0, y0 in ((0, 0), (n - 7, 0), (0, n - 7)):
                if x0 <= x < x0 + 7 and y0 <= y < y0 + 7:
                    rx, ry = x - x0, y - y0
                    on = rx in (0, 6) or ry in (0, 6) or (2 <= rx <= 4 and 2 <= ry <= 4)
            if on is None:
                on = random.random() < .48
            if on:
                cells.append(f'<i style="left:{x / n * 100:.3f}%;top:{y / n * 100:.3f}%"></i>')
    return "".join(cells)


def build(work):
    S, U, total = marcas(work)
    fc = (work / "fc").as_uri()
    nfc = len(list((work / "fc").glob("*.jpg")))
    optin = ("Olá, Larissa Mendes.<br><br>Café da Esquina te convidou para participar do programa de fidelidade "
             "e acompanhar seu cartão de fidelidade pelo WhatsApp.<br><br>Deseja receber atualizações por aqui?")
    body = f"""{BG}{TOP}
<div class="cap" id="hook">
  <div class="l q" id="h1">“Meu cliente não vai<br>baixar aplicativo.”</div>
  <div class="l" id="h2" style="margin-top:40px"><span class="am">Nem precisa.</span></div>
</div>

<div class="cap step" id="c2"><span class="n">1</span><div>Aponta a câmera<br><span class="hl">pro QR do balcão</span></div></div>
<div class="cap step" id="c3"><span class="n">2</span><div>Nome e WhatsApp<br><span class="hl">e pronto</span></div></div>
<div class="cap step" id="c4"><span class="n wa">{WA_ICON}</span><div>Confirma<br><span class="hl">no WhatsApp</span></div></div>
<div class="cap step" id="c5"><span class="n">✓</span><div>Cartão num link<br><span class="hl">sempre à mão</span></div></div>

<div id="phone"><div class="scr">
  <img id="sv" src="{fc}/0001.jpg">
  <div id="cam"><div class="lbl">Câmera</div>
    <div id="stand"><div class="st1">Café da Esquina</div><div class="st2">Entre no clube de fidelidade</div>
      <div class="qr">{qr_falso()}</div><div class="st3">aponte a câmera</div></div>
    <div id="frame"><b class="a"></b><b class="b"></b><b class="c"></b><b class="d"></b><div id="scan"></div></div>
    <div id="pill">🔗 Abrir link do clube</div>
  </div>
  <div id="flash"></div>
</div><div id="ring"></div></div>

<div class="badge" id="ok" style="right:36px;top:1180px">✓ Já está no clube</div>
{wa_card("wa", "Café da Esquina", optin, ("Sim, quero acompanhar", "Agora não"), top=430)}
{CTA}"""
    css = f"""
#hook{{top:600px}}
.cap .l.q{{font-size:84px}}
#phone{{position:absolute;left:{(W-PW)//2}px;top:{PT}px;width:{PW}px;height:{PH}px;border-radius:78px;padding:16px;
  background:linear-gradient(145deg,#30265A,#0E0A1E);box-shadow:0 0 0 2px rgba(183,156,255,.4),0 0 110px rgba(123,77,255,.55),0 50px 90px rgba(0,0,0,.6);
  transform-origin:50% 30%}}
.scr{{width:100%;height:100%;border-radius:62px;overflow:hidden;position:relative;background:#111521}}
.scr>img{{position:absolute;left:0;top:0;width:100%;height:auto}}
#cam{{position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 40%, #4A3A2A 0%, #1E1810 70%);opacity:0}}
#cam .lbl{{position:absolute;top:40px;left:0;right:0;text-align:center;color:#FFD54A;font-size:24px;font-weight:700;letter-spacing:.12em;text-transform:uppercase}}
#stand{{position:absolute;left:84px;right:84px;top:240px;padding:34px 28px 30px;border-radius:28px;background:#F5F0FF;color:#1A1030;text-align:center;
  box-shadow:0 30px 60px rgba(0,0,0,.5);transform:rotate(-4deg)}}
#stand .st1{{font-size:30px;font-weight:800}} #stand .st2{{font-size:22px;color:#5B5473;margin-top:4px}}
#stand .qr{{position:relative;width:250px;height:250px;margin:22px auto 14px}}
#stand .qr i{{position:absolute;width:4.9%;height:4.9%;background:#1A1030}}
#stand .st3{{font-size:20px;font-weight:700;color:#5B34E8;text-transform:uppercase;letter-spacing:.1em}}
#frame{{position:absolute;left:130px;top:330px;width:308px;height:308px}}
#frame b{{position:absolute;width:64px;height:64px;border:7px solid #FFD54A}}
#frame .a{{left:0;top:0;border-right:0;border-bottom:0;border-radius:18px 0 0 0}}
#frame .b{{right:0;top:0;border-left:0;border-bottom:0;border-radius:0 18px 0 0}}
#frame .c{{left:0;bottom:0;border-right:0;border-top:0;border-radius:0 0 0 18px}}
#frame .d{{right:0;bottom:0;border-left:0;border-top:0;border-radius:0 0 18px 0}}
#scan{{position:absolute;left:12px;right:12px;height:6px;border-radius:3px;background:#FFD54A;box-shadow:0 0 24px #FFD54A}}
#pill{{position:absolute;left:0;right:0;margin:auto;width:max-content;top:760px;padding:20px 30px;border-radius:999px;background:rgba(255,255,255,.95);
  color:#141024;font-size:28px;font-weight:800;opacity:0}}
#flash{{position:absolute;inset:0;background:#fff;opacity:0}}
#ring{{position:absolute;left:30px;right:30px;border-radius:30px;border:5px solid {C['amber']};
  box-shadow:0 0 40px rgba(255,194,77,.7), inset 0 0 30px rgba(255,194,77,.25);opacity:0}}
"""
    js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f}, FC="{fc}", NFC={nfc}, SH={SH};
window.R=async function(t){{
  const [n1a,n1b]=S.N1,[n2a,n2b]=S.N2,[n3a,n3b]=S.N3,[n4a,n4b]=S.N4,[n5a,n5b]=S.N5,[n6a,n6b]=S.N6;
  const ps=[];
  // gancho: citação, depois "Nem precisa."
  const h1=ease((t-(n1a-.05))/.45), h2=back((t-(U.s2-.05))/.45);
  $('h1').style.cssText=`opacity:${{h1}};transform:translateY(${{(1-h1)*40}}px)`;
  $('h2').style.cssText=`opacity:${{cl((t-(U.s2-.05))/.15)}};transform:scale(${{h2}})`;
  const ho=cl((t-(n2a-.45))/.35); $('hook').style.opacity=1-ho; $('hook').style.transform=`translateY(${{-ho*60}}px)`;
  // celular
  const pe=ease((t-(n2a-.3))/.6), ck=cta(t,n6a);
  const dip=1-.04*cl(1-Math.abs(t-(n4a-.2))/.25);
  $('phone').style.opacity=pe*(1-ck); $('phone').style.transform=`translateY(${{(1-pe)*700+ck*300}}px) scale(${{(1-ck*.1)*dip}})`;
  $('top').style.opacity=1-ck;
  // câmera lendo o QR (N2), flash e abre o link
  const camOut=cl((t-(n3a-.25))/.2);
  $('cam').style.opacity=(t<n2a-.3?0:1)*(1-camOut);
  const sp=((t-n2a)%1.1)/1.1; $('scan').style.top=`${{20+sp*268}}px`;
  $('frame').style.transform=`scale(${{lerp(1.25,1,(t-n2a)/.6)}})`;
  $('pill').style.opacity=cl((t-(n2b-.6))/.2); $('pill').style.transform=`translateY(${{(1-ease((t-(n2b-.6))/.3))*20}}px)`;
  $('flash').style.opacity=.85*cl(1-Math.abs(t-(n3a-.15))/.15);
  // tela real: página do clube → formulário → confirmado (N3); confirmado rolando (N4); cartão (N5)
  const vt=pw([[0,.5],[n3a-.2,.5],[n3a+.4,3.2],[U.pronto||n3b-.6,20.9],[n4a,22.5],[n5a-.2,31.4],[n5a-.19,37.0],[n5a,37.2],[T,39.6]],t);
  setImg($('sv'),`${{FC}}/${{pad(Math.min(NFC,Math.max(1,Math.round(vt*30)+1)))}}.jpg`,ps);
  // legendas
  show('c2',t,n2a,n3a); show('c3',t,n3a,n4a-.1); show('c4',t,n4a-.1,n5a); show('c5',t,n5a,n6a-.1);
  pop('ok',t,(U.pronto||n3b-.6)+.1,n4a+.2,-2);
  // WhatsApp: convite e toque em "Sim"
  const wi=back((t-(n4a+.1))/.5), wo=cl((t-(n5a-.15))/.35);
  $('wa').style.cssText=`top:430px;opacity:${{cl((t-(n4a+.1))/.2)*(1-wo)}};transform:translateY(${{(1-wi)*-260-wo*200}}px) scale(${{.96+wi*.04}})`;
  const tap=(U.sim||n4b-.9), bt=document.querySelector('#wa .bt');
  const tk=cl((t-tap)/.25);
  bt.style.background=tk>0?`rgba(46,212,122,${{.25+.75*tk}})`:'#EDE8FF'; bt.style.color=tk>.5?'#0F3D22':'#4A2BC8';
  bt.textContent=tk>.5?'✓ Sim, quero acompanhar':'Sim, quero acompanhar';
  bt.style.transform=`scale(${{1-.05*cl(1-Math.abs(t-tap)/.12)}})`;
  // anel no cartão
  const rg=io(t,n5a+.5,n6a-.1,.3,.25);
  $('ring').style.cssText=`opacity:${{rg}};top:${{16+.275*SH}}px;height:${{.235*SH}}px;transform:scale(${{lerp(1.1,1,(t-n5a-.5)/.3)}})`;
  await Promise.all(ps);
}};
"""
    return page(body, css, js), total


if __name__ == "__main__":
    main(build, "reel_03_sem_app.mp4", sys.argv)
