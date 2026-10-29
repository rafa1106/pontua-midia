# -*- coding: utf-8 -*-
"""Reel 15 — "Cafeteria: 10 cafés, 1 grátis. Sem papel." (série Pra quem é).

Cenas por IA: espresso (N1), padaria (N2, r11), carimbo de borracha e cartões de papel (N3), café desfocado (N4, r10),
cappuccino servido (N5). Celular com o cartão real (fluxo 03), avisos reais do WhatsApp em pilha, cartão 10/10.

Uso: python3 reel_cafe.py <pasta> [preview t1,t2,...]   <pasta>/audio (reels/15_cafeteria) · <pasta>/fc_card.jpg
"""
import json, sys
from pathlib import Path
from reel_base import *
from reel_papel import CTA_GRATIS

CENAS = Path(__file__).parent / "cenas"
PW = 520
SH = round((PW - 32) * 1342 / 620)
PH = SH + 32

AV = [
    ("Olá, Sabrina Alves.<br>Você recebeu um novo carimbo de Café da Esquina.<br>No momento, <b>faltam 3 carimbos</b> para completar o cartão.", "7/10"),
    ("Olá, Sabrina Alves.<br>Você recebeu um novo carimbo de Café da Esquina.<br>No momento, <b>faltam 2 carimbos</b> para completar o cartão.", "8/10"),
    ("Olá, Sabrina Alves!<br>Seu cartão da Café da Esquina foi <b>completado com sucesso.</b>", "10/10 🎉"),
]


