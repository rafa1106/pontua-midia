# -*- coding: utf-8 -*-
"""Reels 15b–15g — versões por segmento do Reel 15 ("X: 10 ..., 1 grátis. Sem papel.").

Mesmo argumento do Reel 15 (cafeteria), adaptado: cenas por IA do segmento (gancho, ambiente, prêmio), o mesmo carimbo de
borracha (N3), avisos com o texto real dos modelos do WhatsApp (nomes de loja e cliente de exemplo) e, no celular, o cartão
desenhado no visual do app com o nome e o ícone do segmento.

Uso: python3 reel_segmento.py <seg> <pasta> [preview t1,t2,...]   seg: barbearia|salao|pet|acai|lava|burger
"""
import json, sys
from pathlib import Path
from reel_base import *
from reel_papel import CTA_GRATIS
from render2 import _emoji

CENAS = Path(__file__).parent / "cenas"
PW = 520
SH = round((PW - 32) * 1342 / 620)
PH = SH + 32

SEGS = {
  "barbearia": dict(chip="💈 Barbearia", hook="10 cortes,<br>1 grátis.", loja="Barbearia do Bairro", cliente="Rafael Lima", ic="✂️",
      premio="1 corte grátis", item="corte", grad="linear-gradient(135deg,#2B2440,#4A3D6E)",
      c2='O corte de todo mês,<br><span class="hl">carimbo no celular</span>', c5='O 10º corte é<br><span class="am">por conta da casa.</span>',
      cenas=("r15b_hook.png", "r11_barbearia.png", "r15b_premio.png"), out="15b_barbearia"),
  "salao": dict(chip="💇 Salão de beleza", hook="10 visitas,<br>1 escova<br>grátis.", loja="Studio da Vila", cliente="Juliana Costa", ic="💅",
      premio="1 escova grátis", item="visita", grad="linear-gradient(135deg,#C2577F,#E98AA8)",
      c2='A escova ou a unha,<br><span class="hl">carimbo no celular</span>', c5='Na 10ª visita, a escova<br><span class="am">é por conta da casa.</span>',
      cenas=("r15c_hook.png", "r15c_amb.png", "r15c_premio.png"), out="15c_salao"),
  "pet": dict(chip="🐾 Pet shop", hook="10 banhos,<br>1 grátis.", loja="Pet Feliz", cliente="Carla Martins", ic="🐾",
      premio="1 banho grátis", item="banho", grad="linear-gradient(135deg,#D9607E,#F08BA0)",
      c2='Cada banho do pet,<br><span class="hl">carimbo no celular</span>', c5='O 10º banho é<br><span class="am">por conta da casa.</span>',
      cenas=("r15d_hook.png", "r15d_amb.png", "r11_pet.png"), out="15d_pet"),
  "acai": dict(chip="🍇 Açaí", hook="10 copos,<br>1 grátis.", loja="Açaí da Praça", cliente="Maria Souza", ic="🍇",
      premio="1 açaí grátis", item="açaí", grad="linear-gradient(135deg,#5B2A86,#8E4FC4)",
      c2='O açaí de sempre,<br><span class="hl">carimbo no celular</span>', c5='O 10º açaí é<br><span class="am">por conta da casa.</span>',
      cenas=("r15e_hook.png", "r15e_amb.png", "r11_acai.png"), out="15e_acai"),
  "lava": dict(chip="🚗 Lava-rápido", hook="10 lavagens,<br>1 grátis.", loja="Lava-Rápido Brilho", cliente="Paulo Souza", ic="🚗",
      premio="1 lavagem grátis", item="lavagem", grad="linear-gradient(135deg,#1F5FA8,#3E8EDB)",
      c2='Cada lavagem,<br><span class="hl">carimbo no celular</span>', c5='A 10ª lavagem é<br><span class="am">por conta da casa.</span>',
      cenas=("r12_lava.png", "r15f_amb.png", "r15f_premio.png"), out="15f_lavarapido"),
  "burger": dict(chip="🍔 Hamburgueria", hook="10 lanches,<br>1 grátis.", loja="Burger da Vila", cliente="Lucas Pereira", ic="🍔",
      premio="1 lanche grátis", item="lanche", grad="linear-gradient(135deg,#B2361F,#E0652E)",
      c2='O lanche de sempre,<br><span class="hl">carimbo no celular</span>', c5='O 10º lanche é<br><span class="am">por conta da casa.</span>',
      cenas=("r15g_hook.png", "r15g_amb.png", "r15g_premio.png"), out="15g_hamburgueria"),
}
SEG = None


