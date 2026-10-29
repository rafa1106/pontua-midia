# -*- coding: utf-8 -*-
"""Reel 13 — "POV: você entrou no clube sem baixar nenhum aplicativo" (série Do lado do cliente).

Cena por IA (POV do celular apontado para o QR no balcão) + celular com a gravação real do fluxo 02
(cliente.mp4: página do clube → nome e telefone → confirmado → cartão) + convite real no WhatsApp.

Uso: python3 reel_pov.py <pasta> [preview t1,t2,...]
  <pasta>/fc  quadros do cliente.mp4 (fluxo 02, 620 px, realce aplicado) · <pasta>/audio (reels/13_pov_clube)
"""
import json, sys
from pathlib import Path
from reel_base import *
from reel_papel import CTA_GRATIS

CENAS = Path(__file__).parent / "cenas"
PW = 540
SH = round((PW - 32) * 1342 / 620)
PH = SH + 32
QR = dict(x=0, y=0, w=0, h=0)   # caixa do QR na cena (px da tela 1080x1920), definida em cenas/r13_pov.json

OPTIN = ("Olá, Larissa Mendes.<br><br>Café da Esquina te convidou para participar do programa de fidelidade "
         "e acompanhar seu cartão de fidelidade pelo WhatsApp.<br><br>Deseja receber atualizações por aqui?")


