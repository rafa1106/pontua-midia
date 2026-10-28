# -*- coding: utf-8 -*-
"""Reel 05 — "Cartão com a cara do seu negócio" (fluxo 09: Studio da Vila troca o tema e envia o logo).

Uso: python3 reel_marca.py <pasta> [preview t1,t2,...]
  <pasta>/fl  quadros do lojista.mp4 (computador, 1200 px) com realce
  <pasta>/fc  quadros do cliente.mp4 (celular, 620 px) com realce
  <pasta>/audio/narracao.mp3 + alinhamento.json
"""
import json, sys
from reel_base import *

PW = 600
SW = PW - 32
SH = round(SW * 2532 / 1170)
PT = 470
WW = 1000
VH0 = round(WW * 900 / 1440)
VH = round(VH0 * 1.19)   # recorte = só tira a barra lateral do painel (nada de conteúdo cortado)
WT = 540
LW, LH = 760, 470   # lupa


def build(work):
    S, U, total = marcas(work)
    fl, fc = (work / "fl").as_uri(), (work / "fc").as_uri()
    nfl, nfc = len(list((work / "fl").glob("*.jpg"))), len(list((work / "fc").glob("*.jpg")))
    body = f"""{BG}{TOP}
<div class="cap" id="hook">
  <div class="l" id="h1">Seu cartão com<br>a <span class="am">cara do seu</span><br><span class="am">negócio</span></div>
</div>

<div class="cap step" id="c2"><span class="n">1</span><div>Escolhe o tema<br><span class="hl">e vê a prévia</span></div></div>
<div class="cap step" id="c3"><span class="n">2</span><div>Coloca<br><span class="hl">o seu logo</span></div></div>
<div class="cap step" id="c4"><span class="n">✓</span><div>No celular<br><span class="hl">da cliente</span></div></div>
<div class="cap step" id="c5"><span class="n">★</span><div>Cartão<br><span class="am">personalizado</span></div></div>

<div id="win">
  <div class="bar"><i></i><i></i><i></i><span class="url">🔒 pontua.club</span></div>
  <div class="vp"><img id="sw" src="{fl}/0001.jpg"></div>
</div>
<div id="lens"><img id="sl" src="{fl}/0001.jpg"><div id="tema"><span>tema</span><b id="tn">Rose</b></div><div id="ltag">logo</div></div>

<div id="phone"><div class="scr"><img id="sa" src="{fc}/0078.jpg"><img id="sd" src="{fc}/0900.jpg"><div id="wipe"></div></div><div id="ring"></div></div>
<div id="who">antes</div>

<div class="badge" id="logo" style="left:0;right:0;margin:auto;width:max-content;top:1490px">✓ Logo enviado</div>
<div id="plano"><div class="p1">Disponível a partir do</div><div class="p2">Plano Basic</div><div class="p3">R$ 39/mês</div></div>
{CTA}"""
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
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f}, FL="{fl}", FC="{fc}", NFL={nfl}, NFC={nfc};
const SW={SW}, SH={SH}, VW={WW}, VH={VH}, VH0={VH0}, LW={LW}, LH={LH};
function zoomP(el,fx,fy,z){{ const tx=cl(SW/2-fx*SW*z,SW-SW*z,0), ty=cl(SH/2-fy*SH*z,SH-SH*z,0); el.style.transform=`translate(${{tx}}px,${{ty}}px) scale(${{z}})`; return ty; }}
function zoomW(el,fx,fy,z){{ const tx=cl(VW/2-fx*VW*z,VW-VW*z,0), ty=cl(VH/2-fy*VH0*z,VH-VH0*z,0); el.style.transform=`translate(${{tx}}px,${{ty}}px) scale(${{z}})`; }}
function kf(K,t){{ let i=1; while(i<K.length-1 && t>K[i][0]) i++; const [a,fa]=K[i-1],[b,fb]=K[i];
  const k=ease((t-a)/Math.max(.01,b-a)); return [0,1,2].map(j=>fa[j]+(fb[j]-fa[j])*k); }}
