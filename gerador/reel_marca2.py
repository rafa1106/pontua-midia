# -*- coding: utf-8 -*-
"""Reel 05 v3 — "Cartão com a cara do seu negócio": tema + logo (fluxo 09) + imagem de fundo e ícone próprio (fluxo 09b).

Uso: python3 reel_marca2.py <pasta> [preview t1,t2,...]
  <pasta>/fl, fc    quadros do fluxo 09 (lojista 1200 px / cliente 620 px) com realce
  <pasta>/fl2, fc2  quadros do fluxo 09b
  <pasta>/assets/fundo.jpg, icone.png  arquivos que a lojista enviou na gravação
  <pasta>/audio/narracao.mp3 + alinhamento.json (7 falas)
"""
import json, sys
from reel_base import *

PW = 600
SW = PW - 32
SH = round(SW * 2532 / 1170)
PT = 470
WW = 1000
VH0 = round(WW * 900 / 1440)
VH = round(VH0 * 1.19)
WT = 540
LW, LH = 760, 470


def build(work):
    S, U, total = marcas(work)
    u = {k: (work / k).as_uri() for k in ("fl", "fc", "fl2", "fc2", "assets")}
    n = {k: len(list((work / k).glob("*.jpg"))) for k in ("fl", "fc", "fl2", "fc2")}
    cta_html = CTA
    body = f"""{BG}{TOP}
<div class="cap" id="hook">
  <div class="l" id="h1">Seu cartão com<br>a <span class="am">cara do seu</span><br><span class="am">negócio</span></div>
</div>

<div class="cap step" id="c2"><span class="n">1</span><div>Escolhe o tema<br><span class="hl">e vê a prévia</span></div></div>
<div class="cap step" id="c3"><span class="n">2</span><div>Coloca<br><span class="hl">o seu logo</span></div></div>
<div class="cap step" id="c4"><span class="n">3</span><div>Sua imagem de fundo<br><span class="am">e ícone próprio</span></div></div>
<div class="cap step" id="c5"><span class="n">✓</span><div>No celular<br><span class="hl">da cliente</span></div></div>
<div class="cap step" id="c6"><span class="n">★</span><div>Cartão<br><span class="am">personalizado</span></div></div>

<div id="win">
  <div class="bar"><i></i><i></i><i></i><span class="url">🔒 pontua.club</span></div>
  <div class="vp"><img id="sw" src="{u['fl']}/0001.jpg"></div>
</div>
<div id="lens"><img id="sl" src="{u['fl']}/0001.jpg"><div id="tema"><span>tema</span><b id="tn">Rose</b></div><div id="ltag">logo</div></div>

<div class="file" id="ff"><img src="{u['assets']}/fundo.jpg"><div><b>fundo_studio.jpg</b><small>imagem de fundo</small></div></div>
<div class="file" id="fi"><img src="{u['assets']}/icone.png" class="ic"><div><b>icone_escova.png</b><small>ícone do carimbo</small></div></div>

<div id="phone"><div class="scr"><img id="sa" src="{u['fc']}/0078.jpg"><img id="sd" src="{u['fc2']}/0740.jpg"><div id="wipe"></div></div><div id="ring"></div></div>
<div id="who">antes</div>

<div class="badge" id="logo" style="left:0;right:0;margin:auto;width:max-content;top:1490px">✓ Logo enviado</div>
<div id="plano"><div class="p1">Disponível a partir do</div><div class="p2">Plano Basic</div><div class="p3">R$ 39/mês</div></div>
{cta_html}"""
    css = f"""
#hook{{top:600px}}
#win{{position:absolute;left:{(W-WW)//2}px;top:{WT}px;width:{WW}px;border-radius:26px;overflow:hidden;background:#0F1220;opacity:0;
  box-shadow:0 0 0 2px rgba(183,156,255,.45),0 0 110px rgba(123,77,255,.5),0 50px 90px rgba(0,0,0,.6);transform-origin:50% 0}}
#win .bar{{height:58px;background:#1C1A30;display:flex;align-items:center;gap:12px;padding:0 22px}}
#win .bar i{{width:16px;height:16px;border-radius:50%;background:#3C3760}}
#win .url{{margin-left:22px;flex:1;height:36px;border-radius:12px;background:#0F0D1E;color:#B9B2D9;font-size:22px;display:flex;align-items:center;padding-left:18px}}
#win .vp{{position:relative;width:{WW}px;height:{VH}px;overflow:hidden}}
#win .vp img{{position:absolute;left:0;top:0;width:{WW}px;height:{VH0}px;transform-origin:0 0}}
#lens{{position:absolute;left:0;right:0;margin:auto;top:1120px;width:{LW}px;height:{LH}px;border-radius:30px;overflow:hidden;background:#0F1220;opacity:0;
  border:4px solid {C['amber']};box-shadow:0 30px 80px rgba(0,0,0,.6),0 0 70px rgba(255,194,77,.45);transform-origin:50% 0}}
#lens img{{position:absolute;left:0;top:0;transform-origin:0 0}}
#tema,#ltag{{position:absolute;left:22px;top:20px;display:flex;align-items:center;gap:14px;padding:12px 24px;border-radius:999px;
  background:rgba(13,10,24,.82);border:1.5px solid rgba(183,156,255,.45)}}
#ltag{{font-size:30px;font-weight:900;color:{C['amber']};text-transform:uppercase;letter-spacing:.12em;opacity:0}}
#tema span{{font-size:24px;color:{C['muted']};font-weight:600;text-transform:uppercase;letter-spacing:.12em}}
#tema b{{font-size:40px;font-weight:900;letter-spacing:-.02em}}
.file{{position:absolute;display:flex;align-items:center;gap:20px;padding:18px 26px 18px 18px;border-radius:24px;background:#F5F2FF;color:#141024;
  box-shadow:0 24px 60px rgba(0,0,0,.55),0 0 50px rgba(155,120,255,.45);opacity:0;white-space:nowrap}}
.file img{{width:150px;height:84px;object-fit:cover;border-radius:12px}}
.file img.ic{{width:84px;height:84px;object-fit:contain}}
.file b{{display:block;font-size:30px;font-weight:800}} .file small{{display:block;font-size:24px;color:#5B5473;font-weight:600;margin-top:4px}}
#phone{{position:absolute;left:{(W-PW)//2}px;top:{PT}px;width:{PW}px;height:{SH + 32}px;border-radius:78px;padding:16px;
  background:linear-gradient(145deg,#352B66,#120D26);box-shadow:0 0 0 2px rgba(183,156,255,.5),0 0 110px rgba(123,77,255,.55),0 50px 90px rgba(0,0,0,.6);
  transform-origin:50% 30%}}
.scr{{width:100%;height:100%;border-radius:62px;overflow:hidden;position:relative;background:#1A1E2C}}
.scr img{{position:absolute;left:0;top:0;width:{SW}px;height:{SH}px;transform-origin:0 0}}
#wipe{{position:absolute;top:0;bottom:0;width:10px;background:linear-gradient(90deg,transparent,#fff,transparent);box-shadow:0 0 40px #FFD777;opacity:0}}
#who{{position:absolute;left:0;right:0;top:{PT + SH + 32 + 22}px;text-align:center;font-size:32px;font-weight:800;color:{C['muted']};letter-spacing:.14em;text-transform:uppercase}}
#ring{{position:absolute;border-radius:26px;border:5px solid {C['amber']};box-shadow:0 0 36px rgba(255,194,77,.65);opacity:0}}
#plano{{position:absolute;right:36px;top:1420px;padding:30px 40px;border-radius:30px;background:linear-gradient(135deg,{C['violet2']},{C['violet']});
  box-shadow:0 20px 60px rgba(0,0,0,.45),0 0 70px rgba(123,77,255,.7);text-align:center;opacity:0}}
#plano .p1{{font-size:26px;font-weight:600;color:#E6E0FF}} #plano .p2{{font-size:56px;font-weight:900;letter-spacing:-.03em;margin-top:4px}}
#plano .p3{{font-size:32px;font-weight:800;color:{C['amber']};margin-top:2px}}
"""
    js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f}, UR={json.dumps(u)}, NF={json.dumps(n)};
