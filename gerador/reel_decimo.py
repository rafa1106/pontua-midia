# -*- coding: utf-8 -*-
"""Reel 17 — "POV: o décimo café chegou" (série Do lado do cliente, viés pico-fim).

Cenas por IA (pedido no balcão, entrega do café, o café nas mãos) + duas telas reais do cliente (fluxo 04 do
material bruto: 9 de 10 → cartão completo com a recompensa disponível; a data de validade foi coberta para o vídeo
ficar atemporal) + o aviso real de cartão completo no WhatsApp.

Uso: python3 reel_decimo.py <pasta> [preview t1,t2,...]   <pasta>/audio (reels/17_pov_decimo)
"""
import json, sys
from pathlib import Path
from reel_base import *
from reel_papel import CTA_GRATIS

CENAS = Path(__file__).parent / "cenas"
PWD = 800                      # largura do painel com a tela real
K = PWD / 620                  # escala da tela (quadros de 620 px)
PX, PY = (W - PWD) // 2, 520   # canto do painel
SLOT10 = (473, 462)            # centro do 10º círculo na tela A (px da tela)
ROW = (775, 860)               # faixa "1 café grátis · DISPONÍVEL" na tela B

MSG = ("Olá, Ricardo Martins!<br><br>Seu cartão da Café da Esquina foi <b>completado com sucesso.</b><br><br>"
       "Toque em “Ver opções” para consultar os próximos passos.")


def build(work):
    S, U, total = marcas(work)
    c = {k: (CENAS / f).as_uri() for k, f in (("ped", "r17_pedido.png"), ("ent", "r17_entrega.png"), ("mom", "r17_momento.png"))}
    ta, tb = (CENAS / "r17_tela_a.png").as_uri(), (CENAS / "r17_tela_b.png").as_uri()
    scenes = "".join(f'<div class="sc" id="sc_{k}"><img src="{v}"></div>' for k, v in c.items())
    body = f"""<div id="bg"></div>
{scenes}
<div id="blur"></div><div id="shade"></div><div id="flash"></div>
{TOP}
<div class="cap" id="hook"><div class="pov">POV:</div><div class="l">o décimo café<br><span class="am">chegou.</span></div></div>
<div class="chip" id="falta">faltava 1 ☕</div>
<div class="cap step" id="c2"><span class="n">☕</span><div>O de sempre,<br><span class="hl">último carimbo</span></div></div>
<div class="cap step" id="c3"><span class="n wa">{WA_ICON}</span><div>Cartão completo,<br><span class="hl">no WhatsApp</span></div></div>
<div class="cap step" id="c4"><span class="n">🎁</span><div>O prêmio<br><span class="hl">já está lá</span></div></div>
<div class="cap" id="c4b"><div class="l mid">Esse é por<br><span class="am">conta da casa.</span></div></div>
<div class="cap" id="c5"><div class="l mid" id="c5a">É desse momento<br>que ele lembra.</div><div class="l mid am" id="c5b">E é por ele<br>que volta.</div></div>
<div id="fonte">efeito pico-fim · Kahneman e colegas, 1993</div>
<div class="cap" id="c6"><div class="l mid">Dê esse momento<br><span class="am">pro seu cliente.</span></div></div>
<div class="pn" id="pa"><img src="{ta}"></div>
<div class="pn" id="pb"><img src="{tb}"><div id="ring"></div></div>
<div id="tela">tela real do cliente</div>
<div id="plus">+1</div>
{wa_card("wa", "Café da Esquina", MSG, ("Ver opções",), top=560)}
{CTA_GRATIS}"""
    css = f"""
#bg{{position:absolute;inset:0;background:#0B0816}}
.sc{{position:absolute;inset:0;overflow:hidden;opacity:0}}
.sc img{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;transform-origin:50% 50%}}
#blur{{position:absolute;inset:0;backdrop-filter:blur(14px) brightness(.55);-webkit-backdrop-filter:blur(14px) brightness(.55);opacity:0}}
#shade{{position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,rgba(8,5,20,.9) 0%,rgba(8,5,20,.62) 26%,rgba(8,5,20,.25) 36%,rgba(8,5,20,0) 46%,rgba(8,5,20,0) 62%,rgba(8,5,20,.7) 100%)}}
#flash{{position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none;z-index:6}}
#top{{z-index:3}} .cap{{z-index:3}}
.cap .l{{font-size:112px;line-height:1.02;text-shadow:0 4px 18px rgba(0,0,0,.85),0 6px 50px rgba(0,0,0,.6)}}
.cap .l.mid{{font-size:88px}}
#hook{{top:230px}} #hook .pov{{font-size:64px;font-weight:900;color:{C['amber']};letter-spacing:.04em;margin-bottom:6px;text-shadow:0 4px 18px rgba(0,0,0,.8)}}
#c2,#c3,#c4{{top:240px}} #c2 div,#c3 div,#c4 div{{font-size:58px}}
#c4b,#c5,#c6{{top:250px}}
#c5 .l{{position:absolute;left:0;right:0}} #c5b{{top:210px}}
#falta{{left:0;right:0;margin:auto;width:max-content;top:690px;z-index:3}}
.pn{{position:absolute;left:{PX}px;top:{PY}px;width:{PWD}px;border-radius:34px;overflow:hidden;z-index:2;opacity:0;
  box-shadow:0 0 0 2px rgba(183,156,255,.45),0 0 110px rgba(123,77,255,.5),0 40px 90px rgba(0,0,0,.6)}}
.pn img{{display:block;width:100%}}
#ring{{position:absolute;left:{round(52 * K)}px;right:{round(52 * K)}px;top:{round((ROW[0] - 10) * K)}px;height:{round((ROW[1] - ROW[0] + 20) * K)}px;
  border-radius:26px;border:6px solid {C['amber']};box-shadow:0 0 40px rgba(255,194,77,.75);opacity:0}}
#tela{{position:absolute;left:0;right:0;text-align:center;z-index:3;font-size:28px;font-weight:700;color:rgba(230,224,255,.75);opacity:0}}
#plus{{position:absolute;left:0;top:0;width:200px;height:200px;border-radius:50%;z-index:4;display:flex;align-items:center;justify-content:center;
  background:radial-gradient(circle,#FFD777 0%,#FFC24D 55%,#E8A020 100%);color:#1A1030;font-size:86px;font-weight:900;opacity:0;
  box-shadow:0 20px 70px rgba(255,194,77,.6)}}
#wa{{z-index:4;box-shadow:0 30px 80px rgba(0,0,0,.55),0 0 90px rgba(37,211,102,.35)}}
#wa .tx b{{background:#FFF1C9}}
#fonte{{position:absolute;left:0;right:0;top:1580px;text-align:center;z-index:3;font-size:26px;font-weight:600;color:rgba(230,224,255,.7);opacity:0}}
#cta{{z-index:5;background:radial-gradient(110% 60% at 80% 0%, #4A28C8 0%, #2A1470 35%, transparent 70%),radial-gradient(80% 50% at 0% 100%, #3A1BA8 0%, transparent 60%), #0E0822}}
#cta .semcc{{font-size:38px;font-weight:800;color:{C['gain']};margin-top:-20px}}
"""
    js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f}, W={W}, K={K}, PX={PX}, PY={PY}, SL={json.dumps(SLOT10)};