def build(work):
    S, U, total = marcas(work)
    q = json.loads((CENAS / "r13_pov.json").read_text())
    pov = (CENAS / "r13_pov.png").as_uri()
    fundo = (CENAS / "r10_fundo.png").as_uri()
    fc = (work / "fc").as_uri()
    nfc = len(list((work / "fc").glob("*.jpg")))
    body = f"""<div id="bg"></div>
<div class="sc" id="sc_pov"><img src="{pov}"></div>
<div class="sc" id="sc_fundo"><img src="{fundo}"></div>
<div id="shade"></div>
<div id="scanbox"><b class="a"></b><b class="b"></b><b class="c"></b><b class="d"></b><div id="scan"></div></div>
<div id="pill">🔗 Abrir clube da Café da Esquina</div>
<div id="flash"></div>
{TOP}
<div class="cap" id="hook"><div class="pov">POV:</div><div class="l">você entrou no clube<br>de fidelidade <span class="am">sem baixar<br>nenhum aplicativo.</span></div></div>
<div class="cap step" id="c2"><span class="n">1</span><div>Câmera<br><span class="hl">no QR do balcão</span></div></div>
<div class="cap step" id="c3"><span class="n">2</span><div>Nome<br><span class="hl">e WhatsApp</span></div></div>
<div class="cap step" id="c4"><span class="n wa">{WA_ICON}</span><div>Confirma<br><span class="hl">no WhatsApp</span></div></div>
<div class="cap step" id="c5"><span class="n">✓</span><div>Cartão<br><span class="hl">no celular</span></div></div>
<div id="phone"><div class="scr"><img id="sv" src="{fc}/0001.jpg"></div><div id="ring"></div></div>
<div id="wa">
  <div class="hd"><span class="ic">{WA_ICON}</span><span class="ap">WhatsApp</span><span class="tm">agora</span></div>
  <div class="ti">Café da Esquina</div>
  <div class="tx">{OPTIN}</div>
  <div class="bt" id="sim">Sim, quero acompanhar</div><div class="bt2">Agora não</div>
</div>
<div id="chips"><div class="ch" id="k1">⏱ menos de 1 minuto</div><div class="ch" id="k2">sem app · sem papel</div></div>
<div class="cap" id="c6"><div class="l mid">Pro seu cliente,<br><span class="am">é fácil assim.</span></div></div>
{CTA_GRATIS}"""
    css = f"""
#bg{{position:absolute;inset:0;background:#0B0816}}
.sc{{position:absolute;inset:0;overflow:hidden;opacity:0}}
.sc img{{position:absolute;left:0;top:0;width:{W}px;height:{H}px}}
#sc_pov img{{transform-origin:{q['x'] + q['w'] / 2}px {q['y'] + q['h'] / 2}px}}
#shade{{position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,rgba(8,5,20,.9) 0%,rgba(8,5,20,.5) 24%,rgba(8,5,20,0) 42%,rgba(8,5,20,0) 70%,rgba(8,5,20,.6) 100%)}}
#flash{{position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none;z-index:6}}
#top{{z-index:3}} .cap{{z-index:3}}
#hook{{top:230px}} #hook .pov{{font-size:64px;font-weight:900;color:{C['amber']};letter-spacing:.04em;margin-bottom:6px}}
.cap .l{{font-size:84px;line-height:1.05;text-shadow:0 6px 40px rgba(0,0,0,.6)}}
.cap .l.mid{{font-size:90px}}
#c6{{top:250px;z-index:4}}
#scanbox{{position:absolute;z-index:2;opacity:0;transform-origin:50% 50%}}
#scanbox b{{position:absolute;width:70px;height:70px;border:9px solid #FFD54A;filter:drop-shadow(0 0 12px rgba(255,213,74,.8))}}
#scanbox .a{{left:0;top:0;border-right:0;border-bottom:0;border-radius:22px 0 0 0}}
#scanbox .b{{right:0;top:0;border-left:0;border-bottom:0;border-radius:0 22px 0 0}}
#scanbox .c{{left:0;bottom:0;border-right:0;border-top:0;border-radius:0 0 0 22px}}
#scanbox .d{{right:0;bottom:0;border-left:0;border-top:0;border-radius:0 0 22px 0}}
#scan{{position:absolute;left:16px;right:16px;height:7px;border-radius:4px;background:#FFD54A;box-shadow:0 0 30px #FFD54A}}
#pill{{position:absolute;left:0;right:0;margin:auto;width:max-content;z-index:3;padding:24px 36px;border-radius:999px;background:rgba(255,255,255,.96);
  color:#141024;font-size:38px;font-weight:800;box-shadow:0 20px 60px rgba(0,0,0,.5);opacity:0}}
#phone{{position:absolute;left:{(W - PW) // 2}px;top:500px;width:{PW}px;height:{PH}px;border-radius:72px;padding:16px;z-index:2;opacity:0;
  background:linear-gradient(145deg,#30265A,#0E0A1E);box-shadow:0 0 0 2px rgba(183,156,255,.4),0 0 110px rgba(123,77,255,.55),0 50px 90px rgba(0,0,0,.6)}}
#phone .scr{{width:100%;height:100%;border-radius:56px;overflow:hidden;position:relative;background:#111521}}
#phone .scr img{{position:absolute;left:0;top:0;width:100%;height:auto}}
#phone .scr::after{{content:"";position:absolute;left:0;right:0;bottom:0;height:24%;background:linear-gradient(rgba(17,21,33,0),#111521 40%);opacity:var(--fade,0)}}
#ring{{position:absolute;left:30px;right:30px;border-radius:30px;border:5px solid {C['amber']};box-shadow:0 0 40px rgba(255,194,77,.7);opacity:0}}
#wa{{position:absolute;left:70px;right:70px;top:430px;z-index:4;padding:32px 36px;border-radius:38px;background:rgba(248,246,255,.98);color:#141024;opacity:0;
  box-shadow:0 30px 80px rgba(0,0,0,.55),0 0 90px rgba(37,211,102,.35)}}
#wa .hd{{display:flex;align-items:center;gap:16px;font-size:28px;color:#5B5473;font-weight:600}}
#wa .ic{{width:52px;height:52px;border-radius:15px;background:{C['green']};display:flex;align-items:center;justify-content:center}}
#wa .ic svg{{width:32px;height:32px}} #wa .tm{{margin-left:auto;font-size:26px}}
#wa .ti{{font-size:40px;font-weight:800;margin-top:18px}} #wa .tx{{font-size:34px;line-height:1.34;margin-top:10px;color:#2A2440}}
#wa .bt{{margin-top:22px;padding:22px;border-radius:20px;background:#EDE8FF;color:#4A2BC8;text-align:center;font-size:32px;font-weight:800}}
#wa .bt2{{margin-top:12px;padding:18px;text-align:center;font-size:30px;font-weight:700;color:#5B5473}}
#chips{{position:absolute;left:0;right:0;top:1500px;z-index:4;display:flex;flex-direction:column;align-items:center;gap:18px}}
.ch{{padding:20px 38px;border-radius:999px;background:rgba(248,246,255,.97);color:#141024;font-size:42px;font-weight:800;box-shadow:0 20px 60px rgba(0,0,0,.5);opacity:0}}
#cta{{z-index:5;background:radial-gradient(110% 60% at 80% 0%, #4A28C8 0%, #2A1470 35%, transparent 70%),radial-gradient(80% 50% at 0% 100%, #3A1BA8 0%, transparent 60%), #0E0822}}
#cta .semcc{{font-size:38px;font-weight:800;color:{C['gain']};margin-top:-20px}}
"""
    js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f}, FC="{fc}", NFC={nfc}, SH={SH}, Q={json.dumps(q)};