const SW={SW}, SH={SH}, VW={WW}, VH={VH}, VH0={VH0}, LW={LW}, LH={LH};
function zoomP(el,fx,fy,z){{ const tx=cl(SW/2-fx*SW*z,SW-SW*z,0), ty=cl(SH/2-fy*SH*z,SH-SH*z,0); el.style.transform=`translate(${{tx}}px,${{ty}}px) scale(${{z}})`; return ty; }}
function zoomW(el,fx,fy,z){{ const tx=cl(VW/2-fx*VW*z,VW-VW*z,0), ty=cl(VH/2-fy*VH0*z,VH-VH0*z,0); el.style.transform=`translate(${{tx}}px,${{ty}}px) scale(${{z}})`; }}
function kf(K,t){{ let i=1; while(i<K.length-1 && t>K[i][0]) i++; const [a,fa]=K[i-1],[b,fb]=K[i];
  const k=ease((t-a)/Math.max(.01,b-a)); return [0,1,2].map(j=>fa[j]+(fb[j]-fa[j])*k); }}
const fr=(src,vt)=>`${{UR[src]}}/${{pad(Math.min(NF[src],Math.max(1,Math.round(vt*30)+1)))}}.jpg`;
// arquivo "voando" para dentro da janela: sai de baixo, pousa sobre a área de envio e some
function voa(id,t,t0,y0,y1){{ const e=$(id), k=ease((t-t0)/.45), o=cl((t-t0)/.12)*(1-cl((t-(t0+.65))/.22));
  e.style.opacity=o; e.style.left='0'; e.style.right='0'; e.style.margin='auto'; e.style.width='max-content';
  e.style.top=`${{y0+(y1-y0)*k}}px`; e.style.transform=`scale(${{1-.45*cl((t-(t0+.55))/.32)}}) rotate(${{(1-k)*-6}}deg)`; }}
