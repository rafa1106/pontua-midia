# -*- coding: utf-8 -*-
"""Reel 07 — "No automático" (fluxo 05, Pet Feliz): canais de aviso, mimos automáticos (aba Avançado)
e os avisos que o cliente recebe no WhatsApp (textos reais dos modelos aprovados).

Uso: python3 reel_auto.py <pasta> [preview t1,t2,...]
  <pasta>/fl  quadros do lojista.mp4 (computador, 1200 px) com realce local
  <pasta>/audio/narracao.mp3 + alinhamento.json
"""
import json, sys
from reel_base import *

WW = 1000
VH0 = round(WW * 900 / 1440)
VH = round(VH0 * 1.19)
WT = 540
LW, LH = 920, 380

# textos reais (05_automacoes/mensagens.json) — remetente Pet Feliz
AVISOS = [
    ("carimbo recebido", "Olá, Carla Martins.<br><br>Você recebeu um novo carimbo de Pet Feliz.<br><br>No momento, faltam 2 carimbos para completar o cartão."),
    ("aniversário", "Olá, Diego. Feliz aniversário! 🎉<br><br>Para marcar essa data, adicionamos 1 carimbo ao seu cartão Banho Fidelidade Pet Feliz de Pet Feliz."),
    ("cliente sumido", "Olá, Diego.<br><br>Seu cartão Banho Fidelidade Pet Feliz da Pet Feliz está parado há alguns dias, mas você ainda pode continuar seu progresso.<br><br>Você já tem 4 carimbos no cartão."),
]


