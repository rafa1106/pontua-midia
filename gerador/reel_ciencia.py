# -*- coding: utf-8 -*-
"""Reel 12 — "2 carimbos de presente quase dobram quem completa o cartão" (série A ciência da fidelidade).

Estudo: Nunes & Drèze (2006), Journal of Consumer Research 32(4) — 300 clientes de lava-rápido, 9 meses:
cartão de 8 vazio = 19% completaram; cartão de 10 com 2 carimbos dados = 34%.

Uso: python3 reel_ciencia.py <pasta> [preview t1,t2,...]
  <pasta>/audio (reels/12_progresso) · <pasta>/fl_bonus.jpg (tela real: Emitir carimbo, campo "Carimbos bônus")
"""
import json, sys
from pathlib import Path
from reel_base import *
from reel_papel import CTA_GRATIS, NOTIF

CENAS = Path(__file__).parent / "cenas"
PW = 540
SH = round((PW - 32) * 1342 / 620)
PH = SH + 32


def cartao(id_, titulo, sub, n, dados):
    slots = "".join(f'<i class="{"on" if k < dados else ""}">{"🎁" if k < dados else ""}</i>' for k in range(n))
    return (f'<div class="cd" id="{id_}"><div class="hd"><b>{titulo}</b><span>{sub}</span></div>'
            f'<div class="grid g{n}">{slots}</div></div>')