window.R=async function(t){{
  const [n1a,n1b]=S.N1,[n2a,n2b]=S.N2,[n3a,n3b]=S.N3,[n4a,n4b]=S.N4,[n5a,n5b]=S.N5,[n6a,n6b]=S.N6,[n7a,n7b]=S.N7;
  const d4=n4b-n4a, tF=n4a+.12*d4, tI=n4a+.55*d4;   // fundo e ícone (no ritmo da fala)
  const ps=[];
  // gancho
  const h1=ease((t-(n1a-.05))/.5);
  $('h1').style.cssText=`opacity:${{h1}};transform:translateY(${{(1-h1)*40}}px)`;
  const ho=cl((t-(n1b-1.3))/.35); $('hook').style.opacity=1-ho; $('hook').style.transform=`translateY(${{-ho*60}}px)`;
  const ck=cta(t,n7a);
  $('top').style.opacity=1-ck;
  // celular: ANTES (fim do N1); volta no N5 com DEPOIS
  const pin=ease((t-(n1b-1.05))/.6), pout=ease((t-(n2a-.1))/.45), pback=ease((t-(n5a-.62))/.5);
  const pv = t<n5a-.62 ? pin*(1-pout) : pback*(1-ck);
  const px = t<n5a-.62 ? -pout*900 : (1-pback)*900;
  $('phone').style.opacity=pv; $('who').style.opacity=pv;
  $('phone').style.transform=`translate(${{px}}px,${{t<n2a?(1-pin)*700:0}}px) scale(${{1-ck*.1}})`;
  // janela do painel (N2–N4)
  const win=ease((t-(n2a-.15))/.5), wout=ease((t-(n5a-.62))/.5);
  $('win').style.opacity=win*(1-wout); $('win').style.transform=`translate(${{(1-win)*900-wout*900}}px,0)`;
  const ln=back((t-(n2a+.45))/.5), lo=cl((t-(n5a-.62))/.25);
  $('lens').style.opacity=cl((t-(n2a+.45))/.15)*(1-lo); $('lens').style.transform=`scale(${{.85+.15*ln}})`;
  // qual gravação: 09 (tema e logo) até o N4; 09b (fundo e ícone) no N4
  const B = t>=n4a-.05;
  let vt, src;
  if(!B){{ src='fl'; vt=pw([[n2a,3.0],[n2a+.7,5.0],[n2a+.8,5.5],[n2a+1.55,7.5],[n2a+1.65,8.2],[n2b,11.6],[n3a,12.4],[n3a+.45,15.0],[n3a+.5,15.8],[n3b,17.4]],t); }}
  else {{ src='fl2'; vt=pw([[n4a,4.0],[tF+.45,5.7],[tF+.6,6.6],[tI+.35,10.6],[tI+.6,11.6],[n4b,14.0],[T,14.0]],t); }}
  setImg($('sw'),fr(src,vt),ps);
  zoomW($('sw'),.58,.5,1.19);
  setImg($('sl'),$('sw').src,ps);
  const modo = B?'img':(vt<12.1?'tema':'logo');
  $('tema').style.opacity = modo=='tema'?1:0; $('ltag').style.opacity = modo=='tema'?0:1;
  $('ltag').textContent = modo=='logo'?'logo':(t<tI-.4?'imagem de fundo':'ícone do carimbo');
  const [lx,ly,lz] = modo=='logo'?[.30,.425,3.0]:[.815,.47,2.32];
  const LHc = modo=='logo'?330:LH; $('lens').style.height=LHc+'px';
  const lw=VW*lz, lh=VH0*lz; $('sl').style.width=lw+'px'; $('sl').style.height=lh+'px';
  $('sl').style.transform=`translate(${{cl(LW/2-lx*lw,LW-lw,0)}}px,${{cl(LHc/2-ly*lh,LHc-lh,0)}}px)`;
  $('tn').textContent = vt<5.2?'Rose':(vt<7.8?'Escuro':'Dourado');
  $('tn').style.color = vt<5.2?'#FF5FA2':(vt<7.8?'#C9C4E6':'#FFC24D');
  pop('logo',t,n3a+.5,n4a-.05,-2);
  // arquivos enviados (os mesmos da gravação)
  voa('ff',t,tF-.4,1760,1290); voa('fi',t,tI-.4,1760,1290);
  // antes → depois (cortina): antes = cartão rose sem logo; depois = fundo + ícone + logo
  const wk=ease((t-(n5a+.35))/.9);
  $('sd').style.clipPath=`inset(0 ${{(1-wk)*100}}% 0 0)`;
  $('wipe').style.left=`${{wk*SW-5}}px`; $('wipe').style.opacity=(wk>0&&wk<1)?1:0;
  $('who').textContent = (t>n5a+.8)?'depois':'antes';
  $('who').style.color = (t>n5a+.8)?'#FFC24D':'{C['muted']}';
  setImg($('sd'),fr('fc2',pw([[n5a,24.6],[T,26.2]],t)),ps);
  const fz=kf([[0,[.5,.26,1.08]],[n5a+1.3,[.5,.26,1.08]],[n5a+2.0,[.5,.3,1.12]],[T,[.5,.3,1.12]]],t);
  zoomP($('sa'),...fz); const ty=zoomP($('sd'),...fz);
  const rg=io(t,n5a+1.5,n7a-.1,.3,.25);
  $('ring').style.cssText=`opacity:${{rg}};left:36px;right:36px;top:${{16+ty+.065*SH*fz[2]}}px;height:${{.5*SH*fz[2]}}px`;
  // legendas
  show('c2',t,n2a,n3a); show('c3',t,n3a,n4a); show('c4',t,n4a,n5a-.1); show('c5',t,n5a-.1,n6a); show('c6',t,n6a,n7a-.1);
  // plano
  const pl=back((t-(n6a+.3))/.5), plo=cl((t-(n7a-.35))/.25);
  $('plano').style.opacity=cl((t-(n6a+.3))/.15)*(1-plo); $('plano').style.transform=`scale(${{pl}}) rotate(-3deg)`;
  await Promise.all(ps);
}};
"""
    return page(body, css, js), total


if __name__ == "__main__":
    main(build, "reel_05_cartao_marca_v3.mp4", sys.argv)