def build(work):
    S, U, total = marcas(work)
    fl = (work / "fl").as_uri()
    nfl = len(list((work / "fl").glob("*.jpg")))
    cards = "".join(
        f'<div class="av" id="av{i}"><div class="hd"><span class="ic">{WA_ICON}</span><span>WhatsApp · <b>Pet Feliz</b></span>'
        f'<span class="ev">{ev}</span></div><div class="tx">{tx}</div><div class="bt">Ver meu cartão</div></div>'
        for i, (ev, tx) in enumerate(AVISOS))
    body = f"""{BG}{TOP}
<div class="cap" id="hook">
  <div class="l" id="h1">Cliente some<br>e você <span class="am">nem percebe?</span></div>
  <div class="l small2" id="h2">Deixa o pontua<br><span class="hl">avisar por você.</span></div>
</div>

<div class="cap step" id="c2"><span class="n wa">{WA_ICON}</span><div>Avisa no <span class="hl">WhatsApp</span><br><span class="sm">+ SMS e e-mail, se quiser</span></div></div>
<div class="cap step" id="c3"><span class="n">2</span><div>Liga os mimos<br><span class="am">automáticos</span></div></div>
<div class="cap step" id="c4"><span class="n wa">{WA_ICON}</span><div>Saem sozinhos<br><span class="hl">no WhatsApp</span></div></div>
<div class="cap step" id="c5"><span class="n">★</span><div>Sem você<br><span class="am">lembrar de nada</span></div></div>

<div id="win">
  <div class="bar"><i></i><i></i><i></i><span class="url">🔒 pontua.club</span></div>
  <div class="vp"><img id="sw" src="{fl}/0001.jpg"></div>
</div>
<div id="lens"><img id="sl" src="{fl}/0001.jpg"><div id="lring"></div></div><div id="ltag">canais de aviso</div>

<div id="stack">{cards}</div>
<div id="nota">textos reais dos avisos · nomes de exemplo</div>
<div id="plano"><div class="p1">Avisos automáticos</div><div class="p2">no WhatsApp ✓</div></div>
{CTA_PAGO}"""
    css = f"""
#hook{{top:540px}}
.step .sm{{font-size:40px;font-weight:700;color:#E6E0FF;letter-spacing:-.02em}}
.cap .l.small2{{font-size:66px;font-weight:800;letter-spacing:-.035em;line-height:1.08;margin-top:44px;color:#EDE8FF}}
#win{{position:absolute;left:{(W-WW)//2}px;top:{WT}px;width:{WW}px;border-radius:26px;overflow:hidden;background:#0F1220;opacity:0;
  box-shadow:0 0 0 2px rgba(183,156,255,.45),0 0 110px rgba(123,77,255,.5),0 50px 90px rgba(0,0,0,.6);transform-origin:50% 0}}
#win .bar{{height:58px;background:#1C1A30;display:flex;align-items:center;gap:12px;padding:0 22px}}
#win .bar i{{width:16px;height:16px;border-radius:50%;background:#3C3760}}
#win .url{{margin-left:22px;flex:1;height:36px;border-radius:12px;background:#0F0D1E;color:#B9B2D9;font-size:22px;display:flex;align-items:center;padding-left:18px}}
#win .vp{{position:relative;width:{WW}px;height:{VH}px;overflow:hidden}}
#win .vp img{{position:absolute;left:0;top:0;width:{WW}px;height:{VH0}px;transform-origin:0 0}}
#lens{{position:absolute;left:0;right:0;margin:auto;top:1110px;width:{LW}px;height:{LH}px;border-radius:30px;overflow:hidden;background:#0F1220;opacity:0;
  border:4px solid {C['amber']};box-shadow:0 30px 80px rgba(0,0,0,.6),0 0 70px rgba(255,194,77,.45);transform-origin:50% 0}}
#lens img{{position:absolute;left:0;top:0;transform-origin:0 0}}
#ltag{{position:absolute;left:{(W-LW)//2+26}px;top:1074px;opacity:0;z-index:5;padding:10px 22px;border-radius:999px;background:rgba(13,10,24,.85);border:1.5px solid rgba(183,156,255,.45);
  font-size:26px;font-weight:900;color:{C['amber']};text-transform:uppercase;letter-spacing:.12em}}
#lring{{position:absolute;border-radius:18px;border:4px solid {C['amber']};box-shadow:0 0 30px rgba(255,194,77,.7);opacity:0}}
#stack{{position:absolute;left:60px;right:60px;top:430px}}
.av{{position:relative;margin-bottom:28px;padding:26px 30px 24px;border-radius:32px;background:rgba(248,246,255,.98);color:#141024;opacity:0;
  box-shadow:0 26px 70px rgba(0,0,0,.5),0 0 70px rgba(155,120,255,.35)}}
.av .hd{{display:flex;align-items:center;gap:14px;font-size:26px;color:#5B5473;font-weight:600}}
.av .hd b{{color:#141024}}
.av .ic{{width:46px;height:46px;border-radius:13px;background:{C['green']};display:flex;align-items:center;justify-content:center}}
.av .ic svg{{width:28px;height:28px}}
.av .ev{{margin-left:auto;padding:6px 16px;border-radius:999px;background:#EDE8FF;color:#4A2BC8;font-size:22px;font-weight:800;text-transform:uppercase;letter-spacing:.06em}}
.av .tx{{font-size:30px;line-height:1.36;margin-top:14px;color:#2A2440}}
.av .bt{{margin-top:16px;padding:14px;border-radius:16px;background:#EDE8FF;color:#4A2BC8;text-align:center;font-size:27px;font-weight:800}}
#nota{{position:absolute;left:0;right:0;top:1690px;text-align:center;font-size:26px;color:{C['muted']};font-weight:600;opacity:0}}
#plano{{position:absolute;left:0;right:0;margin:auto;width:max-content;top:1060px;padding:40px 70px;border-radius:36px;text-align:center;opacity:0;
  background:linear-gradient(135deg,{C['violet2']},{C['violet']});box-shadow:0 30px 80px rgba(0,0,0,.55),0 0 90px rgba(123,77,255,.8)}}
#plano .p1{{font-size:34px;font-weight:700;color:#E6E0FF}} #plano .p2{{font-size:76px;font-weight:900;letter-spacing:-.035em;margin-top:6px}}
#plano .p3{{font-size:40px;font-weight:800;color:{C['amber']};margin-top:4px}}
"""
    js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f}, FL="{fl}", NFL={nfl};
const VW={WW}, VH={VH}, VH0={VH0}, LW={LW}, LH={LH};
function zoomW(el,fx,fy,z){{ const tx=cl(VW/2-fx*VW*z,VW-VW*z,0), ty=cl(VH/2-fy*VH0*z,VH-VH0*z,0); el.style.transform=`translate(${{tx}}px,${{ty}}px) scale(${{z}})`; }}
function kf(K,t){{ let i=1; while(i<K.length-1 && t>K[i][0]) i++; const [a,fa]=K[i-1],[b,fb]=K[i];
  const k=ease((t-a)/Math.max(.01,b-a)); return fa.map((v,j)=>v+(fb[j]-v)*k); }}
