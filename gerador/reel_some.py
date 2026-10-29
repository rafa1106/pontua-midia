# -*- coding: utf-8 -*-
"""Reel 14 — "Cliente que some não avisa" (série A dor do balcão; viés: aversão à perda + gradiente de meta).

Cenas por IA: mesa vazia (N1–N2), cliente na correria com o celular (N3–N4: a tela do celular da cena
acende com o aviso), cliente voltando pela porta (N5). Calendário animado dos dias sem aparecer (N2),
aviso real do WhatsApp ("faltam 2 carimbos"), cartão 8/10 (N5) e CTA do grátis.

Uso: python3 reel_some.py <pasta> [preview t1,t2,...]   <pasta>/audio (reels/14_cliente_some)
"""
import json, sys
from pathlib import Path
from reel_base import *
from reel_papel import CTA_GRATIS, NOTIF

CENAS = Path(__file__).parent / "cenas"


def build(work):
    S, U, total = marcas(work)
    c = {k: (CENAS / f"r14_{k}.png").as_uri() for k in ("mesa", "rua", "volta")}
    dias = "".join(f'<i id="d{k}"><span>{k + 1}</span></i>' for k in range(28))
    st = "".join(f'<i id="s{k}" class="{"on" if k < 8 else ""}">{"☕" if k < 8 else ""}</i>' for k in range(10))
    body = f"""<div id="bg"></div>
<div class="sc" id="sc_mesa"><div class="w"><img src="{c['mesa']}"></div></div>
<div class="sc" id="sc_rua"><div class="w"><img src="{c['rua']}">
  <div id="tela"><div class="lk">09:41</div><div class="nt"><span class="ic">{WA_ICON}</span><div><b>Café da Esquina</b><br>faltam 2 carimbos…</div></div></div></div></div>
<div class="sc" id="sc_volta"><div class="w"><img src="{c['volta']}"></div></div>
<div id="shade"></div>
{TOP}
<div class="cap" id="hook"><div class="l">Cliente que some<br><span class="loss">não avisa.</span></div></div>
<div class="cap" id="c2"><div class="l mid">Um dia ele<br><span class="am">para de vir.</span></div></div>
<div class="cap" id="c2b"><div class="l mid">E você só percebe<br><span class="loss">semanas depois.</span></div></div>
<div id="cal"><div class="hd"><span>Última visita do Paulo</span><b id="cnt">0 dias</b></div><div class="grid">{dias}</div></div>
<div class="cap" id="c3"><div class="l mid">Na correria,<br>ele <span class="am">só esqueceu.</span></div></div>
<div class="cap step" id="c4"><span class="n wa">{WA_ICON}</span><div>Cada carimbo vira<br><span class="hl">aviso no WhatsApp</span></div></div>
<div id="wa">
  <div class="hd"><span class="ic">{WA_ICON}</span><span class="ap">WhatsApp</span><span class="tm">agora</span></div>
  <div class="ti">Café da Esquina</div>
  <div class="tx">{NOTIF.replace("Sabrina Alves", "Paulo Souza").replace("faltam 2 carimbos", "<b>faltam 2 carimbos</b>")}</div>
  <div class="bt">Ver meu cartão</div>
</div>
<div class="cap" id="c5a"><div class="l big"><span class="am">Faltam 2.</span></div></div>
<div class="cap" id="c5b"><div class="l mid">Ele lembra.<br><span class="hl">E volta.</span></div></div>
<div id="card"><div class="hd"><b>Cartão Café da Esquina</b><span>1 café grátis</span></div><div class="grid">{st}</div>
  <div class="ft"><span>8 de 10</span><span class="falt">faltam 2</span></div></div>
{CTA_GRATIS}"""
    css = f"""
#bg{{position:absolute;inset:0;background:#0B0816}}
.sc{{position:absolute;inset:0;overflow:hidden;opacity:0}}
.sc .w{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;transform-origin:50% 50%}}
.sc img{{position:absolute;left:0;top:0;width:{W}px;height:{H}px}}
#tela{{position:absolute;left:362px;top:740px;width:182px;height:426px;border-radius:26px;overflow:hidden;transform-origin:0 0;
  transform:skewX(8.4deg) rotate(-1.6deg);background:linear-gradient(170deg,#1C2A3A,#0E1622);opacity:0}}
#tela .lk{{margin-top:40px;text-align:center;color:#fff;font-size:44px;font-weight:300;letter-spacing:-.02em}}
#tela .nt{{margin:34px 10px 0;padding:10px;border-radius:14px;background:rgba(255,255,255,.92);display:flex;gap:8px;align-items:flex-start;
  font-size:14px;line-height:1.25;color:#141024}}
#tela .nt .ic{{flex:0 0 26px;height:26px;border-radius:8px;background:{C['green']};display:flex;align-items:center;justify-content:center}}
#tela .nt .ic svg{{width:17px;height:17px}}
#shade{{position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,rgba(8,5,20,.9) 0%,rgba(8,5,20,.5) 24%,rgba(8,5,20,0) 42%,rgba(8,5,20,0) 64%,rgba(8,5,20,.72) 100%)}}
#top{{z-index:3}} .cap{{z-index:3}}
.cap .l{{font-size:96px;line-height:1.04;text-shadow:0 6px 40px rgba(0,0,0,.6)}}
.cap .l.mid{{font-size:84px}} .cap .l.big{{font-size:150px;letter-spacing:-.05em}}
#hook,#c2,#c2b,#c3,#c5a,#c5b{{top:250px}} #c4{{top:240px}} #c4 div{{font-size:60px}}
.loss{{color:{C['loss']};text-shadow:0 0 34px rgba(255,107,107,.45)}}
#cal{{position:absolute;left:90px;right:90px;top:1040px;z-index:3;padding:30px 34px;border-radius:32px;background:rgba(248,246,255,.96);color:#1A1430;opacity:0;
  box-shadow:0 30px 80px rgba(0,0,0,.55)}}
#cal .hd{{display:flex;justify-content:space-between;align-items:baseline;font-size:34px;font-weight:800}}
#cal .hd b{{font-size:52px;font-weight:900;color:{C['loss']}}}
#cal .grid{{display:grid;grid-template-columns:repeat(7,1fr);gap:12px;margin-top:22px}}
#cal i{{position:relative;height:74px;border-radius:16px;background:#EEE9FA;display:flex;align-items:center;justify-content:center;font-style:normal;
  font-size:28px;font-weight:800;color:#6A6288}}
#cal i.v{{background:{C['violet2']};color:#fff}}
#cal i.x{{background:#FFE5E5;color:#C24545}}
#cal i.x::after{{content:"";position:absolute;left:14px;right:14px;top:50%;height:5px;border-radius:3px;background:{C['loss']};transform:rotate(-30deg)}}
#wa{{position:absolute;left:70px;right:70px;top:1210px;z-index:4;padding:30px 36px;border-radius:38px;background:rgba(248,246,255,.98);color:#141024;opacity:0;
  box-shadow:0 30px 80px rgba(0,0,0,.55),0 0 90px rgba(37,211,102,.35)}}
#wa .hd{{display:flex;align-items:center;gap:16px;font-size:28px;color:#5B5473;font-weight:600}}
#wa .ic{{width:52px;height:52px;border-radius:15px;background:{C['green']};display:flex;align-items:center;justify-content:center}}
#wa .ic svg{{width:32px;height:32px}} #wa .tm{{margin-left:auto;font-size:26px}}
#wa .ti{{font-size:38px;font-weight:800;margin-top:16px}} #wa .tx{{font-size:32px;line-height:1.34;margin-top:10px;color:#2A2440}}
#wa .tx b{{background:#FFF1C9}}
#wa .bt{{margin-top:18px;padding:18px;border-radius:20px;background:#EDE8FF;color:#4A2BC8;text-align:center;font-size:30px;font-weight:800}}
#card{{position:absolute;left:0;right:0;margin:auto;top:1180px;width:880px;border-radius:34px;padding:28px 34px;z-index:3;opacity:0;color:#fff;
  background:linear-gradient(135deg,#C9692A,#E8943A);box-shadow:0 30px 80px rgba(0,0,0,.6)}}
#card .hd{{display:flex;justify-content:space-between;align-items:center;font-size:32px;font-weight:800}}
#card .hd span{{padding:8px 18px;border-radius:999px;background:rgba(255,255,255,.22);font-size:26px}}
#card .grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;margin-top:22px}}
#card i{{height:96px;border-radius:22px;border:3px dashed rgba(255,255,255,.55);display:flex;align-items:center;justify-content:center;font-size:52px;font-style:normal}}
#card i img{{width:54px;height:54px}}
#card i.on{{background:rgba(255,255,255,.95);border:3px solid #fff}}
#card .ft{{display:flex;justify-content:space-between;align-items:center;margin-top:18px;font-size:34px;font-weight:900}}
#card .falt{{padding:10px 24px;border-radius:999px;background:{C['amber']};color:#1A1030}}
#cta{{z-index:5;background:radial-gradient(110% 60% at 80% 0%, #4A28C8 0%, #2A1470 35%, transparent 70%),radial-gradient(80% 50% at 0% 100%, #3A1BA8 0%, transparent 60%), #0E0822}}
#cta .semcc{{font-size:38px;font-weight:800;color:{C['gain']};margin-top:-20px}}
"""
    js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f};
