# -*- coding: utf-8 -*-
"""Reel 10 — "Onde foi parar o cartão de papel?" (2ª remessa: cenas por IA + movimento).

Uso: python3 reel_papel.py <pasta> [preview t1,t2,...]
  <pasta>/audio/narracao.mp3 + alinhamento.json (robô de narração, reels/10_cartao_papel)
  gerador/cenas/r10_*.png  cenas geradas por IA (1152x2048)
  <pasta>/fc_card.jpg      tela real do cartão digital (fluxo 03, celular da cliente)
"""
import json, sys
from pathlib import Path
from reel_base import *

CENAS = Path(__file__).parent / "cenas"
PW = 560
SH = round((PW - 32) * 1342 / 620)
PH = SH + 32

CTA_GRATIS = f"""<div id="cta">
  <img src="{LOGO_CLARA}" class="lg">
  <div class="t">Fidelidade que acontece<br>no <span class="hl">WhatsApp</span> do seu cliente.</div>
  <div class="pill">Crie o seu grátis · link na bio</div>
  <div class="semcc">✓ sem cartão de crédito</div>
  <div class="hd2">@pontua.club</div>
</div>"""

NOTIF = ("Olá, Sabrina Alves.<br><br>Você recebeu um novo carimbo de Café da Esquina.<br><br>"
         "No momento, faltam 2 carimbos para completar o cartão.")