window.R=async function(t){{
  const [n1a,n1b]=S.N1,[n2a,n2b]=S.N2,[n3a,n3b]=S.N3,[n4a,n4b]=S.N4,[n5a,n5b]=S.N5,[n6a,n6b]=S.N6;
  const ps=[], q=U['N1.2'], d2=n2b-n2a;
  // gancho
  const h1=ease((t-(n1a-.05))/.45), h2=ease((t-(q-.1))/.45);
  $('h1').style.cssText=`opacity:${{h1}};transform:translateY(${{(1-h1)*40}}px)`;
  $('h2').style.cssText=`opacity:${{h2}};transform:translateY(${{(1-h2)*40}}px)`;
  const ho=cl((t-(n2a-.45))/.35); $('hook').style.opacity=1-ho; $('hook').style.transform=`translateY(${{-ho*60}}px)`;
  const ck=cta(t,n6a);
  $('top').style.opacity=1-ck;
  // janela + lupa (N2–N3)
  const win=ease((t-(n2a-.25))/.55), wout=ease((t-(n4a-.25))/.45);
  $('win').style.opacity=win*(1-wout); $('win').style.transform=`translateY(${{(1-win)*700-wout*120}}px) scale(${{1-wout*.08}})`;
  const lin=back((t-(n2a+.45))/.5), lo=cl((t-(n4a-.3))/.25);
  $('lens').style.opacity=cl((t-(n2a+.45))/.15)*(1-lo); $('lens').style.transform=`scale(${{.85+.15*lin}})`;
  const vt = t<n3a ? pw([[n2a,3.2],[n2b,11.6]],t)
                   : pw([[n3a,12.4],[n3a+2.1,14.3],[n3a+2.4,14.8],[n3a+4.9,15.9],[n3a+5.3,16.6],[n3b,19.0],[T,19.0]],t);
  setImg($('sw'),`${{FL}}/${{pad(Math.min(NFL,Math.max(1,Math.round(vt*30)+1)))}}.jpg`,ps);
  zoomW($('sw'),.58,.5,1.19);
  setImg($('sl'),$('sw').src,ps);
  // lupa: canais (N2, desce WhatsApp → SMS → e-mail) e engajamento (N3)
  let L, alvo=null, tag;
  if(t<n3a){{
    const q2=U['N2.2']||(n2a+.5*d2), d22=n2b-q2, tw=n2a+.25, ts=q2+.45*d22, te=q2+.75*d22;
    L=kf([[n2a,[.42,.43,2.0]],[ts-.45,[.42,.43,2.0]],[ts,[.42,.58,2.0]],[te-.4,[.42,.58,2.0]],[te,[.42,.7,2.0]],[T,[.42,.7,2.0]]],t);
    alvo = t<tw-.3?null:(t<ts-.2?[.38,.49]:(t<te-.2?[.535,.68]:[.705,.79]));
    tag='canais de aviso';
  }} else {{
    L=[.43,.515,1.92]; tag='mimos automáticos';
    const tb=n3a+2.0, ta=n3a+3.6, td=n3a+4.8;
    alvo = t<tb-.2?null:(t<ta-.2?[.355,.415]:(t<td-.2?[.435,.495]:[.535,.66]));
  }}
  const [lx,ly,lz]=L, lw=VW*lz, lh=VH0*lz;
  $('sl').style.width=lw+'px'; $('sl').style.height=lh+'px';
  const ox=cl(LW/2-lx*lw,LW-lw,0), oy=cl(LH/2-ly*lh,LH-lh,0);
  $('sl').style.transform=`translate(${{ox}}px,${{oy}}px)`;
  $('ltag').textContent=tag; $('ltag').style.opacity=$('lens').style.opacity;
  if(alvo){{ const [y0,y1]=alvo; $('lring').style.cssText=`opacity:1;left:${{ox+.195*lw}}px;top:${{oy+y0*lh}}px;width:${{.47*lw}}px;height:${{(y1-y0)*lh}}px`; }}
  else $('lring').style.opacity=0;
  // avisos no WhatsApp (N4) — entram um a um; no N5 ficam ao fundo
  const dim = 1-.6*ease((t-(n5a-.1))/.4), sOut=1-ck;
  [0,1,2].forEach(i=>{{ const t0=n4a-.12+i*.75, k=back((t-t0)/.5), o=cl((t-t0)/.18);
    const e=$('av'+i); e.style.opacity=o*dim*sOut; e.style.transform=`translateY(${{(1-k)*-120}}px) scale(${{.94+.06*k}})`; }});
  $('nota').style.opacity=io(t,n4a+1.8,n5a+.2,.3,.3);
  // plano
  const pl=back((t-(n5a+.15))/.5), plo=cl((t-(n6a-.3))/.25);
  $('plano').style.opacity=cl((t-(n5a+.15))/.15)*(1-plo); $('plano').style.transform=`scale(${{pl}})`;
  // legendas
  show('c2',t,n2a,n3a); show('c3',t,n3a,n4a-.1); show('c4',t,n4a-.1,n5a); show('c5',t,n5a,n6a-.1);
  await Promise.all(ps);
}};
"""
    return page(body, css, js), total


if __name__ == "__main__":
    main(build, "reel_07_automatico.mp4", sys.argv)
