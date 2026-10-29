# -*- coding: utf-8 -*-
"""Reel 16 — "Por que o cliente volta mais rápido quando faltam 2?" (série A ciência da fidelidade).

Estudo: Kivetz, Urminsky & Zheng (2006), "The Goal-Gradient Hypothesis Resurrected", Journal of Marketing Research 43(1):
num cartão "compre 10 cafés, ganhe 1", os clientes compraram com mais frequência à medida que se aproximavam do café grátis.
Sem número na tela (o resumo aberto não traz a porcentagem); o gráfico é marcado como ilustração do padrão.

Uso: python3 reel_gradiente.py <pasta> [preview t1,t2,...]   <pasta>/audio (reels/16_faltam_dois) · <pasta>/fc_card.jpg
"""
import json, sys
from pathlib import Path
from reel_base import *
from reel_papel import CTA_GRATIS, NOTIF

CENAS = Path(__file__).parent / "cenas"
PW = 520
SH = round((PW - 32) * 1342 / 620)
PH = SH + 32
BARS = [100, 96, 90, 84, 76, 68, 58, 47, 36]   # altura relativa do intervalo até a próxima visita (ilustrativa)


def build(work):
    S, U, total = marcas(work)
    c = {k: (CENAS / f).as_uri() for k, f in (("che", "r16_chegada.png"), ("bal", "r10_balcao.png"), ("gav", "r10_gaveta.png"), ("pad", "r11_padaria.png"))}
    fc = (work / "fc_card.jpg").as_uri()
    scenes = "".join(f'<div class="sc" id="sc_{k}"><img src="{v}"></div>' for k, v in c.items())
    bars = "".join(f'<div class="col"><div class="b" id="b{i}" style="--h:{h}%"></div><span>{i + 1}º</span></div>' for i, h in enumerate(BARS))
    body = f"""<div id="bg"></div>
{scenes}
<div id="shade"></div><div id="flash"></div>
{TOP}
<div class="cap" id="hook"><div class="l">Por que o cliente<br>volta mais rápido<br>quando <span class="am">faltam 2?</span></div></div>
<div class="cap" id="c2"><div class="l mid">Um estudo com<br>o cartão de uma <span class="hl">cafeteria</span></div></div>
<div class="tagc" id="t2">☕ 10 cafés, 1 grátis</div>
<div class="cap" id="c3"><div class="l mid">Mais perto do grátis,<br><span class="am">mais rápido ele volta.</span></div></div>
<div id="chart"><div class="ttl">tempo até a próxima visita</div><div class="bars">{bars}</div>
  <div class="ax">carimbos no cartão → <b>café grátis</b></div>
  <div class="src">ilustração do padrão observado · Kivetz, Urminsky &amp; Zheng (2006), Journal of Marketing Research</div></div>
<div class="cap" id="c4"><div class="chip0">gradiente de meta</div><div class="l mid">Perto da chegada,<br><span class="am">a gente acelera.</span></div></div>
<div class="cap" id="c5"><div class="l mid">Mas o cliente precisa<br><span class="loss">ver quanto falta.</span></div></div>
<div class="cap step" id="c6"><span class="n wa">{WA_ICON}</span><div>Cada carimbo:<br><span class="hl">quanto falta, no WhatsApp</span></div></div>
<div id="phone"><div class="scr"><img src="{fc}"></div></div>
<div id="wa">
  <div class="hd"><span class="ic">{WA_ICON}</span><span class="ap">WhatsApp</span><span class="tm">agora</span></div>
  <div class="ti">Café da Esquina</div>
  <div class="tx">{NOTIF.replace("faltam 2 carimbos", "<b>faltam 2 carimbos</b>")}</div>
</div>
{CTA_GRATIS}"""
    css = f"""
#bg{{position:absolute;inset:0;background:#0B0816}}
.sc{{position:absolute;inset:0;overflow:hidden;opacity:0}}
.sc img{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;transform-origin:50% 50%}}
#shade{{position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,rgba(8,5,20,.9) 0%,rgba(8,5,20,.5) 26%,rgba(8,5,20,0) 44%,rgba(8,5,20,0) 60%,rgba(8,5,20,.72) 100%)}}
#flash{{position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none;z-index:6}}
#top{{z-index:3}} .cap{{z-index:3}}
.cap .l{{font-size:96px;line-height:1.04;text-shadow:0 6px 40px rgba(0,0,0,.6)}}
.cap .l.mid{{font-size:80px}}
#hook,#c2,#c3,#c4,#c5{{top:250px}} #c6{{top:240px}} #c6 div{{font-size:56px}}
.loss{{color:{C['loss']};text-shadow:0 0 34px rgba(255,107,107,.45)}}
.chip0{{display:inline-block;margin-bottom:26px;padding:12px 30px;border-radius:999px;background:rgba(13,10,24,.78);border:2px solid rgba(183,156,255,.55);
  font-size:36px;font-weight:900;color:{C['lilac']};text-transform:uppercase;letter-spacing:.1em}}
.tagc{{position:absolute;left:0;right:0;margin:auto;width:max-content;top:1380px;z-index:4;padding:22px 40px;border-radius:999px;background:{C['amber']};color:#1A1030;
  font-size:48px;font-weight:900;box-shadow:0 14px 50px rgba(255,194,77,.45);opacity:0}}
#chart{{position:absolute;left:60px;right:60px;top:640px;z-index:3;opacity:0;padding:40px 40px 34px;border-radius:34px;background:rgba(13,10,24,.84);
  border:2px solid rgba(183,156,255,.35);box-shadow:0 30px 80px rgba(0,0,0,.5)}}
#chart .ttl{{font-size:38px;font-weight:800;color:#E6E0FF}}
#chart .bars{{display:flex;align-items:flex-end;gap:16px;height:520px;margin-top:28px;border-bottom:3px solid rgba(255,255,255,.25)}}
#chart .col{{flex:1;height:100%;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;position:relative}}
#chart .b{{width:100%;border-radius:16px 16px 4px 4px;height:0;background:linear-gradient(180deg,{C['violet2']},{C['violet']})}}
#chart .col span{{position:absolute;bottom:-50px;font-size:28px;font-weight:800;color:{C['muted']}}}
#chart .b.hot{{background:linear-gradient(180deg,#FFD777,{C['amber']});box-shadow:0 0 30px rgba(255,194,77,.5)}}
#chart .ax{{margin-top:66px;font-size:32px;font-weight:700;color:{C['muted']}}} #chart .ax b{{color:{C['amber']}}}
#chart .src{{margin-top:20px;font-size:23px;font-weight:600;color:rgba(185,178,217,.8)}}
#phone{{position:absolute;left:{(W - PW) // 2}px;top:500px;width:{PW}px;height:{PH}px;border-radius:70px;padding:16px;z-index:2;opacity:0;
  background:linear-gradient(145deg,#30265A,#0E0A1E);box-shadow:0 0 0 2px rgba(183,156,255,.4),0 0 110px rgba(123,77,255,.55),0 50px 90px rgba(0,0,0,.6)}}
#phone .scr{{width:100%;height:100%;border-radius:54px;overflow:hidden;position:relative;background:#111521}}
#phone .scr img{{position:absolute;left:0;top:0;width:100%;height:auto}}
#phone .scr::after{{content:"";position:absolute;left:0;right:0;bottom:0;height:42%;background:linear-gradient(rgba(17,21,33,0),#111521 30%)}}
#wa{{position:absolute;left:70px;right:70px;top:1220px;z-index:4;padding:30px 36px;border-radius:38px;background:rgba(248,246,255,.98);color:#141024;opacity:0;
  box-shadow:0 30px 80px rgba(0,0,0,.55),0 0 90px rgba(37,211,102,.35)}}
#wa .hd{{display:flex;align-items:center;gap:16px;font-size:28px;color:#5B5473;font-weight:600}}
#wa .ic{{width:52px;height:52px;border-radius:15px;background:{C['green']};display:flex;align-items:center;justify-content:center}}
#wa .ic svg{{width:32px;height:32px}} #wa .tm{{margin-left:auto;font-size:26px}}
#wa .ti{{font-size:38px;font-weight:800;margin-top:16px}} #wa .tx{{font-size:32px;line-height:1.34;margin-top:10px;color:#2A2440}} #wa .tx b{{background:#FFF1C9}}
#cta{{z-index:5;background:radial-gradient(110% 60% at 80% 0%, #4A28C8 0%, #2A1470 35%, transparent 70%),radial-gradient(80% 50% at 0% 100%, #3A1BA8 0%, transparent 60%), #0E0822}}
#cta .semcc{{font-size:38px;font-weight:800;color:{C['gain']};margin-top:-20px}}
"""
    js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f};
