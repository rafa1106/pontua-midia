# -*- coding: utf-8 -*-
"""Reel 06 — "Conheça seus clientes" (fluxo 07: lista, aviso de sumidos e ficha da cliente no Studio da Vila).

Uso: python3 reel_clientes.py <pasta> [preview t1,t2,...]
  <pasta>/fl  quadros do lojista.mp4 (computador, 1200 px) com realce local
  <pasta>/audio/narracao.mp3 + alinhamento.json
"""
import json, sys
from reel_base import *

WW = 1000
VH0 = round(WW * 900 / 1440)
VH = round(VH0 * 1.19)          # recorte limpo: só sai a barra lateral
WT = 540
LW, LH = 920, 300               # lupa


def build(work):
    S, U, total = marcas(work)
    fl = (work / "fl").as_uri()
    nfl = len(list((work / "fl").glob("*.jpg")))
    body = f"""{BG}{TOP}
<div class="cap" id="hook">
  <div class="l" id="h1">Quem são os seus<br>clientes <span class="hl">de verdade?</span></div>
  <div class="l" id="h2" style="margin-top:40px"><span class="am">E quem sumiu?</span></div>
</div>

<div class="cap step" id="c2"><span class="n">1</span><div>Seus clientes<br><span class="hl">num lugar só</span></div></div>
<div class="cap step" id="c3"><span class="n">2</span><div>Aviso de quem<br><span class="am">sumiu há 30+ dias</span></div></div>
<div class="cap step" id="c4"><span class="n">3</span><div>A ficha<br><span class="hl">de cada cliente</span></div></div>

<div id="win">
  <div class="bar"><i></i><i></i><i></i><span class="url">🔒 pontua.club</span></div>
  <div class="vp"><img id="sw" src="{fl}/0001.jpg"></div>
</div>
<div id="lens"><img id="sl" src="{fl}/0001.jpg"><div id="ltag">clientes</div><div id="lring"></div></div>

<div id="base">
  <div class="b1">Uma base que é <span class="am">sua.</span></div>
  <div class="b2">Não da rede social.</div>
</div>
{CTA}"""
    css = f"""
#hook{{top:560px}}
#win{{position:absolute;left:{(W-WW)//2}px;top:{WT}px;width:{WW}px;border-radius:26px;overflow:hidden;background:#0F1220;opacity:0;
  box-shadow:0 0 0 2px rgba(183,156,255,.45),0 0 110px rgba(123,77,255,.5),0 50px 90px rgba(0,0,0,.6);transform-origin:50% 0}}
#win .bar{{height:58px;background:#1C1A30;display:flex;align-items:center;gap:12px;padding:0 22px}}
#win .bar i{{width:16px;height:16px;border-radius:50%;background:#3C3760}}
#win .url{{margin-left:22px;flex:1;height:36px;border-radius:12px;background:#0F0D1E;color:#B9B2D9;font-size:22px;display:flex;align-items:center;padding-left:18px}}
#win .vp{{position:relative;width:{WW}px;height:{VH}px;overflow:hidden}}
#win .vp img{{position:absolute;left:0;top:0;width:{WW}px;height:{VH0}px;transform-origin:0 0}}
#lens{{position:absolute;left:0;right:0;margin:auto;top:1170px;width:{LW}px;height:{LH}px;border-radius:30px;overflow:hidden;background:#0F1220;opacity:0;
  border:4px solid {C['amber']};box-shadow:0 30px 80px rgba(0,0,0,.6),0 0 70px rgba(255,194,77,.45);transform-origin:50% 0}}
#lens img{{position:absolute;left:0;top:0;transform-origin:0 0}}
#ltag{{position:absolute;left:20px;top:16px;padding:10px 22px;border-radius:999px;background:rgba(13,10,24,.85);border:1.5px solid rgba(183,156,255,.45);
  font-size:26px;font-weight:900;color:{C['amber']};text-transform:uppercase;letter-spacing:.12em}}
#lring{{position:absolute;border-radius:16px;border:4px solid {C['amber']};box-shadow:0 0 30px rgba(255,194,77,.7);opacity:0}}
#base{{position:absolute;left:60px;right:60px;top:720px;text-align:center;opacity:0}}
#base .b1{{font-size:96px;font-weight:900;letter-spacing:-.045em;line-height:1.05}}
#base .b2{{font-size:64px;font-weight:800;letter-spacing:-.03em;margin-top:30px;color:#E6E0FF}}
"""
    js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f}, FL="{fl}", NFL={nfl};
const VW={WW}, VH={VH}, VH0={VH0}, LW={LW}, LH={LH};
function zoomW(el,fx,fy,z){{ const tx=cl(VW/2-fx*VW*z,VW-VW*z,0), ty=cl(VH/2-fy*VH0*z,VH-VH0*z,0); el.style.transform=`translate(${{tx}}px,${{ty}}px) scale(${{z}})`; }}
function kf(K,t){{ let i=1; while(i<K.length-1 && t>K[i][0]) i++; const [a,fa]=K[i-1],[b,fb]=K[i];
  const k=ease((t-a)/Math.max(.01,b-a)); return fa.map((v,j)=>v+(fb[j]-v)*k); }}
