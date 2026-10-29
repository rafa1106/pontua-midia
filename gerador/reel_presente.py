# -*- coding: utf-8 -*-
"""Reel 19 — "Salão e barbearia: e se o primeiro carimbo fosse um presente?" (série Pra quem é, viés reciprocidade).

Cenas por IA (barbearia e salão, atendimento no balcão, presente na bancada) + a tela real de emitir carimbo com o
campo "Carimbos bônus adicionais" (o bônus do 1º atendimento funciona no grátis) + o cartão desenhado no visual do
app (nomes de exemplo) + avisos com o texto real dos modelos do WhatsApp.

Uso: python3 reel_presente.py <pasta> [preview t1,t2,...]   <pasta>/audio (reels/19_presente_salao)
"""
import json, sys
from pathlib import Path
from reel_base import *
from reel_papel import CTA_GRATIS
from render2 import _emoji

CENAS = Path(__file__).parent / "cenas"
LOJA, CLI, IC, PREMIO = "Studio Corte & Cia", "Rafael Lima", "✂️", "1 corte grátis"
GRAD = "linear-gradient(135deg,#3B2A6E,#6A4BC4)"
TW = 760                       # largura da tela real (bônus)
TK = TW / 620
TY = 700
PW = 520
SH = round((PW - 32) * 1342 / 620)
PH = SH + 32


def tela(n_on):
    st = "".join(f'<i id="m{j}" class="{"on" if j < n_on else ""}">{("🎁" if j == 1 else IC) if j < n_on else ""}</i>' for j in range(10))
    return f"""<div class="app"><div class="pn"><div class="lj">{LOJA}</div><div class="tt">Cartão {LOJA}</div>
  <div class="ds">A cada corte, um carimbo. Completou, o próximo corte é por nossa conta!</div>
  <div class="ol">Olá, {CLI.split()[0]}!</div>
  <div class="cd" style="background:{GRAD}"><div class="h"><div><b>Cartão {LOJA}</b><small>{LOJA}</small></div><span>{PREMIO}</span></div>
    <div class="gr">{st}</div><div class="pf"><span>Progresso</span><span>2/10</span></div><div class="pl"><i></i></div></div>
  <div class="pg"><b>2 de 10 carimbos</b><span>ATIVO</span></div><div class="bar"><i></i></div>
  <div class="rc">🎁 Recompensa: {PREMIO}</div>
  <div class="hs"><b>Histórico</b><div class="hr new"><span>+1 carimbo bônus 🎁</span><span>hoje</span></div>
    <div class="hr"><span>+1 carimbo</span><span>hoje</span></div></div></div></div>"""


