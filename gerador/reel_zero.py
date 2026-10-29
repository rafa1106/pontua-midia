# -*- coding: utf-8 -*-
"""Reel 02 — "Do zero ao programa no ar" (fluxo 01 do material bruto, lojista no computador).

Uso: python3 reel_zero.py <pasta> [preview t1,t2,...]
  <pasta>/fl/NNNN.jpg  quadros do lojista.mp4 (30 fps, 960x600)
  <pasta>/audio/narracao.mp3 + marcas.json
O cronômetro mostra o tempo REAL da gravação (vídeo acelerado).
"""
import json, sys
from reel_base import *

WW = 1000                 # largura da janela do navegador
VH0 = round(WW * 900 / 1440)  # altura da imagem da tela (16:10) na largura da janela
VH = VH0                  # tela inteira, sem recorte (nada cortado nas laterais)
WT = 520                  # topo da janela
LW, LH = 920, 330         # lupa


def build(work):
    S, U, total = marcas(work)
    fl = (work / "fl").as_uri()
    nfl = len(list((work / "fl").glob("*.jpg")))
    body = f"""{BG}{TOP}
<div class="cap" id="hook">
  <div class="l" id="h1">Montar fidelidade</div>
  <div class="l" id="h2"><span class="am">dá trabalho?</span></div>
</div>
<div class="cap" id="hook2"><div class="l small">Olha esse saindo do zero 👇</div></div>

<div class="cap step" id="c2"><span class="n">1</span><div>Cria a conta<br><span class="hl">e dá um nome</span></div></div>
<div class="cap step" id="c3"><span class="n">2</span><div>Escolhe<br><span class="am">a regra</span></div></div>
<div class="cap step" id="c4"><span class="n">3</span><div>Pronto:<br><span class="hl">campanha ativa</span></div></div>
<div class="cap step" id="c5"><span class="n">4</span><div>QR Code<br><span class="hl">pro balcão</span></div></div>

<div id="win">
  <div class="bar"><i></i><i></i><i></i><span class="url">🔒 pontua.club</span></div>
  <div class="vp"><img id="sv" src="{fl}/0001.jpg"></div>
</div>
<div id="lens"><img id="sl" src="{fl}/0001.jpg"><div id="ltag">cria a conta</div></div>
<div id="timer"><span class="ic">⏱</span><b id="tt">0:00</b><span class="lb">tempo real da gravação</span></div>

<div class="chip" id="rule" style="left:0;right:0;margin:auto;width:max-content;top:1610px">a cada 10 cafés, 1 grátis ☕</div>
<div class="badge" id="ativa" style="left:0;right:0;margin:auto;width:max-content;top:1610px">✓ Campanha ativa</div>
<div class="badge" id="qrok" style="left:0;right:0;margin:auto;width:max-content;top:1610px">✓ QR Code e link prontos</div>
{CTA}"""
    css = f"""
#hook{{top:640px}} #hook2{{top:290px}}
#win{{position:absolute;left:{(W-WW)//2}px;top:{WT}px;width:{WW}px;border-radius:26px;overflow:hidden;background:#0F1220;
  box-shadow:0 0 0 2px rgba(183,156,255,.4),0 0 110px rgba(123,77,255,.5),0 50px 90px rgba(0,0,0,.6);transform-origin:50% 0}}
#win .bar{{height:58px;background:#1C1A30;display:flex;align-items:center;gap:12px;padding:0 22px}}
#win .bar i{{width:16px;height:16px;border-radius:50%;background:#3C3760}}
#win .url{{margin-left:22px;flex:1;height:36px;border-radius:12px;background:#0F0D1E;color:#B9B2D9;font-size:22px;
  display:flex;align-items:center;padding-left:18px}}
#win .vp{{position:relative;width:{WW}px;height:{VH}px;overflow:hidden}}
#win .vp img{{position:absolute;left:0;top:0;width:{WW}px;height:{VH0}px;transform-origin:0 0}}
#lens{{position:absolute;left:0;right:0;margin:auto;top:{WT + 58 + VH + 40}px;width:{LW}px;height:{LH}px;border-radius:30px;overflow:hidden;background:#0F1220;opacity:0;
  border:4px solid {C['amber']};box-shadow:0 30px 80px rgba(0,0,0,.6),0 0 70px rgba(255,194,77,.45);transform-origin:50% 0}}
#lens img{{position:absolute;left:0;top:0;transform-origin:0 0}}
#ltag{{position:absolute;left:20px;top:16px;padding:10px 22px;border-radius:999px;background:rgba(13,10,24,.85);border:1.5px solid rgba(183,156,255,.45);
  font-size:26px;font-weight:900;color:{C['amber']};text-transform:uppercase;letter-spacing:.12em}}
#timer{{position:absolute;left:0;right:0;top:{WT - 100}px;margin:auto;width:max-content;display:flex;align-items:center;gap:18px;
  padding:18px 32px;border-radius:999px;background:rgba(255,255,255,.07);border:1.5px solid rgba(183,156,255,.3);opacity:0}}
#timer .ic{{font-size:38px}} #timer b{{font-size:52px;font-weight:900;letter-spacing:-.02em;font-variant-numeric:tabular-nums;min-width:120px}}
#timer .lb{{font-size:28px;color:{C['muted']};font-weight:600}}
"""
    js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f}, FL="{fl}", NFL={nfl}, VW={WW}, VH={VH}, VH0={VH0};