function vis(id,t,a,b,fi=.2,fo=.2){{ const o=cl((t-a)/fi)*(1-cl((t-(b-fo))/fo)); $(id).style.opacity=o; return o; }}
function kb(id,t,a,b,z0,z1,y0,y1){{ const k=cl((t-a)/Math.max(.1,b-a)); $(id).querySelector('img').style.transform=`translateY(${{lerp(y0,y1,k)}}px) scale(${{lerp(z0,z1,k)}})`; }}
window.R=async function(t){{
  const N=[1,2,3,4,5,6].map(i=>S['N'+i]);
  const [n1a,n1b]=N[0],[n2a,n2b]=N[1],[n3a,n3b]=N[2],[n4a,n4b]=N[3],[n5a,n5b]=N[4],[n6a]=N[5];
  const n4m=n4a+.52*(n4b-n4a), n5m=U['N5.2']||(n5a+.55*(n5b-n5a)), ctaT=U['N6.2']||(n6a+2);
  // cenas: pedido (N1–N3, desfocado sob as telas), entrega (2ª metade da N4), café nas mãos (N5–N6)
  vis('sc_ped',t,-1,n4m+.05,.01,.2); kb('sc_ped',t,0,n4m,1.04,1.2,0,-40);
  vis('sc_ent',t,n4m-.1,n5a+.05,.2,.15); kb('sc_ent',t,n4m,n5a,1.12,1.02,-20,10);
  vis('sc_mom',t,n5a-.05,ctaT+.3,.15,.3); kb('sc_mom',t,n5a,T,1.02,1.14,0,-30);
  $('blur').style.opacity=cl((t-(n2a-.1))/.35)*(1-cl((t-(n4m-.3))/.3));
  $('flash').style.opacity=.3*Math.max(0,...[n4m,n5a].map(x=>1-Math.abs(t-x)/.09));
  // gancho
  const h=ease((t-.05)/.4); $('hook').style.opacity=h*(1-cl((t-(n2a-.2))/.2)); $('hook').style.transform=`translateY(${{(1-h)*40}}px)`;
  pop('falta',t,n1a+1.0,n2a-.05,-3);
  // N2: tela real 9/10 + o último carimbo
  show('c2',t,n2a,n3a-.05);
  const pq=n2a+.55*(n2b-n2a), land=pq+.55;
  const ai=ease((t-(n2a+.05))/.5), ao=cl((t-(land+.35))/.12);
  $('pa').style.opacity=cl((t-(n2a+.05))/.2)*(1-ao); $('pa').style.transform=`translateY(${{(1-ai)*500}}px)`;
  const tx=PX+SL[0]*K-100, ty=PY+SL[1]*K-100, pk=ease((t-pq)/.55);
  $('plus').style.opacity=cl((t-pq)/.1)*(1-cl((t-land)/.15));
  $('plus').style.left=lerp(W/2-100,tx,pk)+'px'; $('plus').style.top=lerp(1650,ty,pk)+'px';
  $('plus').style.transform=`scale(${{lerp(1.2,.62,pk)}})`;
  // recarrega como no app: flash branco e a tela já mostra o cartão completo
  $('flash').style.opacity=Math.max(parseFloat($('flash').style.opacity)||0, .9*cl(1-Math.abs(t-(land+.42))/.14));
  const bi=cl((t-(land+.4))/.05), bo=cl((t-(n4m-.35))/.3);
  $('pb').style.opacity=bi*(1-bo); $('pb').style.transform=`translateY(${{bo*-120}}px) scale(${{1-.03*bo}})`;
  // N3: aviso real no WhatsApp (o celular vibra)
  show('c3',t,n3a,n4a-.05);
  const wi=back((t-(n3a+.1))/.5), wo=cl((t-(n4a-.25))/.3), vib=(t>n3a+.1&&t<n3a+.6)?Math.sin(t*90)*8*(1-(t-n3a-.1)/.5):0;
  $('wa').style.opacity=cl((t-(n3a+.1))/.15)*(1-wo);
  $('wa').style.transform=`translate(${{vib}}px,${{(1-wi)*-240-wo*160}}px) scale(${{.96+.04*wi}})`;
  const dim=cl((t-(n3a+.05))/.2)*(1-cl((t-(n4a-.2))/.25)); $('pb').style.filter=`brightness(${{1-.55*dim}})`;
  // N4: a recompensa disponível, depois o café chega
  show('c4',t,n4a,n4m-.1); show('c4b',t,n4m,n5a-.05);
  $('ring').style.opacity=io(t,n4a+.35,n4m-.25,.3,.2);
  $('tela').style.opacity=Math.max(io(t,n2a+.4,land+.3,.3,.15), io(t,land+.5,n4m-.3,.2,.2)*(1-dim));
  const tb=$('pb').getBoundingClientRect(), ta=$('pa').getBoundingClientRect();
  $('tela').style.top=((t<land+.4?ta.bottom:tb.bottom)+18)+'px';
  // N5: pico-fim
  const s5=cl((t-n5a)/.3)*(1-cl((t-(n6a-.25))/.25));
  $('c5').style.opacity=s5;
  const a1=ease((t-n5a)/.35), a2=ease((t-(n5m-.1))/.35);
  $('c5a').style.cssText=`opacity:${{a1}};transform:translateY(${{(1-a1)*30}}px)`;
  $('c5b').style.cssText=`opacity:${{a2}};transform:translateY(${{(1-a2)*30}}px)`;
  $('fonte').style.opacity=io(t,n5a+.6,n6a,.3,.25);
  // N6: fecho e CTA
  show('c6',t,n6a,ctaT);
  const ck=cta(t,ctaT); $('top').style.opacity=1-ck;
  await Promise.all([...document.images].map(i=>i.decode().catch(()=>{{}})));
}};
"""
    return page(body, css, js), total


if __name__ == "__main__":
    main(build, "reel_17_pov_decimo.mp4", sys.argv)
