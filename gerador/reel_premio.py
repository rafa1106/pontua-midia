# -*- coding: utf-8 -*-
"""Reel 04 — "Cartão completo e resgate" (fluxo 04: Ricardo tem 9/10, ganha o 10º, recebe aviso e resgata).

Uso: python3 reel_premio.py <pasta> [preview t1,t2,...]
  <pasta>/fl, <pasta>/fc  quadros (30 fps, 620 px) já com realce de contraste (realce.py)
  <pasta>/audio/narracao.mp3 + alinhamento.json (robô de narração)
"""
import json, sys
from reel_base import *

PW = 600
SW = PW - 32
SH = round(SW * 2532 / 1170)
PT = 470


def build(work):
    S, U, total = marcas(work)
    fl, fc = (work / "fl").as_uri(), (work / "fc").as_uri()
    nfl, nfc = len(list((work / "fl").glob("*.jpg"))), len(list((work / "fc").glob("*.jpg")))
    msg = ("Olá, Ricardo Martins!<br><br>Seu cartão da Café da Esquina foi completado com sucesso.<br><br>"
           "Toque em “Ver opções” para consultar os próximos passos.")
    body = f"""{BG}{TOP}
<div class="cap" id="hook">
  <div class="l" id="h1">O melhor momento<br>da fidelidade?</div>
  <div class="l small2" id="h2">Quando o cliente<br><span class="am">completa o cartão.</span></div>
</div>

<div class="cap step" id="c2"><span class="n">1</span><div>Décimo café:<br><span class="hl">último carimbo</span></div></div>
<div class="cap step" id="c3"><span class="n wa">{WA_ICON}</span><div>Cartão completo<br><span class="hl">aviso no WhatsApp</span></div></div>
<div class="cap step" id="c4"><span class="n">2</span><div>No balcão:<br><span class="hl">valida o resgate</span></div></div>
<div class="cap step" id="c5"><span class="n">↻</span><div>O cartão recomeça<br><span class="am">e ele volta</span></div></div>

<div id="phone"><div class="scr"><img id="sa" src="{fc}/0060.jpg"><img id="sb" src="{fl}/0001.jpg"></div><div id="ring"></div></div>
<div id="who"></div>

<div class="chip" id="falta" style="right:40px;top:1040px">falta 1 ☕</div>
<div id="burst"></div>
<div id="plus"><span>10/10</span><small>cartão completo 🎉</small></div>
{wa_card("wa", "Café da Esquina", msg, ("Ver opções",), top=430)}
<div class="badge" id="ok" style="right:36px;top:1240px">✓ Resgate validado</div>
<div class="chip" id="volta" style="left:0;right:0;margin:auto;width:max-content;top:1330px">próximo café grátis: 0 de 10 ☕</div>
{CTA}"""
    css = f"""
#hook{{top:560px}}
.cap .l.small2{{font-size:66px;font-weight:800;letter-spacing:-.035em;line-height:1.08;margin-top:44px;color:#EDE8FF}}
#phone{{position:absolute;left:{(W-PW)//2}px;top:{PT}px;width:{PW}px;height:{SH + 32}px;border-radius:78px;padding:16px;
  background:linear-gradient(145deg,#352B66,#120D26);box-shadow:0 0 0 2px rgba(183,156,255,.5),0 0 110px rgba(123,77,255,.55),0 50px 90px rgba(0,0,0,.6);
  transform-origin:50% 30%}}
.scr{{width:100%;height:100%;border-radius:62px;overflow:hidden;position:relative;background:#1A1E2C}}
.scr img{{position:absolute;left:0;top:0;width:{SW}px;height:{SH}px;transform-origin:0 0}}
#sb{{opacity:0}}
#who{{position:absolute;left:0;right:0;top:{PT + SH + 32 + 22}px;text-align:center;font-size:30px;font-weight:700;color:{C['muted']}}}
#ring{{position:absolute;border-radius:26px;border:5px solid {C['amber']};box-shadow:0 0 36px rgba(255,194,77,.65);opacity:0}}
#plus{{position:absolute;left:0;right:0;margin:auto;top:1010px;width:460px;height:460px;border-radius:50%;display:flex;flex-direction:column;
  align-items:center;justify-content:center;background:radial-gradient(circle,#FFD777 0%,#FFC24D 55%,#E8A020 100%);color:#1A1030;
  box-shadow:0 0 0 16px rgba(255,194,77,.22),0 0 140px rgba(255,194,77,.8);opacity:0}}
#plus span{{font-size:150px;font-weight:900;letter-spacing:-.06em;line-height:.9}}
#plus small{{font-size:40px;font-weight:800;margin-top:14px}}
#burst{{position:absolute;left:540px;top:1240px;width:0;height:0}}
#burst i{{position:absolute;width:24px;height:24px;border-radius:6px;opacity:0}}
"""
    js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f}, FL="{fl}", FC="{fc}", NFL={nfl}, NFC={nfc}, SW={SW}, SH={SH};