window.R=async function(t){{
  const N=[1,2,3,4,5,6].map(i=>S['N'+i]);
  const [n1a,n1b]=N[0],[n2a,n2b]=N[1],[n3a,n3b]=N[2],[n4a,n4b]=N[3],[n5a,n5b]=N[4],[n6a,n6b]=N[5];
  const ctaT=U['N6.2']||(n6a+1.6);
  const ps=[];
  // cena POV: aproxima devagar do QR; na fala 2 o enquadramento amarelo lê o código
  $('sc_pov').style.opacity=1-cl((t-(n3a-.15))/.05);
  const z=lerp(1.0,1.18,t/Math.max(.1,n3a)); $('sc_pov').querySelector('img').style.transform=`scale(${{z}})`;
  const cx=Q.x+Q.w/2, cy=Q.y+Q.h/2, bw=Q.w*z, bh=Q.h*z;   // o QR cresce junto com a cena (escala em torno do próprio centro)
  const si=cl((t-(n2a+.1))/.2), so=cl((t-(n3a-.2))/.1);
  const sb=$('scanbox'); sb.style.opacity=si*(1-so);
  sb.style.left=(cx-bw/2-20)+'px'; sb.style.top=(cy-bh/2-20)+'px'; sb.style.width=(bw+40)+'px'; sb.style.height=(bh+40)+'px';
  sb.style.transform=`scale(${{lerp(1.25,1,(t-(n2a+.1))/.5)}})`;
  $('scan').style.top=(16+(((t-n2a)%1.0)/1.0)*(bh+8))+'px';
  const pk=back((t-(n2b-.7))/.4); $('pill').style.opacity=cl((t-(n2b-.7))/.15)*(1-so); $('pill').style.transform=`scale(${{pk}})`;
  $('pill').style.top=(cy+bh/2+60)+'px';
  $('flash').style.opacity=.85*cl(1-Math.abs(t-(n3a-.12))/.14);
  // fundo do café desfocado para o celular
  $('sc_fundo').style.opacity=cl((t-(n3a-.12))/.05)*(1-cl((t-ctaT)/.5));
  $('sc_fundo').querySelector('img').style.transform=`scale(${{lerp(1.03,1.12,(t-n3a)/(T-n3a))}})`;
  // gancho e legendas
  const h=ease((t-.05)/.4); $('hook').style.opacity=h*(1-cl((t-(n2a-.2))/.2)); $('hook').style.transform=`translateY(${{(1-h)*40}}px)`;
  show('c2',t,n2a,n3a-.1); show('c3',t,n3a,n4a-.05); show('c4',t,n4a-.05,n5a-.25); show('c5',t,n5a-.05,n6a-.1); show('c6',t,n6a,ctaT);
  // celular com a gravação real (vt = segundos do cliente.mp4)
  const pin=ease((t-(n3a-.1))/.55), pout=cl((t-(ctaT-.3))/.3);
  $('phone').style.opacity=cl((t-(n3a-.12))/.15)*(1-pout); $('phone').style.transform=`translateY(${{(1-pin)*500}}px)`;
  const vt=pw([[0,.5],[n3a,.5],[n3a+.35,3.2],[n3b-.15,20.9],[n4a,21.6],[n5a-.12,24.0],[n5a-.11,37.0],[n5a+.3,37.2],[T,39.4]],t);
  setImg($('sv'),`${{FC}}/${{pad(Math.min(NFC,Math.max(1,Math.round(vt*30)+1)))}}.jpg`,ps);
  $('phone').style.setProperty('--fade', t>=n5a-.11 ? 1 : 0);
  // convite real no WhatsApp e toque em "Sim"
  const wi=back((t-(n4a+.05))/.5), wo=cl((t-(n5a-.42))/.3);
  $('wa').style.opacity=cl((t-(n4a+.05))/.15)*(1-wo); $('wa').style.transform=`translateY(${{(1-wi)*-220-wo*160}}px) scale(${{.96+.04*wi}})`;
  const tap=n4a+.62*(n4b-n4a), tk=cl((t-tap)/.2), bt=$('sim');
  bt.style.background=tk>0?`rgba(46,212,122,${{.25+.75*tk}})`:'#EDE8FF'; bt.style.color=tk>.5?'#0F3D22':'#4A2BC8';
  bt.textContent=tk>.5?'✓ Sim, quero acompanhar':'Sim, quero acompanhar'; bt.style.transform=`scale(${{1-.05*cl(1-Math.abs(t-tap)/.12)}})`;
  // cartão: anel + selos
  const rg=io(t,n5a+.3,n6a-.2,.3,.25);
  $('ring').style.cssText=`opacity:${{rg}};top:${{16+.275*SH}}px;height:${{.235*SH}}px`;
  const d5=n5b-n5a;
  [['k1',.45],['k2',.72]].forEach(([id,f])=>{{ const tq=n5a+f*d5, k=back((t-tq)/.4); $(id).style.opacity=cl((t-tq)/.12)*(1-pout); $(id).style.transform=`scale(${{k}})`; }});
  const ck=cta(t,ctaT); $('top').style.opacity=1-ck;
  await Promise.all(ps.concat([...document.images].map(i=>i.decode().catch(()=>{{}}))));
}};
"""
    return page(body, css, js), total


if __name__ == "__main__":
    main(build, "reel_13_pov_clube.mp4", sys.argv)