def build(work):
    S, U, total = marcas(work)
    c = {k: (CENAS / f).as_uri() for k, f in (("esp", "r15_espresso.png"), ("pad", "r11_padaria.png"), ("rub", "r15_carimbo.png"),
                                             ("fun", "r10_fundo.png"), ("cap", "r15_cappuccino.png"))}
    fc = (work / "fc_card.jpg").as_uri()
    scenes = "".join(f'<div class="sc" id="sc_{k}"><img src="{v}"></div>' for k, v in c.items())
    avs = "".join(f'<div class="av" id="a{i}"><div class="hd"><span class="ic">{WA_ICON}</span><span>WhatsApp · <b>Café da Esquina</b></span>'
                  f'<span class="pr">{p}</span></div><div class="tx">{tx}</div></div>' for i, (tx, p) in enumerate(AV))
    st = "".join(f'<i id="k{j}" class="on">☕</i>' for j in range(10))
    body = f"""<div id="bg"></div>
{scenes}
<div id="shade"></div><div id="flash"></div>
{TOP}
<div class="cap" id="hook"><div class="chip0">☕ Cafeteria</div><div class="l">10 cafés,<br>1 grátis.<br><span class="am">Sem papel.</span></div></div>
<div class="cap step" id="c2"><span class="n">☕</span><div>O cafezinho de todo dia,<br><span class="hl">carimbo no celular</span></div></div>
<div id="phone"><div class="scr"><img src="{fc}"></div></div>
<div id="plus">+1</div>
<div class="cap" id="c3"><div class="l mid">Sem nada disso:</div></div>
<div id="nos">
  <div class="no" id="x1"><span class="ix">✕</span><span class="tt">cartão pra perder</span></div>
  <div class="no" id="x2"><span class="ix">✕</span><span class="tt">carimbo de borracha</span></div>
  <div class="no" id="x3"><span class="ix">✕</span><span class="tt">aplicativo pra baixar</span></div>
</div>
<div class="cap step" id="c4"><span class="n wa">{WA_ICON}</span><div>A cada visita,<br><span class="hl">aviso no WhatsApp</span></div></div>
<div id="stack">{avs}</div>
<div id="nota">textos reais dos avisos · nome de exemplo</div>
<div class="cap" id="c5"><div class="l mid">O 10º café é<br><span class="am">por conta da casa.</span></div></div>
<div id="card"><div class="hd"><b>Cartão Café da Esquina</b><span>1 café grátis</span></div><div class="grid">{st}</div>
  <div class="ft"><span>10 de 10</span><span class="gift">✓ prêmio liberado!</span></div></div>
{CTA_GRATIS}"""
    css = f"""
#bg{{position:absolute;inset:0;background:#0B0816}}
.sc{{position:absolute;inset:0;overflow:hidden;opacity:0}}
.sc img{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;transform-origin:50% 50%}}
#shade{{position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,rgba(8,5,20,.9) 0%,rgba(8,5,20,.5) 24%,rgba(8,5,20,0) 42%,rgba(8,5,20,0) 60%,rgba(8,5,20,.72) 100%)}}
#flash{{position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none;z-index:6}}
#top{{z-index:3}} .cap{{z-index:3}}
.cap .l{{font-size:112px;line-height:1.02;text-shadow:0 6px 40px rgba(0,0,0,.6)}}
.cap .l.mid{{font-size:84px}}
#hook{{top:230px}} #c3,#c5{{top:250px}} #c2,#c4{{top:240px}} #c2 div,#c4 div{{font-size:58px}}
.chip0{{display:inline-block;margin-bottom:28px;padding:14px 34px;border-radius:999px;background:rgba(13,10,24,.78);border:2px solid rgba(183,156,255,.55);
  font-size:42px;font-weight:900}}
#phone{{position:absolute;left:{(W - PW) // 2}px;top:520px;width:{PW}px;height:{PH}px;border-radius:70px;padding:16px;z-index:2;opacity:0;
  background:linear-gradient(145deg,#30265A,#0E0A1E);box-shadow:0 0 0 2px rgba(183,156,255,.4),0 0 110px rgba(123,77,255,.55),0 50px 90px rgba(0,0,0,.6)}}
#phone .scr{{width:100%;height:100%;border-radius:54px;overflow:hidden;position:relative;background:#111521}}
#phone .scr img{{position:absolute;left:0;top:0;width:100%;height:auto}}
#phone .scr::after{{content:"";position:absolute;left:0;right:0;bottom:0;height:42%;background:linear-gradient(rgba(17,21,33,0),#111521 30%)}}
#plus{{position:absolute;left:0;right:0;margin:auto;width:230px;height:230px;border-radius:50%;z-index:4;display:flex;align-items:center;justify-content:center;
  background:radial-gradient(circle,#FFD777 0%,#FFC24D 55%,#E8A020 100%);color:#1A1030;font-size:96px;font-weight:900;opacity:0;
  box-shadow:0 20px 70px rgba(255,194,77,.6)}}
#nos{{position:absolute;left:90px;right:90px;top:900px;z-index:3;display:flex;flex-direction:column;gap:30px}}
.no{{display:flex;align-items:center;gap:26px;padding:26px 34px;border-radius:30px;background:rgba(13,10,24,.82);border:2px solid rgba(255,255,255,.18);opacity:0;
  box-shadow:0 20px 60px rgba(0,0,0,.5)}}
.no .ix{{flex:0 0 76px;height:76px;border-radius:50%;background:{C['loss']};color:#fff;display:flex;align-items:center;justify-content:center;font-size:44px;font-weight:900}}
.no .tt{{position:relative;font-size:56px;font-weight:800;letter-spacing:-.02em}}
.no .tt::after{{content:"";position:absolute;left:-6px;top:52%;height:7px;border-radius:4px;background:{C['loss']};width:var(--sk,0%)}}
#stack{{position:absolute;left:60px;right:60px;top:470px;z-index:3}}
.av{{margin-bottom:24px;padding:26px 30px;border-radius:30px;background:rgba(248,246,255,.98);color:#141024;opacity:0;box-shadow:0 26px 70px rgba(0,0,0,.5)}}
.av .hd{{display:flex;align-items:center;gap:14px;font-size:26px;color:#5B5473;font-weight:600}} .av .hd b{{color:#141024}}
.av .ic{{width:46px;height:46px;border-radius:13px;background:{C['green']};display:flex;align-items:center;justify-content:center}} .av .ic svg{{width:28px;height:28px}}
.av .pr{{margin-left:auto;padding:6px 16px;border-radius:999px;background:#EDE8FF;color:#4A2BC8;font-size:24px;font-weight:900;white-space:nowrap}}
.av .tx{{font-size:33px;line-height:1.36;margin-top:12px;color:#2A2440}} .av .tx b{{background:#FFF1C9}}
#a2 .pr{{background:{C['amber']};color:#1A1030}}
#nota{{position:absolute;left:0;right:0;top:1560px;text-align:center;z-index:3;font-size:26px;font-weight:600;color:rgba(230,224,255,.7);opacity:0}}
#card{{position:absolute;left:0;right:0;margin:auto;top:1200px;width:880px;border-radius:34px;padding:28px 34px;z-index:3;opacity:0;color:#fff;
  background:linear-gradient(135deg,#C9692A,#E8943A);box-shadow:0 30px 80px rgba(0,0,0,.6)}}
#card .hd{{display:flex;justify-content:space-between;align-items:center;font-size:32px;font-weight:800}}
#card .hd span{{padding:8px 18px;border-radius:999px;background:rgba(255,255,255,.22);font-size:26px}}
#card .grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;margin-top:22px}}
#card i{{height:96px;border-radius:22px;background:rgba(255,255,255,.95);display:flex;align-items:center;justify-content:center;font-size:52px;font-style:normal}}
#card i img{{width:54px;height:54px}}
#card .ft{{display:flex;justify-content:space-between;align-items:center;margin-top:18px;font-size:34px;font-weight:900}}
#card .gift{{padding:10px 24px;border-radius:999px;background:{C['amber']};color:#1A1030}}
#cta{{z-index:5;background:radial-gradient(110% 60% at 80% 0%, #4A28C8 0%, #2A1470 35%, transparent 70%),radial-gradient(80% 50% at 0% 100%, #3A1BA8 0%, transparent 60%), #0E0822}}
#cta .semcc{{font-size:38px;font-weight:800;color:{C['gain']};margin-top:-20px}}
"""
    js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f}, SH={SH};
