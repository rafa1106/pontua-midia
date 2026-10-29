# -*- coding: utf-8 -*-
"""Reel 18 — "Quanto custa começar um programa de fidelidade? Zero." (série Dor do balcão, viés preço zero).

Tipografia animada + 3 inserts curtos e reais do app: o cartão no celular do cliente (fc_card do Reel 16),
o cadastro pelo QR Code (gravação do fluxo 02, a mesma do Reel 13) e o aviso real de carimbo no WhatsApp.
Só recursos que o grátis entrega; sem preço, sem nome de plano e sem limites (ficam no site).

Uso: python3 reel_custazero.py <pasta> [preview t1,t2,...]
  <pasta>/audio (reels/18_custa_zero) · <pasta>/fq (quadros do cadastro, 620 px) · <pasta>/fc_card.jpg
"""
import json, sys
from reel_base import *
from reel_papel import CTA_GRATIS, NOTIF

PWD = 640                     # largura dos inserts
K = PWD / 620
PY = 520
PHT = 1010                    # altura visível do insert

ITENS = [("📱", "Cartão de carimbos no celular"), ("📲", "Cadastro por QR Code, sem app"),
         ("💬", "Avisos no WhatsApp"), ("💳", "Sem cartão de crédito"), ("⚡", "No ar no mesmo dia")]


def build(work):
    S, U, total = marcas(work)
    fq = (work / "fq").as_uri()
    nfq = len(list((work / "fq").glob("*.jpg")))
    card = (work / "fc_card.jpg").as_uri()
    lis = "".join(f'<div class="it" id="i{j}"><span class="ck">✓</span><span class="ic{" wa" if ic == "wa" else ""}">'
                  f'{WA_ICON if ic == "wa" else ic}</span><span class="tx">{tx}</span></div>' for j, (ic, tx) in enumerate(ITENS))
    body = f"""{BG}{TOP}
<div class="cap" id="q"><div class="l q">Quanto custa começar<br>um programa<br>de fidelidade?</div></div>
<div id="zero"><b>Zero.</b></div>
<div class="cap step" id="c2"><span class="n">📱</span><div>Cartão de carimbos<br><span class="hl">no celular do cliente</span></div></div>
<div class="cap step" id="c3"><span class="n">📲</span><div>Cadastro pelo QR Code,<br><span class="hl">sem baixar app</span></div></div>
<div class="cap step" id="c4"><span class="n wa">{WA_ICON}</span><div>Avisos no WhatsApp<br><span class="hl">que ele já usa</span></div></div>
<div class="pn" id="p1"><img src="{card}"></div>
<div class="pn" id="p2"><img id="vq" src="{fq}/0001.jpg"></div>
<div id="tela">telas reais do app</div>
{wa_card("wa", "Café da Esquina", NOTIF, (), top=640)}
<div class="chip" id="todo">todo dia no celular dele</div>
<div class="cap" id="c5"><div class="l mid">Tudo isso,<br><span class="am">de graça:</span></div></div>
<div id="lista">{lis}</div>
<div class="cap" id="c6"><div class="l mid">Começar<br><span class="am">não custa nada.</span></div></div>
<div id="fonte">efeito do preço zero · Shampanier, Mazar &amp; Ariely, 2007</div>
{CTA_GRATIS}"""
    css = f"""
.cap .l{{font-size:96px;line-height:1.04}}
.cap .l.q{{font-size:92px}}
.cap .l.mid{{font-size:92px}}
#q{{top:330px}} #c2,#c3,#c4{{top:240px}} #c2 div,#c3 div,#c4 div{{font-size:56px}} #c5,#c6{{top:250px}}
#zero{{position:absolute;left:0;right:0;top:860px;text-align:center;opacity:0}}
#zero b{{display:inline-block;font-size:300px;font-weight:900;letter-spacing:-.06em;color:{C['amber']};
  text-shadow:0 0 120px rgba(255,194,77,.55),0 20px 60px rgba(0,0,0,.5)}}
.pn{{position:absolute;left:{(W - PWD) // 2}px;top:{PY}px;width:{PWD}px;height:{PHT}px;border-radius:40px;overflow:hidden;opacity:0;background:#1A1E2C;
  box-shadow:0 0 0 2px rgba(183,156,255,.45),0 0 110px rgba(123,77,255,.5),0 40px 90px rgba(0,0,0,.6)}}
.pn img{{position:absolute;left:0;width:100%}}
#p1 img{{top:{-round(70 * K)}px}} #p2 img{{top:0}}
.pn::after{{content:"";position:absolute;left:0;right:0;bottom:0;height:150px;background:linear-gradient(rgba(26,30,44,0),#1A1E2C 85%)}}
#tela{{position:absolute;left:0;right:0;top:{PY + PHT + 20}px;text-align:center;font-size:28px;font-weight:700;color:rgba(230,224,255,.75);opacity:0}}
#wa{{z-index:4}}
#todo{{left:0;right:0;margin:auto;width:max-content;top:1240px}}
#lista{{position:absolute;left:90px;right:90px;top:560px;display:flex;flex-direction:column;gap:26px}}
.it{{display:flex;align-items:center;gap:24px;padding:26px 30px;border-radius:28px;background:rgba(19,14,40,.78);border:2px solid rgba(183,156,255,.3);opacity:0;
  box-shadow:0 18px 50px rgba(0,0,0,.4)}}
.it .ck{{flex:0 0 64px;height:64px;border-radius:50%;background:{C['gain']};color:#0B2A18;display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:900}}
.it .ic{{flex:0 0 56px;height:56px;display:flex;align-items:center;justify-content:center;font-size:44px}}
.it .ic img{{width:48px;height:48px}}
.it .ic.wa{{border-radius:16px;background:{C['green']}}} .it .ic.wa svg{{width:36px;height:36px}}
.it .tx{{font-size:44px;white-space:nowrap;font-weight:800;letter-spacing:-.02em}}
#fonte{{position:absolute;left:0;right:0;top:1580px;text-align:center;font-size:26px;font-weight:600;color:rgba(230,224,255,.7);opacity:0}}
#cta{{z-index:5}}
#cta .semcc{{font-size:38px;font-weight:800;color:{C['gain']};margin-top:-20px}}
"""
    js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f}, FQ="{fq}", NFQ={nfq};
