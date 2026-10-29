# -*- coding: utf-8 -*-
"""Reel 11 — "Seu negócio está nessa lista?" (2ª remessa, série Pra quem é: cenas por IA + movimento).

Uso: python3 reel_lista.py <pasta> [preview t1,t2,...]
  <pasta>/audio/narracao.mp3 + alinhamento.json (reels/11_pra_quem_e)
  gerador/cenas/r11_*.png  cenas por IA · <pasta>/fc_card.jpg  tela real do cartão digital
"""
import json, sys
from pathlib import Path
from reel_base import *
from reel_papel import CTA_GRATIS

CENAS = Path(__file__).parent / "cenas"
PW = 540
SH = round((PW - 32) * 1342 / 620)
PH = SH + 32

# segmento: (id da cena, nome, frase, ícone do carimbo, prêmio, gradiente do cartão)
SEG = [
    ("padaria", "Café", "Cafeteria e padaria", 'o décimo café é <span class="am">por conta da casa.</span>', "☕", "1 café grátis",
     "linear-gradient(135deg,#C9692A,#E8943A)"),
    ("barbearia", "Barbearia", "Salão e barbearia", 'o corte que <span class="am">completa o cartão.</span>', "✂️", "1 corte grátis",
     "linear-gradient(135deg,#2B2440,#4A3D6E)"),
    ("pet", "Pet", "Pet shop", 'o banho que <span class="am">vira prêmio.</span>', "🐾", "1 banho grátis",
     "linear-gradient(135deg,#D9607E,#F08BA0)"),
    ("acai", "Açaí", "Açaí, sorveteria e lanchonete", 'o cliente volta <span class="am">pra completar.</span>', "🍧", "1 açaí grátis",
     "linear-gradient(135deg,#5B2A86,#8E4FC4)"),
]