function vis(id,t,a,b,fi=.2,fo=.2){{ const o=cl((t-a)/fi)*(1-cl((t-(b-fo))/fo)); $(id).style.opacity=o; return o; }}
function kb(id,t,a,b,z0,z1,y0,y1){{ const k=cl((t-a)/Math.max(.1,b-a)); $(id).querySelector('img').style.transform=`translateY(${{lerp(y0,y1,k)}}px) scale(${{lerp(z0,z1,k)}})`; }}
window.R=async function(t){{
  const N=[1,2,3,4,5,6].map(i=>S['N'+i]);
  const [n1a,n1b]=N[0],[n2a,n2b]=N[1],[n3a,n3b]=N[2],[n4a,n4b]=N[3],[n5a,n5b]=N[4],[n6a]=N[5];
  // cenas
  vis('sc_esp',t,-1,n2a+.05,.01,.15); kb('sc_esp',t,0,n2a,1.04,1.16,0,-50);
  vis('sc_pad',t,n2a-.05,n3a+.05,.15,.15); kb('sc_pad',t,n2a,n3a,1.12,1.03,-30,20);
  vis('sc_rub',t,n3a-.05,n4a+.05,.15,.15); kb('sc_rub',t,n3a,n4a,1.03,1.14,0,-40);
  $('sc_rub').querySelector('img').style.filter=`brightness(${{.62}}) saturate(.75)`;
  vis('sc_fun',t,n4a-.05,n5a+.05,.15,.15); kb('sc_fun',t,n4a,n5a,1.03,1.12,0,0);
  vis('sc_cap',t,n5a-.05,n6a+.6,.15,.3); kb('sc_cap',t,n5a,T,1.1,1.0,-30,20);
  const fl=Math.max(0,...[n2a,n3a,n4a,n5a].map(c=>1-Math.abs(t-c)/.09)); $('flash').style.opacity=.25*fl;
  // gancho
  const h=ease((t-.05)/.4); $('hook').style.opacity=h*(1-cl((t-(n2a-.2))/.2)); $('hook').style.transform=`translateY(${{(1-h)*40}}px)`;
  // N2: celular com o cartão real + carimbo voando para dentro
  show('c2',t,n2a,n3a-.05);
  const pin=ease((t-(n2a+.05))/.55), pout=cl((t-(n3a-.25))/.25);
  $('phone').style.opacity=cl((t-n2a)/.2)*(1-pout); $('phone').style.transform=`translateY(${{(1-pin)*600}}px)`;
  const pq=n2a+.55*(n2b-n2a), pk=ease((t-pq)/.55);
  $('plus').style.opacity=cl((t-pq)/.1)*(1-cl((t-(pq+.5))/.15));
  $('plus').style.top=lerp(1480,860,pk)+'px'; $('plus').style.transform=`scale(${{lerp(1.15,.45,pk)}})`;
  // N3: três coisas riscadas
  show('c3',t,n3a,n4a-.05);
  const d3=n3b-n3a;
  [['x1',.04],['x2',.36],['x3',.68]].forEach(([id,f])=>{{ const tq=n3a+f*d3, k=back((t-tq)/.4), e=$(id);
    e.style.opacity=cl((t-tq)/.12)*(1-cl((t-(n4a-.2))/.2)); e.style.transform=`translateX(${{(1-k)*-140}}px)`;
    e.style.setProperty('--sk', (cl((t-(tq+.35))/.3)*104)+'%'); }});
  // N4: pilha de avisos reais
  show('c4',t,n4a,n5a-.05);
  const d4=n4b-n4a, ao=cl((t-(n5a-.2))/.25);
  [.32,.55,.8].forEach((f,i)=>{{ const tq=n4a+f*d4, k=back((t-tq)/.45);
    const e=$('a'+i); e.style.opacity=cl((t-tq)/.15)*(1-ao); e.style.transform=`translateY(${{(1-k)*-100}}px) scale(${{.95+.05*k}})`; }});
  $('nota').style.opacity=io(t,n4a+.9*d4-.3,n5a,.3,.2);
  // N5: o 10º café
  show('c5',t,n5a,n6a-.05);
  const ki=back((t-(n5a+.15))/.45), ko=cl((t-(n6a-.2))/.2);
  $('card').style.opacity=cl((t-(n5a+.15))/.15)*(1-ko); $('card').style.transform=`translateY(${{(1-ki)*160}}px) rotate(-1.5deg)`;
  const gq=n5a+.6, g=back((t-gq)/.4); document.querySelector('#card .gift').style.cssText=`opacity:${{cl((t-gq)/.1)}};transform:scale(${{g}})`;
  const ck=cta(t,n6a); $('top').style.opacity=1-ck;
  await Promise.all([...document.images].map(i=>i.decode().catch(()=>{{}})));
}};
"""
    return page(body, css, js), total


if __name__ == "__main__":
    main(build, "reel_15_cafeteria.mp4", sys.argv)