def build(work):
    S, U, total = marcas(work)
    lava = (CENAS / "r12_lava.png").as_uri()
    fl = (work / "fl_bonus.jpg").as_uri()
    body = f"""<div id="bg"></div>
<div class="sc" id="sc_lava"><img src="{lava}"></div>
<div id="shade"></div>
{TOP}
<div class="cap" id="hook"><div class="l"><span class="am">2 carimbos</span><br>de presente quase<br>dobram quem<br>completa o cartão.</div>
  <div class="est">estudo publicado · Journal of Consumer Research</div></div>
<div class="cap" id="c2"><div class="l mid">Um estudo com clientes<br>de um <span class="hl">lava-rápido</span></div></div>
{cartao("ka", "Cartão A", "8 carimbos · começa vazio", 8, 0)}
{cartao("kb", "Cartão B", "10 carimbos · 2 já de presente", 10, 2)}
<div class="cap" id="c4"><div class="l mid">O esforço<br><span class="hl">era o mesmo.</span></div></div>
<div class="cap" id="c4b"><div class="l mid">Quase <span class="am">o dobro</span><br>completou.</div></div>
<div id="chart">
  <div class="row"><div class="lb">Cartão A · vazio</div><div class="bar"><i id="ba"></i></div><div class="pc" id="pa">0%</div></div>
  <div class="row"><div class="lb am">Cartão B · com presente</div><div class="bar"><i id="bb" class="win"></i></div><div class="pc am" id="pb">0%</div></div>
  <div class="ttl">completaram o cartão</div>
  <div class="src">Nunes &amp; Drèze (2006), Journal of Consumer Research · 300 clientes, 9 meses</div>
</div>
<div class="cap" id="c5"><div class="l">Quem já começa<br>na frente <span class="am">quer<br>terminar.</span></div></div>
<div class="cap step" id="c6"><span class="n">🎁</span><div>No pontua: carimbo<br><span class="hl">de presente já no 1º</span></div></div>
<div id="phone"><div class="scr"><img src="{fl}"></div><div id="ring"></div></div>
<div class="tagc" id="tg">carimbo de presente aqui</div>
<div id="wa">
  <div class="hd"><span class="ic">{WA_ICON}</span><span class="ap">WhatsApp</span><span class="tm">agora</span></div>
  <div class="ti">Café da Esquina</div>
  <div class="tx">{NOTIF}</div>
</div>
{CTA_GRATIS}"""
    css = f"""
#bg{{position:absolute;inset:0;background:#0B0816}}
.sc{{position:absolute;inset:0;overflow:hidden}}
.sc img{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;transform-origin:50% 50%}}
#shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,5,20,.9) 0%,rgba(8,5,20,.55) 30%,rgba(8,5,20,.15) 55%,rgba(8,5,20,.7) 100%)}}
#top{{z-index:3}} .cap{{z-index:3}}
.cap .l{{font-size:96px;line-height:1.04;text-shadow:0 6px 40px rgba(0,0,0,.6)}}
.cap .l.mid{{font-size:78px}}
#hook{{top:250px}} #c2,#c4,#c4b,#c6{{top:240px}} #c5{{top:700px}}
#hook .est{{display:inline-block;margin-top:40px;padding:14px 30px;border-radius:999px;background:rgba(13,10,24,.8);border:2px solid rgba(183,156,255,.5);
  font-size:32px;font-weight:800;color:#E6E0FF}}
.cd{{position:absolute;left:0;right:0;margin:auto;width:900px;border-radius:30px;padding:28px 34px;z-index:3;opacity:0;
  background:rgba(248,246,255,.97);color:#1A1430;box-shadow:0 30px 80px rgba(0,0,0,.55)}}
#ka{{top:640px}} #kb{{top:1040px}}
.cd .hd{{display:flex;align-items:baseline;gap:20px}} .cd .hd b{{font-size:40px;font-weight:900}} .cd .hd span{{font-size:30px;font-weight:700;color:#6A6288}}
.cd .grid{{display:grid;gap:16px;margin-top:22px}} .cd .g8{{grid-template-columns:repeat(4,1fr)}} .cd .g10{{grid-template-columns:repeat(5,1fr)}}
.cd i{{height:96px;border-radius:22px;border:3px dashed #C9C2E0;display:flex;align-items:center;justify-content:center;font-size:52px;font-style:normal}}
.cd i img{{width:56px;height:56px}}
.cd i.on{{border:3px solid {C['violet2']};background:#EDE6FF}}
#chart{{position:absolute;left:70px;right:70px;top:720px;z-index:3;opacity:0;padding:44px 40px;border-radius:34px;background:rgba(13,10,24,.82);
  border:2px solid rgba(183,156,255,.35);box-shadow:0 30px 80px rgba(0,0,0,.5)}}
#chart .row{{display:grid;grid-template-columns:1fr;gap:14px;margin-bottom:36px;position:relative}}
#chart .lb{{font-size:40px;font-weight:800}}
#chart .bar{{height:84px;border-radius:20px;background:rgba(255,255,255,.08);overflow:hidden;margin-right:190px}}
#chart .bar i{{display:block;height:100%;width:0;border-radius:20px;background:#8C85A8}}
#chart .bar i.win{{background:linear-gradient(90deg,{C['amber']},#FFD777);box-shadow:0 0 40px rgba(255,194,77,.5)}}
#chart .pc{{position:absolute;right:0;bottom:4px;font-size:84px;font-weight:900;letter-spacing:-.03em;line-height:1}}
#chart .ttl{{font-size:36px;font-weight:700;color:{C['muted']};margin-top:-6px}}
#chart .src{{margin-top:30px;font-size:24px;font-weight:600;color:rgba(185,178,217,.8)}}
#c6 div{{font-size:58px}}
#phone{{position:absolute;left:{(W - PW) // 2}px;top:500px;width:{PW}px;height:{PH}px;border-radius:72px;padding:16px;z-index:2;opacity:0;
  background:linear-gradient(145deg,#30265A,#0E0A1E);box-shadow:0 0 0 2px rgba(183,156,255,.4),0 0 110px rgba(123,77,255,.55),0 50px 90px rgba(0,0,0,.6)}}
#phone .scr{{width:100%;height:100%;border-radius:56px;overflow:hidden;position:relative;background:#111521}}
#phone .scr img{{position:absolute;left:0;top:0;width:100%;height:auto}}
#ring{{position:absolute;left:34px;right:34px;border-radius:22px;border:5px solid {C['amber']};box-shadow:0 0 40px rgba(255,194,77,.7);opacity:0}}
.tagc{{position:absolute;left:0;right:0;margin:auto;width:max-content;z-index:4;padding:18px 34px;border-radius:999px;background:{C['amber']};color:#1A1030;
  font-size:40px;font-weight:900;box-shadow:0 14px 50px rgba(255,194,77,.45);opacity:0}}
#wa{{position:absolute;left:70px;right:70px;top:1210px;z-index:4;padding:30px 36px;border-radius:38px;background:rgba(248,246,255,.98);color:#141024;opacity:0;
  box-shadow:0 30px 80px rgba(0,0,0,.55),0 0 90px rgba(37,211,102,.35)}}
#wa .hd{{display:flex;align-items:center;gap:16px;font-size:28px;color:#5B5473;font-weight:600}}
#wa .ic{{width:52px;height:52px;border-radius:15px;background:{C['green']};display:flex;align-items:center;justify-content:center}}
#wa .ic svg{{width:32px;height:32px}} #wa .tm{{margin-left:auto;font-size:26px}}
#wa .ti{{font-size:38px;font-weight:800;margin-top:16px}} #wa .tx{{font-size:32px;line-height:1.34;margin-top:10px;color:#2A2440}}
#cta{{z-index:5;background:radial-gradient(110% 60% at 80% 0%, #4A28C8 0%, #2A1470 35%, transparent 70%),radial-gradient(80% 50% at 0% 100%, #3A1BA8 0%, transparent 60%), #0E0822}}
#cta .semcc{{font-size:38px;font-weight:800;color:{C['gain']};margin-top:-20px}}
"""
    js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f};