def tela_cartao(g):
    """Tela do cartão no layout da página real do cliente (fc_card do Reel 15), com nome/ícone do segmento; nomes de exemplo."""
    st = "".join(f'<i id="m{j}" class="{"on" if j < 7 else ""}">{g["ic"] if j < 7 else ""}</i>' for j in range(10))
    return f"""<div class="app"><div class="pn"><div class="lj">{g['loja']}</div><div class="tt">Cartão {g['loja']}</div>
  <div class="ds">A cada {g['item']}, um carimbo. Completou, o próximo {g['item']} é por nossa conta!</div>
  <div class="ol">Olá, {g['cliente'].split()[0]}!</div>
  <div class="cd" style="background:{g['grad']}"><div class="h"><div><b>Cartão {g['loja']}</b><small>{g['loja']}</small></div><span>{g['premio']}</span></div>
    <div class="gr">{st}</div><div class="pf"><span>Progresso</span><span id="mfr">7/10</span></div><div class="pl"><i id="mpl"></i></div></div>
  <div class="pg"><b id="mcnt">7 de 10 carimbos</b><span>ATIVO</span></div><div class="bar"><i id="mbar"></i></div>
  <div class="rc">🎁 Recompensa: {g['premio']}</div>
  <div class="hs"><b>Histórico</b><div class="hr new" id="mnew"><span>+1 carimbo</span><span>agora</span></div>
    <div class="hr"><span>+1 carimbo</span><span>14/10</span></div><div class="hr"><span>+1 carimbo</span><span>07/10</span></div></div></div></div>"""