def build(work):
    S, U, total = marcas(work)
    cena = {k: (CENAS / f"r11_{k}.png").as_uri() for k in ("rua", "padaria", "barbearia", "pet", "acai")}
    fundo = (CENAS / "r10_fundo.png").as_uri()
    fc = (work / "fc_card.jpg").as_uri()
    scenes = "".join(f'<div class="sc" id="sc_{k}"><img src="{v}"></div>' for k, v in cena.items())
    segs = ""
    for i, (k, curto, nome, frase, ic, premio, grad) in enumerate(SEG):
        st = "".join(f'<i id="s{i}_{j}"><b>{ic}</b></i>' for j in range(10))
        segs += f"""<div class="seg" id="g{i}"><div class="nm">{nome}</div><div class="fr">{frase}</div></div>
<div class="card" id="k{i}" style="background:{grad}"><div class="hd"><span>Cartão {curto}</span><span class="pr">{premio}</span></div>
  <div class="grid">{st}</div><div class="ft"><span id="n{i}">6/10</span><span class="gift" id="w{i}">✓ prêmio liberado!</span></div></div>"""
    body = f"""<div id="bg"></div>
{scenes}<div class="sc" id="sc_fundo"><img src="{fundo}"></div>
<div id="shade"></div><div id="flash"></div>
{TOP}
<div class="cap" id="hook"><div class="l">Seu negócio<br>está <span class="am">nessa lista?</span></div></div>
{segs}
<div class="cap" id="c6"><div class="l mid">Se está, o pontua<br><span class="hl">é pra você.</span></div></div>
<div id="phone"><div class="scr"><img src="{fc}"></div></div>
<div id="chips">
  <div class="ch" id="h1"><span class="ok">✓</span>cartão no celular</div>
  <div class="ch" id="h2"><span class="ok">✓</span>sem aplicativo</div>
  <div class="ch" id="h3"><span class="ok okwa">{WA_ICON}</span>avisos no WhatsApp</div>
</div>
{CTA_GRATIS}"""
    css = f"""
#bg{{position:absolute;inset:0;background:#0B0816}}
.sc{{position:absolute;inset:0;overflow:hidden;opacity:0}}
.sc img{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;transform-origin:50% 50%}}
#shade{{position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,rgba(8,5,20,.88) 0%,rgba(8,5,20,.5) 24%,rgba(8,5,20,0) 44%,rgba(8,5,20,0) 58%,rgba(8,5,20,.75) 100%)}}
#flash{{position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none}}
#top{{z-index:3}} .cap{{z-index:3}}
.cap .l{{font-size:100px;line-height:1.04;text-shadow:0 6px 40px rgba(0,0,0,.6)}}
.cap .l.mid{{font-size:84px}}
#hook,#c6{{top:250px}}
.seg{{position:absolute;left:60px;right:60px;top:240px;z-index:3;text-align:center;opacity:0}}
.seg .nm{{display:inline-block;padding:14px 34px;border-radius:999px;background:rgba(13,10,24,.78);border:2px solid rgba(183,156,255,.55);
  font-size:40px;font-weight:900;color:#fff;letter-spacing:-.01em}}
.seg .fr{{margin-top:26px;font-size:76px;font-weight:800;letter-spacing:-.04em;line-height:1.06;text-shadow:0 6px 40px rgba(0,0,0,.7)}}
.card{{position:absolute;left:0;right:0;margin:auto;top:1180px;width:880px;border-radius:34px;padding:30px 36px 26px;z-index:3;opacity:0;color:#fff;
  box-shadow:0 30px 80px rgba(0,0,0,.6),0 0 0 2px rgba(255,255,255,.18) inset}}
.card .hd{{display:flex;justify-content:space-between;align-items:center;font-size:32px;font-weight:800}}
.card .pr{{padding:8px 18px;border-radius:999px;background:rgba(255,255,255,.22);font-size:26px}}
.card .grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:18px 20px;margin-top:24px}}
.card i{{display:flex;align-items:center;justify-content:center;width:132px;height:100px;border-radius:24px;background:rgba(255,255,255,.14);
  border:2px dashed rgba(255,255,255,.35)}}
.card i b{{font-size:54px;opacity:0;transform:scale(.4)}} .card i b img{{width:56px;height:56px}}
.card i.on{{background:rgba(255,255,255,.95);border:2px solid #fff}}
.card i.on b{{opacity:1;transform:scale(1)}}
.card .ft{{display:flex;justify-content:space-between;align-items:center;margin-top:20px;font-size:32px;font-weight:900}}
.card .gift{{padding:10px 22px;border-radius:999px;background:{C['amber']};color:#1A1030;font-size:30px;opacity:0}}
#phone{{position:absolute;left:{(W - PW) // 2}px;top:500px;width:{PW}px;height:{PH}px;border-radius:72px;padding:16px;z-index:2;opacity:0;
  background:linear-gradient(145deg,#30265A,#0E0A1E);box-shadow:0 0 0 2px rgba(183,156,255,.4),0 0 110px rgba(123,77,255,.55),0 50px 90px rgba(0,0,0,.6)}}
#phone .scr{{width:100%;height:100%;border-radius:56px;overflow:hidden;position:relative;background:#111521}}
#phone .scr img{{position:absolute;left:0;top:0;width:100%;height:auto}}
#phone .scr::after{{content:"";position:absolute;left:0;right:0;bottom:0;height:40%;background:linear-gradient(rgba(17,21,33,0),#111521 30%)}}
#chips{{position:absolute;left:0;right:0;top:1150px;z-index:4;display:flex;flex-direction:column;align-items:center;gap:22px}}
.ch{{display:flex;align-items:center;gap:20px;padding:22px 40px 22px 24px;border-radius:999px;background:rgba(248,246,255,.98);color:#141024;
  font-size:46px;font-weight:800;box-shadow:0 20px 60px rgba(0,0,0,.5);opacity:0}}
.ch .ok{{width:62px;height:62px;border-radius:50%;background:{C['gain']};color:#fff;display:flex;align-items:center;justify-content:center;font-size:38px}}
.ch .ok.okwa{{background:{C['green']}}} .ch .ok svg{{width:36px;height:36px}}
#cta{{z-index:5;background:radial-gradient(110% 60% at 80% 0%, #4A28C8 0%, #2A1470 35%, transparent 70%),radial-gradient(80% 50% at 0% 100%, #3A1BA8 0%, transparent 60%), #0E0822}}
#cta .semcc{{font-size:38px;font-weight:800;color:{C['gain']};margin-top:-20px}}
"""
    js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f};