window.R=async function(t){{
  const N=[1,2,3,4,5,6,7].map(i=>S['N'+i]);
  const [n1a,n1b]=N[0],[n2a,n2b]=N[1],[n3a,n3b]=N[2],[n4a,n4b]=N[3],[n5a,n5b]=N[4],[n6a,n6b]=N[5],[n7a]=N[6];
  const q4=U['N4.2']||(n4a+1.2);
  // fundo: lava-rápido; escurece e desfoca quando entram os gráficos
  const k=cl(t/T); $('sc_lava').querySelector('img').style.transform=`scale(${{1.04+.12*k}})`;
  const dk=ease((t-(n2a-.3))/.6)*(1-ease((t-(n5a-.2))/.5)*.4);
  $('sc_lava').querySelector('img').style.filter=`blur(${{dk*14}}px) brightness(${{1-.55*dk}})`;
  // legendas
  const h=ease((t-.05)/.4); $('hook').style.opacity=h*(1-cl((t-(n2a-.2))/.2)); $('hook').style.transform=`translateY(${{(1-h)*40}}px)`;
  show('c2',t,n2a,n4a); show('c4',t,n4a,q4+.6); show('c4b',t,q4+.6,n5a-.05); show('c5',t,n5a,n6a-.05); show('c6',t,n6a,n7a-.1);
  // cartões A e B
  const ca=back((t-(n2a+.6))/.5), cb=back((t-(n3a+.05))/.5), cout=cl((t-(n4a-.1))/.3);
  $('ka').style.opacity=cl((t-(n2a+.6))/.15)*(1-cout); $('ka').style.transform=`translateY(${{(1-ca)*120}}px)`;
  $('kb').style.opacity=cl((t-(n3a+.05))/.15)*(1-cout); $('kb').style.transform=`translateY(${{(1-cb)*120}}px) scale(${{1+.04*io(t,n3a+.5,n4a,.2,.2)}})`;
  // gráfico 19% x 34%
  const gi=ease((t-(n4a+.1))/.4), go=cl((t-(n5a-.2))/.25);
  $('chart').style.opacity=gi*(1-go); $('chart').style.transform=`translateY(${{(1-gi)*60}}px)`;
  const pa=ease((t-(q4-.2))/.9)*19, pb=ease((t-(q4-.6))/1.1)*34;
  $('ba').style.width=(pa/40*100)+'%'; $('bb').style.width=(pb/40*100)+'%';
  $('pa').textContent=Math.round(pa)+'%'; $('pb').textContent=Math.round(pb)+'%';
  // celular: tela real de emitir carimbo, destaque no campo de carimbos bônus + aviso no WhatsApp
  const pin=ease((t-(n6a+.05))/.6), pout=cl((t-(n7a-.25))/.3);
  $('phone').style.opacity=cl((t-n6a)/.2)*(1-pout); $('phone').style.transform=`translateY(${{(1-pin)*600}}px)`;
  const rg=io(t,n6a+.7,n6a+.62*(n6b-n6a)+.4,.25,.25);
  $('ring').style.cssText=`opacity:${{rg}};top:${{16+.655*SH}}px;height:${{.11*SH}}px`;
  const tg=back((t-(n6a+.85))/.4); $('tg').style.opacity=io(t,n6a+.85,n6a+.62*(n6b-n6a)+.4,.15,.25);
  $('tg').style.top='1120px'; $('tg').style.transform=`scale(${{tg}})`;
  const wq=n6a+.62*(n6b-n6a), wk=back((t-wq)/.5);
  $('wa').style.opacity=cl((t-wq)/.15)*(1-pout); $('wa').style.transform=`translateY(${{(1-wk)*-140}}px) scale(${{.95+.05*wk}})`;
  const ck=cta(t,n7a); $('top').style.opacity=1-ck;
  await Promise.all([...document.images].map(i=>i.decode().catch(()=>{{}})));
}};
const SH={SH};
"""
    return page(body, css, js), total


if __name__ == "__main__":
    main(build, "reel_12_progresso.mp4", sys.argv)