def build(work):
    S, U, total = marcas(work)
    g = SEG
    hk, am, pz = g["cenas"]
    c = {k: (CENAS / f).as_uri() for k, f in (("esp", hk), ("pad", am), ("rub", "r15_carimbo.png"), ("fun", am), ("cap", pz))}
    AV = [
        (f"Olá, {g['cliente']}.<br>Você recebeu um novo carimbo de {g['loja']}.<br>No momento, <b>faltam 3 carimbos</b> para completar o cartão.", "7/10"),
        (f"Olá, {g['cliente']}.<br>Você recebeu um novo carimbo de {g['loja']}.<br>No momento, <b>faltam 2 carimbos</b> para completar o cartão.", "8/10"),
        (f"Olá, {g['cliente']}!<br>Seu cartão da {g['loja']} foi <b>completado com sucesso.</b>", "10/10 🎉"),
    ]
    scenes = "".join(f'<div class="sc" id="sc_{k}"><img src="{v}"></div>' for k, v in c.items())
    avs = "".join(f'<div class="av" id="a{i}"><div class="hd"><span class="ic">{WA_ICON}</span><span>WhatsApp · <b>{g['loja']}</b></span>'
                  f'<span class="pr">{p}</span></div><div class="tx">{tx}</div></div>' for i, (tx, p) in enumerate(AV))
    st = "".join(f'<i id="k{j}" class="on">{g["ic"]}</i>' for j in range(10))
    body = f"""<div id="bg"></div>
{scenes}
<div id="shade"></div><div id="flash"></div>
{TOP}
<div class="cap" id="hook"><div class="chip0">{g['chip']}</div><div class="l">{g['hook']}<br><span class="am">Sem papel.</span></div></div>
<div class="cap step" id="c2"><span class="n">{g['ic']}</span><div>{g['c2']}</div></div>
<div id="phone"><div class="scr">{tela_cartao(g)}</div></div>
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
<div class="cap" id="c5"><div class="l mid">{g['c5']}</div></div>
<div id="card" style="background:{g['grad']}"><div class="hd"><b>Cartão {g['loja']}</b><span>{g['premio']}</span></div><div class="grid">{st}</div>
  <div class="ft"><span>10 de 10</span><span class="gift">✓ prêmio liberado!</span></div></div>
{CTA_GRATIS}"""
    css = f"""
#bg{{position:absolute;inset:0;background:#0B0816}}
.sc{{position:absolute;inset:0;overflow:hidden;opacity:0}}
.sc img{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;transform-origin:50% 50%}}
#shade{{position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,rgba(8,5,20,.9) 0%,rgba(8,5,20,.62) 26%,rgba(8,5,20,.25) 36%,rgba(8,5,20,0) 46%,rgba(8,5,20,0) 60%,rgba(8,5,20,.72) 100%)}}
#flash{{position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none;z-index:6}}
#top{{z-index:3}} .cap{{z-index:3}}
.cap .l{{font-size:112px;line-height:1.02;text-shadow:0 4px 18px rgba(0,0,0,.85),0 6px 50px rgba(0,0,0,.6)}}
.cap .l.mid{{font-size:84px}}
#hook{{top:230px}} #c3,#c5{{top:250px}} #c2,#c4{{top:240px}} #c2 div,#c4 div{{font-size:58px}}
.chip0{{display:inline-block;margin-bottom:28px;padding:14px 34px;border-radius:999px;background:rgba(13,10,24,.78);border:2px solid rgba(183,156,255,.55);
  font-size:42px;font-weight:900}}
#phone{{position:absolute;left:{(W - PW) // 2}px;top:520px;width:{PW}px;height:{PH}px;border-radius:70px;padding:16px;z-index:2;opacity:0;
  background:linear-gradient(145deg,#30265A,#0E0A1E);box-shadow:0 0 0 2px rgba(183,156,255,.4),0 0 110px rgba(123,77,255,.55),0 50px 90px rgba(0,0,0,.6)}}
#phone .scr{{width:100%;height:100%;border-radius:54px;overflow:hidden;position:relative;background:#111521}}
.app{{position:absolute;inset:0;background:#20232D;color:#E8EAF2;text-align:center}}
.app .pn{{position:absolute;left:18px;right:18px;top:66px;bottom:56px;border-radius:22px;padding:22px 26px 0;
  background:linear-gradient(180deg,#3B4153,#2F3445);box-shadow:0 10px 30px rgba(0,0,0,.35)}}
.app .lj{{font-size:19px;color:#B8C2DA;font-weight:700}} .app .tt{{font-size:26px;font-weight:800;margin-top:8px;color:#fff}}
.app .ds{{font-size:18px;line-height:1.42;color:#BFC8DE;margin:10px 4px 0}} .app .ol{{font-size:19px;font-weight:700;margin-top:12px;color:#fff}}
.app .cd{{margin-top:26px;border-radius:16px;padding:14px 14px 12px;text-align:left;color:#fff;box-shadow:0 10px 30px rgba(0,0,0,.35)}}
.app .cd .h{{display:flex;justify-content:space-between;align-items:flex-start;font-size:15px}} .app .cd .h small{{display:block;font-size:12px;opacity:.85;margin-top:2px}}
.app .cd .h span{{padding:3px 12px;border-radius:999px;background:rgba(255,255,255,.22);font-size:12px;font-weight:800;white-space:nowrap}}
.app .gr{{display:grid;grid-template-columns:repeat(5,1fr);gap:7px;margin-top:12px;padding:0 6px}}
.app .gr i{{aspect-ratio:1;border-radius:50%;border:1.5px solid rgba(255,255,255,.55);display:flex;align-items:center;justify-content:center;font-size:30px;font-style:normal}}
.app .gr i img{{width:34px;height:34px}} .app .gr i.on{{background:rgba(255,255,255,.9);border-color:transparent}}
.app .pf{{display:flex;justify-content:space-between;font-size:11px;margin-top:12px;opacity:.9}}
.app .pl{{height:3px;border-radius:2px;background:rgba(255,255,255,.3);margin-top:4px;overflow:hidden}} .app .pl i{{display:block;height:100%;width:70%;background:#FFD777}}
.app .pg{{display:flex;justify-content:space-between;align-items:center;margin-top:26px;font-size:19px;text-align:left}}
.app .pg span{{padding:4px 12px;border-radius:999px;background:rgba(46,212,122,.18);color:#4BE08F;font-size:14px;font-weight:800}}
.app .bar{{height:10px;border-radius:5px;background:rgba(255,255,255,.14);margin-top:10px;overflow:hidden}} .app .bar i{{display:block;height:100%;width:70%;border-radius:5px;background:#E5D8FF}}
.app .rc{{margin-top:18px;font-size:18px;color:#C9CEDD;text-align:left}}
.app .hs{{margin-top:26px;padding-top:22px;border-top:1px solid rgba(255,255,255,.14);text-align:left;font-size:19px}}
.app .hr{{display:flex;justify-content:space-between;margin-top:16px;font-size:18px;color:#fff}} .app .hr span+span{{color:#C9CEDD}}
.app .hr.new{{display:none;color:#4BE08F}} .app .hr.new span+span{{color:#4BE08F;font-weight:800}}
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
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f}, SH={SH}, ICON={json.dumps(_emoji(g["ic"]))};
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
  const r7=$('m7').getBoundingClientRect(); $('plus').style.top=lerp(1480,r7.top+r7.height/2-115,pk)+'px'; $('plus').style.transform=`scale(${{lerp(1.15,.45,pk)}})`;
  const got = t>=pq+.5; const e7=$('m7'); e7.className=got?'on':''; e7.innerHTML = got ? ICON : '';
  e7.style.transform = (t>=pq+.5 && t<pq+.75) ? `scale(${{1.3-(t-pq-.5)*1.2}})` : '';
  $('mcnt').textContent = (got?8:7)+' de 10 carimbos'; $('mbar').style.width=(got?80:70)+'%'; $('mfr').textContent=(got?8:7)+'/10'; $('mpl').style.width=(got?80:70)+'%';
  $('mnew').style.display = got ? 'flex' : 'none'; $('mnew').style.opacity = got ? cl((t-pq-.5)/.25) : 0;
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
  // N5: o 10º item
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
    SEG = SEGS[sys.argv[1]]
    main(build, f"reel_{SEG['out']}.mp4", sys.argv[1:])