function vis(id,t,a,b,fi=.2,fo=.2){{ const o=cl((t-a)/fi)*(1-cl((t-(b-fo))/fo)); $(id).style.opacity=o; return o; }}
function kb(id,t,a,b,z0,z1,y0,y1){{ const k=cl((t-a)/Math.max(.1,b-a)); $(id).querySelector('img').style.transform=`translateY(${{lerp(y0,y1,k)}}px) scale(${{lerp(z0,z1,k)}})`; }}
window.R=async function(t){{
  const N=[1,2,3,4,5,6,7].map(i=>S['N'+i]);
  const [n1a,n1b]=N[0],[n2a,n2b]=N[1],[n3a,n3b]=N[2],[n4a,n4b]=N[3],[n5a,n5b]=N[4],[n6a,n6b]=N[5],[n7a]=N[6];
  // cenas: chegada (N1), cartão de papel na cafeteria (N2–N3, escuro), chegada acelerando (N4), gaveta (N5), padaria (N6)
  vis('sc_che',t,-1,n2a+.05,.01,.15); kb('sc_che',t,0,n2a,1.02,1.1,0,-30);
  vis('sc_bal',t,n2a-.05,n4a+.05,.15,.15); kb('sc_bal',t,n2a,n4a,1.04,1.16,0,-40);
  const dk=ease((t-(n3a-.3))/.5); $('sc_bal').querySelector('img').style.filter=`blur(${{dk*12}}px) brightness(${{1-.5*dk}})`;
  if(t>=n4a-.05 && t<n5a+.05){{ vis('sc_che',t,n4a-.05,n5a+.05,.12,.15); const k=cl((t-n4a)/(n5a-n4a));
    $('sc_che').querySelector('img').style.transform=`scale(${{1.06+.34*k*k}})`; $('sc_che').querySelector('img').style.filter=`blur(${{3*k*k}}px)`; }}
  else $('sc_che').querySelector('img').style.filter='';
  vis('sc_gav',t,n5a-.05,n6a+.05,.15,.15); kb('sc_gav',t,n5a,n6a,1.1,1.02,-20,20);
  $('sc_gav').querySelector('img').style.filter='brightness(.7) saturate(.7)';
  vis('sc_pad',t,n6a-.05,n7a+.6,.15,.3); kb('sc_pad',t,n6a,T,1.03,1.12,0,0);
  $('sc_pad').querySelector('img').style.filter='blur(10px) brightness(.62)';
  const fl=Math.max(0,...[n2a,n4a,n5a,n6a].map(c=>1-Math.abs(t-c)/.09)); $('flash').style.opacity=.25*fl;
  // legendas
  const h=ease((t-.05)/.4); $('hook').style.opacity=h*(1-cl((t-(n2a-.2))/.2)); $('hook').style.transform=`translateY(${{(1-h)*40}}px)`;
  show('c2',t,n2a,n3a-.05); show('c3',t,n3a,n4a-.05); show('c4',t,n4a,n5a-.05); show('c5',t,n5a,n6a-.05); show('c6',t,n6a,n7a-.1);
  const tg=back((t-(n2a+.9))/.4); $('t2').style.opacity=io(t,n2a+.9,n3a-.05,.12,.2); $('t2').style.transform=`scale(${{tg}})`;
  // gráfico: barras do intervalo entre visitas, encolhendo à medida que o cartão enche
  const gi=ease((t-(n3a+.05))/.4), go=cl((t-(n4a-.2))/.25);
  $('chart').style.opacity=gi*(1-go); $('chart').style.transform=`translateY(${{(1-gi)*60}}px)`;
  {json.dumps(BARS)}.forEach((hh,i)=>{{ const tq=n3a+.35+i*.2, k=ease((t-tq)/.35), e=$('b'+i);
    e.style.height=(hh*k)+'%'; e.className = i>=7 ? 'b hot' : 'b'; }});
  // celular + aviso real
  const pin=ease((t-(n6a+.05))/.55), pout=cl((t-(n7a-.25))/.3);
  $('phone').style.opacity=cl((t-n6a)/.2)*(1-pout); $('phone').style.transform=`translateY(${{(1-pin)*600}}px)`;
  const wq=n6a+.4*(n6b-n6a), wk=back((t-wq)/.5);
  $('wa').style.opacity=cl((t-wq)/.15)*(1-pout); $('wa').style.transform=`translateY(${{(1-wk)*-140}}px) scale(${{.95+.05*wk}})`;
  const ck=cta(t,n7a); $('top').style.opacity=1-ck;
  await Promise.all([...document.images].map(i=>i.decode().catch(()=>{{}})));
}};
"""
    return page(body, css, js), total


if __name__ == "__main__":
    main(build, "reel_16_faltam_dois.mp4", sys.argv)