def build(work):
    S, U, total = marcas(work)
    cena = {k: (CENAS / f"r10_{k}.png").as_uri() for k in ("balcao", "maquina", "gaveta", "lixo", "fundo")}
    fc = (work / "fc_card.jpg").as_uri()
    stamps = "".join(f'<i class="{"on" if k < 7 else ""}" id="st{k}"></i>' for k in range(10))
    body = f"""<div id="bg"></div>
<div class="sc" id="sc_balcao"><img src="{cena['balcao']}"></div>
<div class="sc" id="sc_maquina"><img src="{cena['maquina']}"></div>
<div class="sc" id="sc_gaveta"><img src="{cena['gaveta']}"></div>
<div class="sc" id="sc_lixo"><img src="{cena['lixo']}"></div>
<div class="sc" id="sc_fundo"><img src="{cena['fundo']}"></div>
<div id="shade"></div>
<div id="flash"></div>
{TOP}

<div class="cap" id="hook"><div class="l">Onde foi parar<br>o <span class="am">cartão de papel</span><br>do seu cliente?</div></div>
<div class="tag" id="t1">No bolso da calça<br><span class="am">que foi pra máquina.</span></div>
<div class="tag" id="t2">No fundo<br><span class="am">da gaveta.</span></div>
<div class="tag" id="t3">No lixo,<br><span class="am">sem querer.</span></div>

<div class="cap" id="c3a"><div class="l mid">E os carimbos<br><span class="am">foram junto.</span></div></div>
<div class="cap" id="c3b"><div class="l mid">O cliente recomeça<br>do zero… <span class="loss">ou desiste.</span></div></div>
<div id="card"><div class="ct">CARTÃO FIDELIDADE</div><div class="grid">{stamps}</div><div class="cnt" id="cnt">7/10</div></div>

<div class="cap step" id="c4"><span class="n wa">{WA_ICON}</span><div>No celular do cliente,<br><span class="hl">avisos no WhatsApp</span></div></div>
<div id="phone"><div class="scr"><img src="{fc}"></div></div>
<div id="wa">
  <div class="hd"><span class="ic">{WA_ICON}</span><span class="ap">WhatsApp</span><span class="tm">agora</span></div>
  <div class="ti">Café da Esquina</div>
  <div class="tx">{NOTIF}</div>
  <div class="bt">Ver meu cartão</div>
</div>
{CTA_GRATIS}"""
    css = f"""
#bg{{position:absolute;inset:0;background:#0B0816}}
.sc{{position:absolute;inset:0;overflow:hidden;opacity:0}}
.sc img{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;transform-origin:50% 50%}}
#shade{{position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,rgba(8,5,20,.88) 0%,rgba(8,5,20,.55) 22%,rgba(8,5,20,0) 42%,rgba(8,5,20,0) 70%,rgba(8,5,20,.6) 100%)}}
#flash{{position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none}}
#top{{z-index:3}}
.cap{{z-index:3}}
.cap .l{{font-size:96px;line-height:1.04;text-shadow:0 6px 40px rgba(0,0,0,.6)}}
.cap .l.mid{{font-size:84px}}
#hook{{top:250px}}
.loss{{color:{C['loss']};text-shadow:0 0 34px rgba(255,107,107,.45)}}
.tag{{position:absolute;left:70px;right:70px;top:250px;z-index:3;text-align:center;font-size:84px;font-weight:800;letter-spacing:-.04em;
  line-height:1.05;text-shadow:0 6px 40px rgba(0,0,0,.7);opacity:0}}
#c3a,#c3b{{top:250px}}
#card{{position:absolute;left:0;right:0;margin:auto;top:820px;width:820px;height:470px;border-radius:26px;z-index:2;opacity:0;
  background:linear-gradient(160deg,#E9DCC3,#D6C3A0);box-shadow:0 40px 90px rgba(0,0,0,.6);color:#5A4630;padding:40px 50px}}
#card .ct{{font-size:30px;font-weight:900;letter-spacing:.2em;opacity:.7}}
#card .grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:26px 30px;margin-top:40px}}
#card i{{display:block;width:112px;height:112px;border-radius:50%;border:4px solid rgba(90,70,48,.55);position:relative}}
#card i.on::after{{content:"";position:absolute;inset:10px;border-radius:50%;background:radial-gradient(circle,#3A2E5A 0%,#2A2246 60%,rgba(42,34,70,.6) 100%)}}
#card .cnt{{position:absolute;right:40px;top:30px;font-size:44px;font-weight:900;color:#5A4630}}
#c4{{top:240px}}
#c4 div{{font-size:60px}}
#phone{{position:absolute;left:{(W - PW) // 2}px;top:500px;width:{PW}px;height:{PH}px;border-radius:74px;padding:16px;z-index:2;opacity:0;
  background:linear-gradient(145deg,#30265A,#0E0A1E);box-shadow:0 0 0 2px rgba(183,156,255,.4),0 0 110px rgba(123,77,255,.55),0 50px 90px rgba(0,0,0,.6)}}
#phone .scr{{width:100%;height:100%;border-radius:58px;overflow:hidden;position:relative;background:#111521}}
#phone .scr img{{position:absolute;left:0;top:0;width:100%;height:auto}}
#wa{{position:absolute;left:70px;right:70px;top:1180px;z-index:4;padding:32px 36px;border-radius:38px;background:rgba(248,246,255,.98);color:#141024;opacity:0;
  box-shadow:0 30px 80px rgba(0,0,0,.55),0 0 90px rgba(37,211,102,.35)}}
#wa .hd{{display:flex;align-items:center;gap:16px;font-size:28px;color:#5B5473;font-weight:600}}
#wa .ic{{width:52px;height:52px;border-radius:15px;background:{C['green']};display:flex;align-items:center;justify-content:center}}
#wa .ic svg{{width:32px;height:32px}}
#wa .tm{{margin-left:auto;font-size:26px}}
#wa .ti{{font-size:40px;font-weight:800;margin-top:18px}}
#wa .tx{{font-size:34px;line-height:1.34;margin-top:10px;color:#2A2440}}
#wa .bt{{margin-top:20px;padding:20px;border-radius:20px;background:#EDE8FF;color:#4A2BC8;text-align:center;font-size:32px;font-weight:800}}
#cta{{z-index:5;background:radial-gradient(110% 60% at 80% 0%, #4A28C8 0%, #2A1470 35%, transparent 70%),radial-gradient(80% 50% at 0% 100%, #3A1BA8 0%, transparent 60%), #0E0822}}
#cta .semcc{{font-size:38px;font-weight:800;color:{C['gain']};margin-top:-20px}}
"""
    js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f};
// Ken Burns: escala e deslocamento por cena (a, b = início/fim da cena)
function kb(id,t,a,b,z0,z1,x0,x1,y0,y1){{ const k=cl((t-a)/Math.max(.1,b-a)); const e=$(id).querySelector('img');
  e.style.transform=`translate(${{lerp(x0,x1,k)}}px,${{lerp(y0,y1,k)}}px) scale(${{lerp(z0,z1,k)}})`; }}