const CORES=['#FFC24D','#B79CFF','#2ED47A','#FF8FB1','#7B4DFF','#FFFFFF'];
for(let i=0;i<26;i++){{const e=document.createElement('i');e.style.background=CORES[i%CORES.length];$('burst').appendChild(e);}}
function zoom(el,fx,fy,z){{ const tx=cl(SW/2-fx*SW*z,SW-SW*z,0), ty=cl(SH/2-fy*SH*z,SH-SH*z,0);
  el.style.transform=`translate(${{tx}}px,${{ty}}px) scale(${{z}})`; }}
// foco suave por tempo: [t,[fx,fy,z]]
function kf(K,t){{ let i=1; while(i<K.length-1 && t>K[i][0]) i++; const [a,fa]=K[i-1],[b,fb]=K[i];
  const k=ease((t-a)/Math.max(.01,b-a)); return [0,1,2].map(j=>fa[j]+(fb[j]-fa[j])*k); }}
window.R=async function(t){{
  const [n1a,n1b]=S.N1,[n2a,n2b]=S.N2,[n3a,n3b]=S.N3,[n4a,n4b]=S.N4,[n5a,n5b]=S.N5,[n6a,n6b]=S.N6;
  const q=U['N1.2'], v2=U['N5.2'];
  const ps=[];
  // gancho
  const h1=ease((t-(n1a-.05))/.45), h2=ease((t-(q-.1))/.45);
  $('h1').style.cssText=`opacity:${{h1}};transform:translateY(${{(1-h1)*40}}px)`;
  $('h2').style.cssText=`opacity:${{h2}};transform:translateY(${{(1-h2)*40}}px)`;
  const ho=cl((t-(n1b-1.25))/.35); $('hook').style.opacity=1-ho; $('hook').style.transform=`translateY(${{-ho*60}}px)`;
  // celular
  const pe=ease((t-(n1b-1.0))/.6), ck=cta(t,n6a);
  $('phone').style.opacity=pe*(1-ck); $('top').style.opacity=1-ck;
  const dip=1-.04*cl(1-Math.abs(t-(n2a+.4))/.22)-.04*cl(1-Math.abs(t-(n5a-.1))/.22);
  $('phone').style.transform=`translateY(${{(1-pe)*700+ck*300}}px) scale(${{(1-ck*.1)*dip}})`;
  // qual tela: cliente (N1), atendente (N2–N4), cliente (N5)
  const lojista = t>=n2a+.4 && t<n5a-.1;
  $('sb').style.opacity = lojista?1:0; $('sa').style.opacity = lojista?0:1;
  $('who').textContent = lojista?'celular da atendente':'celular do cliente';
  $('who').style.opacity = pe*(1-ck);
  // tempo de vídeo
  const vtl=pw([[n2a+.4,6.2],[n3a,17.7],[n3b,19.0],[n4a,19.2],[n4b-.2,29.2],[n5a,30]],t);
  const vtc= t<n2a+1 ? 3 : pw([[n5a,36.6],[n5b,39.2]],t);
  setImg($('sb'),`${{FL}}/${{pad(Math.min(NFL,Math.max(1,Math.round(vtl*30)+1)))}}.jpg`,ps);
  setImg($('sa'),`${{FC}}/${{pad(Math.min(NFC,Math.max(1,Math.round(vtc*30)+1)))}}.jpg`,ps);
  // zoom nas áreas que importam
  const fa=kf([[0,[.5,.36,1.12]],[n2a+.5,[.5,.36,1.12]],[n5a,[.5,.4,1.0]],[n5a+.6,[.5,.44,1.1]],[T,[.5,.44,1.1]]],t);
  zoom($('sa'),...fa);
  const fb=kf([[n2a+.4,[.5,.5,1.0]],[n2a+1.7,[.5,.72,1.28]],[n3a-.2,[.5,.66,1.2]],[n3a+.2,[.5,.28,1.22]],[n4a,[.5,.3,1.22]],
               [n4a+.5,[.5,.48,1.25]],[n4b-1.1,[.5,.5,1.25]],[n4b-.6,[.5,.8,1.12]],[n5a,[.5,.8,1.12]]],t);
  zoom($('sb'),...fb);
  // anel: cartão 9/10 (N1) e "0 de 10 · resgatada" (N5)
  let rg=0, ry=0, rh=0;
  if(t<n2a+.5){{ rg=io(t,n1b-.5,n2a+.35,.3,.2); ry=.283; rh=.2; }}
  else if(t>n5a){{ rg=io(t,n5a+.7,n6a-.1,.3,.25); ry=.494; rh=.058; }}
  // posição do anel acompanha o zoom da tela do cliente
  const ty=cl(SH/2-fa[1]*SH*fa[2],SH-SH*fa[2],0);
  $('ring').style.cssText=`opacity:${{rg}};left:${{16+20}}px;right:${{16+20}}px;top:${{16+ty+ry*SH*fa[2]}}px;height:${{rh*SH*fa[2]}}px`;
  pop('falta',t,n1b-.45,n2a+.4,-3);
  // legendas
  show('c2',t,n2a+.3,n3a); show('c3',t,n3a,n4a); show('c4',t,n4a,n5a); show('c5',t,n5a,n6a-.1);
  // 10/10 + confete, depois WhatsApp
  const tp=n3a+.05, po=cl((t-(n3a+1.3))/.25);
  const pb=back((t-tp)/.45);
  $('plus').style.cssText=`opacity:${{cl((t-tp)/.12)*(1-po)}};transform:scale(${{pb*(1-po*.3)}}) rotate(${{-6+pb*4}}deg)`;
  [...$('burst').children].forEach((e,i)=>{{ const k=cl((t-tp)/1.1), ang=i/26*Math.PI*2+(i%3)*.2, r=120+k*(380+(i%4)*40);
    e.style.opacity=t>tp?(1-k):0; e.style.transform=`translate(${{Math.cos(ang)*r}}px,${{Math.sin(ang)*r+k*k*160}}px) rotate(${{k*540+i*20}}deg)`; }});
  const wa0=n3a+1.35, wi=back((t-wa0)/.5), wo=cl((t-(n4a-.15))/.35);
  $('wa').style.cssText=`top:430px;opacity:${{cl((t-wa0)/.2)*(1-wo)}};transform:translateY(${{(1-wi)*-260-wo*200}}px) scale(${{.96+wi*.04}})`;
  // resgate validado (toast aparece no vídeo ~28,5 s)
  const tok=pw([[n4a,19.2],[n4b-.2,29.2]].map(([a,b])=>[b,a]),28.6);
  pop('ok',t,tok,n5a-.2,-2);
  pop('volta',t,v2-.05,n6a-.1,0);
  await Promise.all(ps);
}};
"""
    return page(body, css, js), total


if __name__ == "__main__":
    main(build, "reel_04_premio.mp4", sys.argv)