window.R=async function(t){{
  const [n1a,n1b]=S.N1,[n2a,n2b]=S.N2,[n3a,n3b]=S.N3,[n4a,n4b]=S.N4,[n5a,n5b]=S.N5,[n6a,n6b]=S.N6;
  const ps=[];
  // gancho
  const h1=ease((t-(n1a-.05))/.5);
  $('h1').style.cssText=`opacity:${{h1}};transform:translateY(${{(1-h1)*40}}px)`;
  const ho=cl((t-(n1b-1.3))/.35); $('hook').style.opacity=1-ho; $('hook').style.transform=`translateY(${{-ho*60}}px)`;
  const ck=cta(t,n6a);
  $('top').style.opacity=1-ck;
  // celular: ANTES (fim do N1), sai no N2–N3, volta no N4 com DEPOIS
  const pin=ease((t-(n1b-1.05))/.6), pout=ease((t-(n2a-.1))/.45), pback=ease((t-(n4a-.62))/.5);
  const pv = t<n4a-.62 ? pin*(1-pout) : pback*(1-ck);
  const px = t<n4a-.62 ? -pout*900 : (1-pback)*900;
  $('phone').style.opacity=pv; $('who').style.opacity=pv;
  $('phone').style.transform=`translate(${{px}}px,${{t<n2a?(1-pin)*700:0}}px) scale(${{1-ck*.1}})`;
  // janela do painel (N2–N3)
  const win=ease((t-(n2a-.15))/.5), wout=ease((t-(n4a-.62))/.5);
  $('win').style.opacity=win*(1-wout); $('win').style.transform=`translate(${{(1-win)*900-wout*900}}px,0)`;
  const ln=back((t-(n2a+.7))/.5), lo=cl((t-(n4a-.62))/.25);
  $('lens').style.opacity=cl((t-(n2a+.7))/.15)*(1-lo); $('lens').style.transform=`scale(${{.85+.15*ln}})`;
  const vt=pw([[n2a,3.0],[n2a+1.1,5.0],[n2a+1.25,5.4],[n2a+2.3,7.5],[n2a+2.45,8.2],[n2b,11.6],[n3a,12.4],[n3a+.9,15.0],[n3a+1.0,15.8],[n3b-.2,17.4],[T,17.4]],t);
  setImg($('sw'),`${{FL}}/${{pad(Math.min(NFL,Math.max(1,Math.round(vt*30)+1)))}}.jpg`,ps);
  zoomW($('sw'),.58,.5,1.19);
  const ll = vt<12.1;   // lupa: prévia do tema (N2) ou logo (N3)
  $('tema').style.opacity=ll?1:0; $('ltag').style.opacity=ll?0:1;
  setImg($('sl'),$('sw').src,ps);
  const [lx,ly,lz]= ll?[.815,.47,2.32]:[.30,.425,3.0];
  const LHc = ll?LH:330; $('lens').style.height=LHc+'px';
  const lw=VW*lz, lh=VH0*lz; $('sl').style.width=lw+'px'; $('sl').style.height=lh+'px';
  $('sl').style.transform=`translate(${{cl(LW/2-lx*lw,LW-lw,0)}}px,${{cl(LHc/2-ly*lh,LHc-lh,0)}}px)`;
  $('tn').textContent = vt<5.2?'Rose':(vt<7.8?'Escuro':'Dourado');
  $('tn').style.color = vt<5.2?'#FF5FA2':(vt<7.8?'#C9C4E6':'#FFC24D');
  pop('logo',t,n3a+1.05,n4a-.6,-2);
  // antes → depois (cortina)
  const wk=ease((t-(n4a+.35))/.9);
  $('sd').style.clipPath=`inset(0 ${{(1-wk)*100}}% 0 0)`;
  $('wipe').style.left=`${{wk*SW-5}}px`; $('wipe').style.opacity=(wk>0&&wk<1)?1:0;
  $('who').textContent = (t>n4a+.8)?'depois':'antes';
  $('who').style.color = (t>n4a+.8)?'#FFC24D':'{C['muted']}';
  const vd=pw([[n4a,29.6],[T,31.4]],t);
  setImg($('sd'),`${{FC}}/${{pad(Math.min(NFC,Math.max(1,Math.round(vd*30)+1)))}}.jpg`,ps);
  const fz=kf([[0,[.5,.26,1.08]],[n4a+1.3,[.5,.26,1.08]],[n4a+2.0,[.5,.3,1.12]],[T,[.5,.3,1.12]]],t);
  zoomP($('sa'),...fz); const ty=zoomP($('sd'),...fz);
  // anel no cartão + logo (depois)
  const rg=io(t,n4a+1.5,n6a-.1,.3,.25);
  $('ring').style.cssText=`opacity:${{rg}};left:36px;right:36px;top:${{16+ty+.065*SH*fz[2]}}px;height:${{.5*SH*fz[2]}}px`;
  // legendas
  show('c2',t,n2a,n3a); show('c3',t,n3a,n4a-.1); show('c4',t,n4a-.1,n5a); show('c5',t,n5a,n6a-.1);
  // plano
  const pl=back((t-(n5a+.3))/.5), plo=cl((t-(n6a-.35))/.25);
  $('plano').style.opacity=cl((t-(n5a+.3))/.15)*(1-plo); $('plano').style.transform=`scale(${{pl}}) rotate(-3deg)`;
  await Promise.all(ps);
}};
"""
    return page(body, css, js), total


if __name__ == "__main__":
    main(build, "reel_05_cartao_marca.mp4", sys.argv)