window.R=async function(t){{
  const N=[1,2,3,4,5,6].map(i=>S['N'+i]);
  const [n1a,n1b]=N[0],[n2a,n2b]=N[1],[n3a,n3b]=N[2],[n4a,n4b]=N[3],[n5a,n5b]=N[4],[n6a]=N[5];
  const z0=U['N1.2']||(n1b-.6), ctaT=U['N6.2']||(n6a+2);
  const ps=[];
  // N1: a pergunta e o "Zero." gigante
  const q=ease((t-.05)/.45); $('q').style.opacity=q*(1-cl((t-(n2a-.25))/.25)); $('q').style.transform=`translateY(${{(1-q)*40}}px)`;
  const zk=back((t-(z0-.05))/.45), zo=cl((t-(n2a-.2))/.25);
  $('zero').style.opacity=cl((t-(z0-.05))/.1)*(1-zo); $('zero').style.transform=`scale(${{.6+.4*zk}}) rotate(${{(1-zk)*-8}}deg)`;
  // N2: o cartão real no celular do cliente
  show('c2',t,n2a,n3a-.05);
  const p1=ease((t-(n2a+.05))/.5), p1o=cl((t-(n3a-.25))/.25);
  $('p1').style.opacity=cl((t-(n2a+.05))/.2)*(1-p1o); $('p1').style.transform=`translateY(${{(1-p1)*400-p1o*80}}px) scale(${{1-.03*p1o}})`;
  // N3: o cadastro real pelo QR (gravação acelerada)
  show('c3',t,n3a,n4a-.05);
  const p2=ease((t-(n3a+.05))/.5), p2o=cl((t-(n4a-.25))/.25);
  $('p2').style.opacity=cl((t-(n3a+.05))/.2)*(1-p2o); $('p2').style.transform=`translateY(${{(1-p2)*400-p2o*80}}px) scale(${{1-.03*p2o}})`;
  const vt=pw([[n3a,0],[n3a+.6,0],[n4a-.3,19.9]],t);
  setImg($('vq'),`${{FQ}}/${{pad(Math.min(NFQ,Math.max(1,Math.round(vt*30)+1)))}}.jpg`,ps);
  $('tela').style.opacity=Math.max(io(t,n2a+.3,n3a-.05,.3,.2),io(t,n3a+.3,n4a-.05,.3,.2));
  // N4: o aviso real no WhatsApp
  show('c4',t,n4a,n5a-.05);
  const wi=back((t-(n4a+.1))/.5), wo=cl((t-(n5a-.25))/.3);
  $('wa').style.opacity=cl((t-(n4a+.1))/.15)*(1-wo); $('wa').style.transform=`translateY(${{(1-wi)*-220-wo*160}}px) scale(${{.96+.04*wi}})`;
  pop('todo',t,n4a+.5*(n4b-n4a),n5a-.05,-2);
  // N5: tudo isso, de graça (3 já vistos + 2 da fala)
  show('c5',t,n5a,n6a-.05);
  const d5=n5b-n5a, tq=[n5a+.15,n5a+.35,n5a+.55,n5a+.1*d5+.6,n5a+.62*d5];
  tq.forEach((a,j)=>{{ const k=back((t-a)/.4), e=$('i'+j); e.style.opacity=cl((t-a)/.12)*(1-cl((t-(n6a-.2))/.2));
    e.style.transform=`translateX(${{(1-k)*-120}}px)`;
    e.querySelector('.ck').style.transform=`scale(${{back((t-(a+.2))/.35)}})`; }});
  // N6: começar não custa nada + CTA
  show('c6',t,n6a,ctaT);
  $('fonte').style.opacity=io(t,n6a+.4,ctaT,.3,.2);
  const ck=cta(t,ctaT); $('top').style.opacity=1-ck;
  await Promise.all(ps.concat([...document.images].map(i=>i.decode().catch(()=>{{}}))));
}};
"""
    return page(body, css, js), total


if __name__ == "__main__":
    main(build, "reel_18_custa_zero.mp4", sys.argv)