function kb(id,t,a,b,z0,z1,y0,y1){{ const k=cl((t-a)/Math.max(.1,b-a)); $(id).querySelector('img').style.transform=`translateY(${{lerp(y0,y1,k)}}px) scale(${{lerp(z0,z1,k)}})`; }}
function vis(id,t,a,b,fi=.18,fo=.18){{ const o=cl((t-a)/fi)*(1-cl((t-(b-fo))/fo)); $(id).style.opacity=o; return o; }}
window.R=async function(t){{
  const N=[1,2,3,4,5,6,7].map(i=>S['N'+i]);
  const [n1a]=N[0], n6=N[5], n7a=N[6][0];
  // cenas: rua (N1), um segmento por fala (N2–N5), fundo do café (N6)
  vis('sc_rua',t,-1,N[1][0]+.05,.01,.15);  kb('sc_rua',t,0,N[1][0],1.03,1.14,0,-60);
  const ids=['padaria','barbearia','pet','acai'];
  ids.forEach((k,i)=>{{ const a=N[i+1][0], b=N[i+2][0]; vis('sc_'+k,t,a-.02,b+.05,.12,.14); kb('sc_'+k,t,a,b,1.12,1.02,-30,20); }});
  vis('sc_fundo',t,n6[0]-.05,n7a+.4,.2,.3); kb('sc_fundo',t,n6[0],n7a,1.02,1.1,0,0);
  const fl=Math.max(0,...[2,3,4,5,6].map(i=>1-Math.abs(t-N[i-1][0])/.09)); $('flash').style.opacity=.28*fl;
  // gancho
  const h=ease((t-.05)/.4); $('hook').style.opacity=h*(1-cl((t-(N[1][0]-.2))/.2)); $('hook').style.transform=`translateY(${{(1-h)*40}}px)`;
  // segmentos: nome + frase + cartão do ramo enchendo de 6/10 até 10/10 (prêmio)
  ids.forEach((k,i)=>{{ const a=N[i+1][0], b=N[i+2][0], d=b-a;
    show('g'+i,t,a,b-.02,.3,.18);
    const c=$('k'+i), ci=back((t-(a+.12))/.45), co=cl((t-(b-.2))/.2);
    c.style.opacity=cl((t-(a+.1))/.15)*(1-co); c.style.transform=`translateY(${{(1-ci)*160}}px) rotate(${{(i%2?1.5:-1.5)}}deg)`;
    let n=6;
    for(let j=0;j<10;j++){{ const tj = j<6 ? -1 : a+.45+(j-6)*Math.min(.32,(d-1.2)/4); const on=t>=tj; if(on && j>=6) n++;
      const e=$(`s${{i}}_${{j}}`); e.className=on?'on':''; e.style.transform=(j>=6 && t>=tj && t<tj+.16)?`scale(${{1.18-(t-tj)}})`:''; }}
    $('n'+i).textContent=n+'/10';
    const gw=a+.45+4*Math.min(.32,(d-1.2)/4)+.05; const g=back((t-gw)/.4); $('w'+i).style.opacity=cl((t-gw)/.1); $('w'+i).style.transform=`scale(${{g}})`;
  }});
  // N6: é pra você — celular com o cartão real e as três vantagens
  show('c6',t,n6[0],n7a-.1);
  const pin=ease((t-(n6[0]+.05))/.6), pout=cl((t-(n7a-.25))/.3);
  $('phone').style.opacity=cl((t-n6[0])/.2)*(1-pout); $('phone').style.transform=`translateY(${{(1-pin)*600}}px)`;
  const d6=n6[1]-n6[0];
  [['h1',.42],['h2',.62],['h3',.8]].forEach(([id,f])=>{{ const tq=n6[0]+f*d6, k=back((t-tq)/.4);
    $(id).style.opacity=cl((t-tq)/.12)*(1-pout); $(id).style.transform=`translateX(${{(1-k)*-120}}px)`; }});
  const ck=cta(t,n7a); $('top').style.opacity=1-ck;
  await Promise.all([...document.images].map(i=>i.decode().catch(()=>{{}})));
}};
"""
    return page(body, css, js), total


if __name__ == "__main__":
    main(build, "reel_11_pra_quem_e.mp4", sys.argv)