def build(work):
    S, U, total = marcas(work)
    c = {k: (CENAS / f).as_uri() for k, f in (("bar", "r15b_hook.png"), ("sal", "r15c_hook.png"), ("rec", "r19_recepcao.png"),
                                             ("pre", "r19_presente.png"), ("amb", "r15c_amb.png"), ("fim", "r15b_premio.png"))}
    tb = (CENAS / "r19_tela_bonus.png").as_uri()
    AV = [
        (f"Olá, {CLI}.<br>Você recebeu um novo carimbo de {LOJA}.<br>No momento, <b>faltam 8 carimbos</b> para completar o cartão.", "2/10"),
        (f"Olá, {CLI}.<br>Você recebeu um novo carimbo de {LOJA}.<br>No momento, <b>faltam 2 carimbos</b> para completar o cartão.", "8/10"),
    ]
    avs = "".join(f'<div class="av" id="a{i}"><div class="hd"><span class="ic">{WA_ICON}</span><span>WhatsApp · <b>{LOJA}</b></span>'
                  f'<span class="pr">{p}</span></div><div class="tx">{tx}</div></div>' for i, (tx, p) in enumerate(AV))
    st10 = "".join(f'<i class="on">{"🎁" if j == 1 else IC}</i>' for j in range(10))
    scenes = "".join(f'<div class="sc" id="sc_{k}"><img src="{v}"></div>' for k, v in c.items() if k not in ("bar", "sal"))
    body = f"""<div id="bg"></div>
<div id="split"><div class="hv" id="hv1"><img src="{c['bar']}"></div><div class="hv" id="hv2"><img src="{c['sal']}"></div><div id="sep"></div></div>
{scenes}
<div id="shade"></div><div id="flash"></div>
{TOP}
<div class="cap" id="hook"><div class="chip0">💈 Salão e barbearia</div><div class="l">E se o 1º carimbo<br>fosse um <span class="am">presente?</span></div></div>
<div class="cap step" id="c2"><span class="n">🎁</span><div>1º atendimento:<br><span class="hl">carimbo extra de presente</span></div></div>
<div id="tb"><img src="{tb}"><div id="val">0</div><div id="tap"></div></div>
<div id="tela">tela real do app</div>
<div class="cap" id="c3"><div class="l mid" id="c3a">Não é desconto.<br><span class="am">É gentileza.</span></div>
  <div class="l small" id="c3b">E quem ganha um presente<br>tende a <span class="hl">retribuir.</span></div></div>
<div id="fonte">reciprocidade · Cialdini, <i>As armas da persuasão</i></div>
<div class="cap step" id="c4"><span class="n wa">{WA_ICON}</span><div>Já sai na frente,<br><span class="hl">e o WhatsApp avisa</span></div></div>
<div id="phone"><div class="scr">{tela(2)}</div></div>
<div id="stack">{avs}</div>
<div id="nota">textos reais dos avisos · nome de exemplo</div>
<div class="cap" id="c5"><div class="l mid">O 10º corte é<br><span class="am">por conta da casa.</span></div></div>
<div id="card" style="background:{GRAD}"><div class="hd"><b>Cartão {LOJA}</b><span>{PREMIO}</span></div><div class="grid">{st10}</div>
  <div class="ft"><span>10 de 10</span><span class="gift">✓ prêmio liberado!</span></div></div>
{CTA_GRATIS}"""
    css = f"""
#bg{{position:absolute;inset:0;background:#0B0816}}
.sc,#split{{position:absolute;inset:0;overflow:hidden;opacity:0}}
.sc img{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;transform-origin:50% 50%}}
.hv{{position:absolute;left:0;width:{W}px;height:{H // 2}px;overflow:hidden}} #hv1{{top:0}} #hv2{{top:{H // 2}px}}
.hv img{{position:absolute;left:0;width:{W}px;height:{H}px}} #hv1 img{{top:-{H // 5}px}} #hv2 img{{top:-{H // 4}px}}
#sep{{position:absolute;left:0;right:0;top:{H // 2 - 4}px;height:8px;background:{C['amber']};box-shadow:0 0 30px rgba(255,194,77,.7)}}
#shade{{position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,rgba(8,5,20,.9) 0%,rgba(8,5,20,.62) 26%,rgba(8,5,20,.25) 36%,rgba(8,5,20,0) 46%,rgba(8,5,20,0) 62%,rgba(8,5,20,.72) 100%)}}
#flash{{position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none;z-index:6}}
#top{{z-index:3}} .cap{{z-index:3}}
.cap .l{{font-size:100px;line-height:1.03;text-shadow:0 4px 18px rgba(0,0,0,.85),0 6px 50px rgba(0,0,0,.6)}}
.cap .l.mid{{font-size:90px}} .cap .l.small{{font-size:66px;font-weight:800;line-height:1.12}}
#hook{{top:220px}} #c2,#c4{{top:240px}} #c2 div,#c4 div{{font-size:56px}} #c3,#c5{{top:250px}}
#c3 .l{{position:absolute;left:0;right:0}} #c3b{{top:250px}}
.chip0{{display:inline-block;margin-bottom:28px;padding:14px 34px;border-radius:999px;background:rgba(13,10,24,.78);border:2px solid rgba(183,156,255,.55);
  font-size:42px;font-weight:900}}
#tb{{position:absolute;left:{(W - TW) // 2}px;top:{TY}px;width:{TW}px;border-radius:34px;overflow:hidden;z-index:3;opacity:0;
  box-shadow:0 0 0 2px rgba(183,156,255,.45),0 0 110px rgba(123,77,255,.5),0 40px 90px rgba(0,0,0,.6)}}
#tb img{{display:block;width:100%}}
#val{{position:absolute;left:{round(106 * TK)}px;top:{round(76 * TK)}px;width:{round(40 * TK)}px;height:{round(40 * TK)}px;background:rgb(86,98,120);
  color:#fff;font-size:{round(24 * TK)}px;font-weight:800;display:flex;align-items:center;justify-content:center}}
#tap{{position:absolute;left:{round(248 * TK)}px;top:{round(408 * TK)}px;width:{round(282 * TK)}px;height:{round(64 * TK)}px;border-radius:{round(12 * TK)}px;
  border:5px solid {C['amber']};box-shadow:0 0 36px rgba(255,194,77,.7);opacity:0}}
#tela{{position:absolute;left:0;right:0;text-align:center;z-index:3;font-size:28px;font-weight:700;color:rgba(230,224,255,.75);opacity:0}}
#fonte{{position:absolute;left:0;right:0;top:1580px;text-align:center;z-index:3;font-size:26px;font-weight:600;color:rgba(230,224,255,.75);opacity:0}}
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
.app .pl{{height:3px;border-radius:2px;background:rgba(255,255,255,.3);margin-top:4px;overflow:hidden}} .app .pl i{{display:block;height:100%;width:20%;background:#FFD777}}
.app .pg{{display:flex;justify-content:space-between;align-items:center;margin-top:26px;font-size:19px;text-align:left}}
.app .pg span{{padding:4px 12px;border-radius:999px;background:rgba(46,212,122,.18);color:#4BE08F;font-size:14px;font-weight:800}}
.app .bar{{height:10px;border-radius:5px;background:rgba(255,255,255,.14);margin-top:10px;overflow:hidden}} .app .bar i{{display:block;height:100%;width:20%;border-radius:5px;background:#E5D8FF}}
.app .rc{{margin-top:18px;font-size:18px;color:#C9CEDD;text-align:left}}
.app .hs{{margin-top:26px;padding-top:22px;border-top:1px solid rgba(255,255,255,.14);text-align:left;font-size:19px}}
.app .hr{{display:flex;justify-content:space-between;margin-top:16px;font-size:18px;color:#fff}} .app .hr span+span{{color:#C9CEDD}}
.app .hr.new{{color:#FFD777}}
#m1{{box-shadow:0 0 0 4px {C['amber']},0 0 26px rgba(255,194,77,.8)}}
#stack{{position:absolute;left:60px;right:60px;top:560px;z-index:4}}
.av{{margin-bottom:24px;padding:26px 30px;border-radius:30px;background:rgba(248,246,255,.98);color:#141024;opacity:0;box-shadow:0 26px 70px rgba(0,0,0,.5)}}
.av .hd{{display:flex;align-items:center;gap:14px;font-size:26px;color:#5B5473;font-weight:600}} .av .hd b{{color:#141024}}
.av .ic{{width:46px;height:46px;border-radius:13px;background:{C['green']};display:flex;align-items:center;justify-content:center}} .av .ic svg{{width:28px;height:28px}}
.av .pr{{margin-left:auto;padding:6px 16px;border-radius:999px;background:#EDE8FF;color:#4A2BC8;font-size:24px;font-weight:900;white-space:nowrap}}
.av .tx{{font-size:33px;line-height:1.36;margin-top:12px;color:#2A2440}} .av .tx b{{background:#FFF1C9}}
#nota{{position:absolute;left:0;right:0;top:1580px;text-align:center;z-index:4;font-size:26px;font-weight:600;color:rgba(230,224,255,.75);opacity:0}}
#card{{position:absolute;left:0;right:0;margin:auto;top:1200px;width:880px;border-radius:34px;padding:28px 34px;z-index:3;opacity:0;color:#fff;
  box-shadow:0 30px 80px rgba(0,0,0,.6)}}
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
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f};
function vis(id,t,a,b,fi=.2,fo=.2){{ const o=cl((t-a)/fi)*(1-cl((t-(b-fo))/fo)); $(id).style.opacity=o; return o; }}
function kb(id,t,a,b,z0,z1,y0,y1){{ const k=cl((t-a)/Math.max(.1,b-a)); $(id).querySelector('img').style.transform=`translateY(${{lerp(y0,y1,k)}}px) scale(${{lerp(z0,z1,k)}})`; }}
window.R=async function(t){{
  const N=[1,2,3,4,5,6].map(i=>S['N'+i]);
  const [n1a,n1b]=N[0],[n2a,n2b]=N[1],[n3a,n3b]=N[2],[n4a,n4b]=N[3],[n5a,n5b]=N[4],[n6a]=N[5];
  const n3m=U['N3.2']||(n3a+.45*(n3b-n3a)), n4m=n4a+.45*(n4b-n4a);
  // gancho: barbearia em cima, salão embaixo
  vis('split',t,-1,n2a+.05,.01,.15);
  const sp=cl(t/Math.max(.1,n2a));
  $('hv1').querySelector('img').style.transform=`translateX(${{lerp(-30,30,sp)}}px) scale(1.08)`;
  $('hv2').querySelector('img').style.transform=`translateX(${{lerp(30,-30,sp)}}px) scale(1.08)`;
  const h=ease((t-.05)/.4); $('hook').style.opacity=h*(1-cl((t-(n2a-.2))/.2)); $('hook').style.transform=`translateY(${{(1-h)*40}}px)`;
  // cenas
  vis('sc_rec',t,n2a-.05,n3a+.05,.15,.15); kb('sc_rec',t,n2a,n3a,1.04,1.14,0,-30);
  vis('sc_pre',t,n3a-.05,n4a+.05,.15,.15); kb('sc_pre',t,n3a,n4a,1.14,1.03,-20,20);
  vis('sc_amb',t,n4a-.05,n5a+.05,.15,.15); kb('sc_amb',t,n4a,n5a,1.03,1.12,0,0);
  vis('sc_fim',t,n5a-.05,n6a+.6,.15,.3); kb('sc_fim',t,n5a,T,1.1,1.0,-30,20);
  $('flash').style.opacity=.25*Math.max(0,...[n2a,n3a,n4a,n5a].map(x=>1-Math.abs(t-x)/.09));
  // N2: tela real — carimbo bônus 0 → 1 e emitir
  show('c2',t,n2a,n3a-.05);
  const ti=ease((t-(n2a+.1))/.5), to=cl((t-(n3a-.25))/.25);
  $('tb').style.opacity=cl((t-(n2a+.1))/.2)*(1-to); $('tb').style.transform=`translateY(${{(1-ti)*400-to*80}}px)`;
  const d2=n2b-n2a, tv=n2a+.42*d2, tt=n2a+.72*d2;
  $('val').textContent = t>=tv ? '1' : '0';
  $('val').style.transform = (t>=tv && t<tv+.3) ? `scale(${{1.5-(t-tv)*1.6}})` : '';
  $('val').style.color = t>=tv ? '{C['amber']}' : '#fff';
  $('tap').style.opacity=io(t,tt,n3a-.1,.12,.2); $('tap').style.transform=`scale(${{1-.06*cl(1-Math.abs(t-(tt+.1))/.12)}})`;
  const r=$('tb').getBoundingClientRect(); $('tela').style.top=(r.bottom+18)+'px'; $('tela').style.opacity=io(t,n2a+.4,n3a-.05,.3,.2);
  // N3: reciprocidade
  const s3=cl((t-n3a)/.3)*(1-cl((t-(n4a-.25))/.25)); $('c3').style.opacity=s3;
  const a1=ease((t-n3a)/.35), a2=ease((t-(n3m-.1))/.35);
  $('c3a').style.cssText=`opacity:${{a1}};transform:translateY(${{(1-a1)*30}}px)`;
  $('c3b').style.cssText=`opacity:${{a2}};transform:translateY(${{(1-a2)*30}}px)`;
  $('fonte').style.opacity=io(t,n3m+.2,n4a,.3,.25);
  // N4: já sai na frente (2 de 10) e os avisos no WhatsApp
  show('c4',t,n4a,n5a-.05);
  const pin=ease((t-(n4a+.05))/.55), pout=cl((t-(n4m-.1))/.3);
  $('phone').style.opacity=cl((t-(n4a+.05))/.2)*(1-pout); $('phone').style.transform=`translateY(${{(1-pin)*600}}px)`;
  const ao=cl((t-(n5a-.2))/.25);
  [n4m+.05,n4m+.35*(n4b-n4m)+.3].forEach((tq,i)=>{{ const k=back((t-tq)/.45), e=$('a'+i);
    e.style.opacity=cl((t-tq)/.15)*(1-ao); e.style.transform=`translateY(${{(1-k)*-100}}px) scale(${{.95+.05*k}})`; }});
  $('nota').style.opacity=io(t,n4m+.4,n5a,.3,.2);
  // N5: o 10º corte
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
    main(build, "reel_19_presente_salao.mp4", sys.argv)