function vis(id,t,a,b,fi=.22,fo=.22){{ const o=cl((t-a)/fi)*(1-cl((t-(b-fo))/fo)); $(id).style.opacity=o; return o; }}
window.R=async function(t){{
  const [n1a,n1b]=S.N1,[n2a,n2b]=S.N2,[n3a,n3b]=S.N3,[n4a,n4b]=S.N4,[n5a,n5b]=S.N5;
  const q2=U['N2.2']||(n2a+2.3), q3=U['N2.3']||(n2a+3.8), r2=U['N3.2']||(n3a+2.2);
  // cenas
  vis('sc_balcao',t,-1,n2a+.05,.01,.18);            kb('sc_balcao',t,0,n2a,1.04,1.16,0,0,0,-70);
  vis('sc_maquina',t,n2a-.02,q2+.05,.12,.12);        kb('sc_maquina',t,n2a,q2,1.12,1.02,0,0,-40,30);
  vis('sc_gaveta',t,q2-.02,q3+.05,.12,.12);          kb('sc_gaveta',t,q2,q3,1.06,1.16,0,0,-60,-20);
  vis('sc_lixo',t,q3-.02,n4a-.1,.12,.35);            kb('sc_lixo',t,q3,n4a,1.04,1.2,0,0,0,40);
  vis('sc_fundo',t,n4a-.5,n5a+.4,.35,.3);           kb('sc_fundo',t,n4a,n5a,1.02,1.1,0,0,0,0);
  // na parte do "cartão perdido", o lixo vira fundo escuro e desfocado
  const dk=ease((t-(n3a-.2))/.5);
  $('sc_lixo').querySelector('img').style.filter=`blur(${{dk*16}}px) brightness(${{1-.62*dk}}) saturate(${{1-.5*dk}})`;
  // flash curto nos cortes da sequência rápida
  const fl=Math.max(0,...[n2a,q2,q3].map(c=>1-Math.abs(t-c)/.09));
  $('flash').style.opacity=.32*fl;
  // legendas
  const h=ease((t-.05)/.4); $('hook').style.opacity=h*(1-cl((t-(n2a-.2))/.2)); $('hook').style.transform=`translateY(${{(1-h)*40}}px)`;
  show('t1',t,n2a,q2+.02); show('t2',t,q2,q3+.02); show('t3',t,q3,n3a+.05);
  show('c3a',t,n3a,r2); show('c3b',t,r2,n4a-.05);
  show('c4',t,n4a-.3,n5a-.1);
  // cartão de papel perdendo os carimbos (N3)
  const ci=back((t-(n3a+.05))/.5), co=cl((t-(n4a-.45))/.35);
  const tilt = ease((t-(r2+.6))/.8);
  $('card').style.opacity=cl((t-n3a)/.15)*(1-co);
  $('card').style.transform=`translateY(${{(1-ci)*120 + tilt*90}}px) rotate(${{-4+tilt*-10}}deg) scale(${{.9+.1*ci - tilt*.08}})`;
  $('card').style.filter=`grayscale(${{tilt*.8}}) brightness(${{1-tilt*.35}})`;
  const t0=n3a+1.0; let n=7;
  for(let k=0;k<7;k++){{ const tk=t0+k*.16; const on=t<tk; if(!on) n--; const e=$('st'+k); e.className=on?'on':'';
    e.style.transform = (t>=tk && t<tk+.15) ? `scale(${{1+.25*(1-(t-tk)/.15)}})` : ''; }}
  $('cnt').textContent=n+'/10'; $('cnt').style.color = n<7 ? '{C['loss']}' : '#5A4630';
  // celular + aviso no WhatsApp (N4)
  const pin=ease((t-(n4a-.3))/.6), pout=cl((t-(n5a-.25))/.3);
  $('phone').style.opacity=cl((t-(n4a-.32))/.2)*(1-pout); $('phone').style.transform=`translateY(${{(1-pin)*600}}px)`;
  const wq=n4a+.2, wk=back((t-wq)/.5);
  $('wa').style.opacity=cl((t-wq)/.15)*(1-pout); $('wa').style.transform=`translateY(${{(1-wk)*-140}}px) scale(${{.95+.05*wk}})`;
  // CTA
  const ck=cta(t,n5a);
  $('top').style.opacity=1-ck;
  await Promise.all([...document.images].map(i=>i.decode().catch(()=>{{}})));
}};
"""
    return page(body, css, js), total


if __name__ == "__main__":
    main(build, "reel_10_cartao_papel.mp4", sys.argv)