window.R=async function(t){{
  const [n1a,n1b]=S.N1,[n2a,n2b]=S.N2,[n3a,n3b]=S.N3,[n4a,n4b]=S.N4,[n5a,n5b]=S.N5,[n6a,n6b]=S.N6;
  const ps=[], q=U['N1.2'];
  // gancho
  const h1=ease((t-(n1a-.05))/.45), h2=back((t-(q-.05))/.45);
  $('h1').style.cssText=`opacity:${{h1}};transform:translateY(${{(1-h1)*40}}px)`;
  $('h2').style.cssText=`opacity:${{cl((t-(q-.05))/.15)}};transform:scale(${{h2}})`;
  const ho=cl((t-(n2a-.45))/.35); $('hook').style.opacity=1-ho; $('hook').style.transform=`translateY(${{-ho*60}}px)`;
  const ck=cta(t,n6a);
  $('top').style.opacity=1-ck;
  // janela (N2–N4) e frase final (N5)
  const win=ease((t-(n2a-.25))/.55), wout=ease((t-(n5a-.2))/.45);
  $('win').style.opacity=win*(1-wout); $('win').style.transform=`translateY(${{(1-win)*700}}px) scale(${{1-wout*.08}})`;
  const lin=back((t-(n2a+.5))/.5), lo=cl((t-(n5a-.25))/.25);
  $('lens').style.opacity=cl((t-(n2a+.5))/.15)*(1-lo); $('lens').style.transform=`scale(${{.85+.15*lin}})`;
  const b=ease((t-(n5a+.05))/.45), bo=cl((t-(n6a-.3))/.3);
  $('base').style.opacity=b*(1-bo); $('base').style.transform=`translateY(${{(1-b)*40}}px)`;
  // tempo da gravação: lista (N2), aviso (N3), ficha → campanhas → prêmios → histórico (N4), sem passar pelas transições
  const d4=n4b-n4a, f1=n4a, f2=n4a+.25*d4, f3=n4a+.5*d4, f4=n4a+.74*d4;
  const vt=pw([[n2a,.8],[n3a,3.4],[n3b,5.0],
              [f1-.01,5.0],[f1,21.6],[f2-.01,24.4],[f2,25.4],[f3-.01,27.4],[f3,28.2],[f4-.01,30.2],[f4,31.0],[n4b+.3,34.6],[T,34.6]],t);
  setImg($('sw'),`${{FL}}/${{pad(Math.min(NFL,Math.max(1,Math.round(vt*30)+1)))}}.jpg`,ps);
  zoomW($('sw'),.58,.5,1.19);
  setImg($('sl'),$('sw').src,ps);
  // lupa: [x,y,zoom] por trecho
  const tc=U['N3.1']||n3a;
  let L, tag;
  if(t<n3a){{ L=[.42,.56,1.6]; tag='clientes'; }}
  else if(t<n4a){{ const k=ease((t-(n3a+.4*(n3b-n3a)))/.6); L=[.43+.39*k,.24,2.0]; tag='sumidos há 30+ dias'; }}
  else if(t<f2){{ L=[.59,.45,1.25]; tag='visão geral'; }}
  else if(t<f3){{ L=[.59,.44,1.2]; tag='campanhas'; }}
  else if(t<f4){{ L=[.59,.55,1.2]; tag='prêmios'; }}
  else {{ L=[.42,lerp(.55,.24,(t-f4)/Math.max(.1,n4b-f4)),1.55]; tag='histórico'; }}
  const [lx,ly,lz]=L, lw=VW*lz, lh=VH0*lz;
  $('sl').style.width=lw+'px'; $('sl').style.height=lh+'px';
  const ox=cl(LW/2-lx*lw,LW-lw,0), oy=cl(LH/2-ly*lh,LH-lh,0);
  $('sl').style.transform=`translate(${{ox}}px,${{oy}}px)`;
  $('ltag').textContent=tag;
  // destaque no botão "Chamar de volta" (região .86–.97 × .225–.26 da tela)
  const bk=io(t,n3a+.4*(n3b-n3a)+.6,n4a-.05,.25,.2);
  $('lring').style.cssText=`opacity:${{bk}};left:${{ox+.855*lw}}px;top:${{oy+.215*lh}}px;width:${{.12*lw}}px;height:${{.055*lh}}px`;
  // legendas
  show('c2',t,n2a,n3a); show('c3',t,n3a,n4a); show('c4',t,n4a,n5a-.2);
  await Promise.all(ps);
}};
"""
    return page(body, css, js), total


if __name__ == "__main__":
    main(build, "reel_06_clientes.mp4", sys.argv)