function vis(id,t,a,b,fi=.2,fo=.2){{ const o=cl((t-a)/fi)*(1-cl((t-(b-fo))/fo)); $(id).style.opacity=o; return o; }}
function kb(id,t,a,b,z0,z1,y0,y1,x0=0,x1=0){{ const k=ease(cl((t-a)/Math.max(.1,b-a))*.999); $(id).querySelector('.w').style.transform=`translate(${{lerp(x0,x1,k)}}px,${{lerp(y0,y1,k)}}px) scale(${{lerp(z0,z1,k)}})`; }}
window.R=async function(t){{
  const N=[1,2,3,4,5,6].map(i=>S['N'+i]);
  const [n1a,n1b]=N[0],[n2a,n2b]=N[1],[n3a,n3b]=N[2],[n4a,n4b]=N[3],[n5a,n5b]=N[4],[n6a]=N[5];
  const q2=U['N2.2']||(n2a+3), lembra=U['N5.2']||(n5a+1.3), volta=U['N5.3']||(n5a+2.4);
  // cenas
  vis('sc_mesa',t,-1,n3a+.05,.01,.25);   kb('sc_mesa',t,0,n3a,1.02,1.14,0,-40);
  const dm=ease((t-(q2-.2))/.6); $('sc_mesa').querySelector('img').style.filter=`brightness(${{1-.45*dm}}) saturate(${{1-.5*dm}})`;
  vis('sc_rua',t,n3a-.2,lembra+.1,.25,.2); kb('sc_rua',t,n3a,n5a,1.0,1.16,0,-60,0,40);
  const tl=cl((t-(n4a+.15))/.15); $('tela').style.opacity=tl;
  $('tela').style.boxShadow=`0 0 ${{60*tl*(.7+.3*Math.sin(t*7))}}px rgba(37,211,102,.8)`;
  vis('sc_volta',t,lembra-.1,n6a+.6,.2,.3); kb('sc_volta',t,lembra,T,1.06,1.18,0,30);
  // escurece a rua quando entra o cartão do "faltam 2"
  const rd=ease((t-(n5a-.1))/.4); $('sc_rua').querySelector('img').style.filter=`blur(${{rd*10}}px) brightness(${{1-.45*rd}})`;
  // legendas
  const h=ease((t-.05)/.4); $('hook').style.opacity=h*(1-cl((t-(n2a-.2))/.2)); $('hook').style.transform=`translateY(${{(1-h)*40}}px)`;
  show('c2',t,n2a,q2); show('c2b',t,q2,n3a-.05); show('c3',t,n3a,n4a-.1); show('c4',t,n4a-.1,n5a-.05);
  const fa=back((t-n5a)/.45); $('c5a').style.opacity=cl((t-n5a)/.12)*(1-cl((t-(lembra-.15))/.15)); $('c5a').style.transform=`scale(${{fa}})`;
  show('c5b',t,lembra,n6a-.05);
  // calendário: última visita no dia 3, depois os dias vão ficando vazios até 23 dias
  const ci=back((t-(n2a+.3))/.5), co=cl((t-(n3a-.3))/.3);
  $('cal').style.opacity=cl((t-(n2a+.3))/.15)*(1-co); $('cal').style.transform=`translateY(${{(1-ci)*140}}px)`;
  const prog=cl((t-(n2a+.9))/(n3a-.6-(n2a+.9)));
  const dd=Math.round(prog*23);
  for(let k=0;k<28;k++){{ const e=$('d'+k); e.className = k<3 ? 'v' : (k-3<dd ? 'x' : ''); }}
  $('cnt').textContent = dd + (dd===1?' dia':' dias');
  // aviso real no WhatsApp
  const wq=n4a+.5, wk=back((t-wq)/.5), wo=cl((t-(n5a-.25))/.3);
  $('wa').style.opacity=cl((t-wq)/.15)*(1-wo); $('wa').style.transform=`translateY(${{(1-wk)*-140}}px) scale(${{.95+.05*wk}})`;
  // cartão 8/10 com as duas casas vazias pulsando
  const ki=back((t-(n5a+.1))/.45), ko=cl((t-(volta-.1))/.25);
  $('card').style.opacity=cl((t-(n5a+.1))/.15)*(1-ko); $('card').style.transform=`translateY(${{(1-ki)*160}}px)`;
  const pl=1+.08*Math.max(0,Math.sin((t-n5a)*7));
  ['s8','s9'].forEach(id=>{{ $(id).style.transform=`scale(${{pl}})`; $(id).style.borderColor=`rgba(255,194,77,${{.6+.4*Math.max(0,Math.sin((t-n5a)*7))}})`; }});
  const ck=cta(t,n6a); $('top').style.opacity=1-ck;
  await Promise.all([...document.images].map(i=>i.decode().catch(()=>{{}})));
}};
"""
    return page(body, css, js), total


if __name__ == "__main__":
    main(build, "reel_14_cliente_some.mp4", sys.argv)