const LW={LW}, LH={LH};
// lupa: [vt, [x,y,zoom]] (tempo da gravação)
const LUPA=[[0,[.5,.42,1.5]],[56,[.5,.42,1.5]],[58.5,[.66,.4,1.35]],[92,[.66,.4,1.35]],[93,[.5,.68,1.6]],[95.0,[.5,.68,1.6]],[95.4,[.4,.2,1.6]],
            [99.9,[.4,.2,1.6]],[100.8,[.35,.72,1.6]],[111,[.35,.72,1.6]],[112.2,[.45,.7,1.5]],[116,[.45,.7,1.5]]];
function lupa(vt){{ let i=1; while(i<LUPA.length-1 && vt>LUPA[i][0]) i++;
  const [a,fa]=LUPA[i-1],[b,fb]=LUPA[i]; const k=ease((vt-a)/Math.max(.01,b-a));
  return [0,1,2].map(j=>fa[j]+(fb[j]-fa[j])*k); }}
window.R=async function(t){{
  const [n1a,n1b]=S.N1,[n2a,n2b]=S.N2,[n3a,n3b]=S.N3,[n4a,n4b]=S.N4,[n5a,n5b]=S.N5,[n6a,n6b]=S.N6;
  const ps=[];
  // gancho
  const h1=ease((t-(n1a-.05))/.45), h2=ease((t-(U.s2-.1))/.45);
  $('h1').style.cssText=`opacity:${{h1}};transform:translateY(${{(1-h1)*40}}px)`;
  $('h2').style.cssText=`opacity:${{h2}};transform:translateY(${{(1-h2)*40}}px)`;
  const ho=cl((t-(U.s3-.35))/.35); $('hook').style.opacity=1-ho; $('hook').style.transform=`translateY(${{-ho*60}}px)`;
  $('hook2').style.opacity=io(t,U.s3-.05,n2a+.15,.35,.25);
  // janela entra / sai
  const pe=ease((t-(U.s3-.1))/.6), ck=cta(t,n6a);
  $('win').style.opacity=pe*(1-ck); $('win').style.transform=`translateY(${{(1-pe)*700+ck*300}}px) scale(${{1-ck*.1}})`;
  $('top').style.opacity=1-ck;
  $('timer').style.opacity=cl((t-n2a)/.3)*(1-ck);
  // tempo de vídeo (real da gravação) por trecho de narração
  const ta=n4a-.05+.3*(n5a-n4a);   // corte seco: pula o carregamento (spinner) entre o foguete e a página da campanha
  const vt=pw([[0,1.9],[n2a,1.9],[n3a-.05,58],[n4a-.05,92],[ta,95.0],[ta+.01,95.45],[n5a-.05,102],[n5b,113],[T,113]],t);
  const fr=Math.min(NFL,Math.max(1,Math.round(vt*30)+1));
  setImg($('sv'),`${{FL}}/${{pad(fr)}}.jpg`,ps);
  setImg($('sl'),$('sv').src,ps);
  const [lx,ly,lz]=lupa(vt), lw=VW*lz, lh=VH0*lz;
  $('sl').style.width=lw+'px'; $('sl').style.height=lh+'px';
  $('sl').style.transform=`translate(${{cl(LW/2-lx*lw,LW-lw,0)}}px,${{cl(LH/2-ly*lh,LH-lh,0)}}px)`;
  $('ltag').textContent = vt<58 ? 'cria a conta' : vt<92.5 ? 'a regra' : vt<95.2 ? 'ativar' : vt<100 ? 'campanha ativa' : vt<111.6 ? 'nome e link' : 'QR Code';
  const lin=back((t-(n2a+.3))/.5);
  $('lens').style.opacity=cl((t-(n2a+.3))/.15)*(1-ck); $('lens').style.transform=`scale(${{.85+.15*lin}})`;
  const sec=Math.round(Math.max(0,vt-1.9)); $('tt').textContent=`${{Math.floor(sec/60)}}:${{String(sec%60).padStart(2,'0')}}`;
  const fim=cl(1-Math.abs(t-(n5b-.4))/.6); $('tt').style.color=fim>0?`rgb(255,${{194+61*(1-fim)}},${{77+178*(1-fim)}})`:'#fff';
  // legendas
  show('c2',t,n2a,n3a+.05); show('c3',t,n3a+.05,n4a); show('c4',t,n4a,n5a); show('c5',t,n5a,n6a-.1);
  // destaques
  pop('rule',t,(U.regra||n3a+1.0),n4a,-2);
  pop('ativa',t,n4a+.25,n5a,2);
  pop('qrok',t,(U.qr||n5a+.8),n6a-.1,-2);
  await Promise.all(ps);
}};
"""
    return page(body, css, js), total


if __name__ == "__main__":
    main(build, "reel_02_do_zero.mp4", sys.argv)
