# -*- coding: utf-8 -*-
"""Reels 08 e 09 — área "Falar com clientes" (envios prontos por regra; saem por SMS e e-mail).

  python3 reel_falar.py sumidos <pasta> [preview t1,t2]   # fluxo 06 (Açaí da Praça)
  python3 reel_falar.py acoes   <pasta> [preview t1,t2]   # fluxo 05, 2ª parte (Pet Feliz)
  <pasta>/fl  quadros do lojista.mp4 (1200 px) com realce local · <pasta>/audio  narração + alinhamento

A janela mostra a tela inteira do modal (recorte simétrico de 9% de cada lado — o modal ocupa 10%–90%).
A lupa segue uma lista de cenas: (início, fim, [fx, fy, zoom], etiqueta, anel[x0,y0,x1,y1] ou None).
"""
import json, sys
from reel_base import *

WW = 1000
VH0 = round(WW * 900 / 1440)
Z = 1.22
VH = round(VH0 * Z)
WT = 520
LW, LH = 920, 330

SMS = {
    "sumidos": [("Açaí da Praça", "Oi Maria! Sentimos sua falta na Açaí da Praça. Que tal passar aqui hoje?", "convite (prévia do sistema, nome de exemplo)")],
    "acoes": [
        ("Pet Feliz", "Oi Eduardo Alves! Hoje tem carimbo em dobro na Pet Feliz. Te esperamos!", "carimbo em dobro"),
        ("Pet Feliz", "Oi Vinicius Barbosa! Voce ganhou 1 carimbo de presente na Pet Feliz. Aproveite e volte sempre!", "mimo de aniversário"),
        ("Pet Feliz", "Oi Eduardo Alves! Voce ganhou 1 carimbo de presente na Pet Feliz. Aproveite e volte sempre!", "carimbo surpresa"),
    ],
}

CAPS = {
    "sumidos": [("1", "O painel avisa", "quem sumiu", "hl"), ("2", "Convite pronto", "em um clique", "am"),
                ("3", "Ajusta, confere", "e envia", "hl"), ("✉", "Sai por", "SMS e e-mail", "hl")],
    "acoes": [("1", "Carimbo em dobro", "pra quem sumiu", "am"), ("2", "Mimo de", "aniversário", "hl"),
              ("3", "Carimbo surpresa", "perto do prêmio", "am"), ("✓", "Confere e envia", "SMS e e-mail", "hl")],
}

HOOK = {
    "sumidos": ('Cliente <span class="am">sumiu?</span>', 'O pontua percebe<br>e monta <span class="hl">o convite.</span>'),
    "acoes": ('Semana <span class="am">parada?</span>', 'Ações <span class="hl">prontas</span><br>pra você.'),
}


def js_sumidos():
    # tempos de vídeo (s) e cenas da lupa, em função das falas
    return r"""
  const d3=n3b-n3a, tcp=n3a+.32*d3, tqr=n3a+.70*d3, ttx=n3a+.84*d3, d4=n4b-n4a, tre=n4a+.38*d4, ten=n4a+.76*d4;
  const vt=pw([[n2a,.6],[n2b,4.6],[n3a,4.8],[n3a+.9,6.2],[n3a+1.5,8.4],[tcp,9.6],[tqr-.05,12.6],[tqr,14.9],[ttx-.05,16.4],[ttx,21.4],
               [n3b,22.6],[n4a,27.2],[tre-.05,30.0],[tre,35.3],[ten-.05,36.8],[ten,38.4],[n4b,40.3],[T,40.8]],t);
  const fx = vt<6.0 ? .58 : .5;
  const CENAS=[
    [n2a+.4, n3a+.3, [.39,.93,2.0], 'sumidos há 30+ dias', [.455,.94,.575,.97]],
    [n3a+1.5, tqr, [.66,.30,1.9], 'carimbo de presente', [.43,.215,.89,.28]],
    [tqr, ttx, [.66,.30,1.9], 'quem recebe', [.665,.175,.895,.25]],
    [ttx, n4a, [.26,.49,2.2], 'o texto (prévia)', [.17,.445,.335,.545]],
    [n4a, tre, [.66,.51,1.9], 'ajusta o texto', [.44,.49,.89,.56]],
    [tre, ten, [.66,.42,1.55], 'resumo e custo', null],
  ];
  const fim=ten, okT=ten+.25;   // depois do "envia": selo de enviado
"""


def js_acoes():
    return r"""
  const d2=n2b-n2a, tsu=n2a+.45*d2, d3=n3b-n3a, tan=n3a+.62*d3, d4=n4b-n4a, tpe=n4a+.42*d4, d5=n5b-n5a, tres=n5a, tenv=n5a+.42*d5;
  const vt=pw([[n2a,50.6],[tsu-.05,53.8],[tsu,58.6],[n2b,60.2],[n3a-.01,60.2],[n3a,77.6],[tan-.05,86.0],[tan,91.6],[n3b,93.2],
               [n4a-.01,93.2],[n4a,113.4],[tpe-.05,117.5],[tpe,124.6],[n4b,126.2],[tres-.01,126.2],[tres,134.0],[tenv-.05,135.6],[tenv,137.4],[T,139.0]],t);
  const fx=.5;
  const CENAS=[
    [n2a+.2, tsu, [.66,.30,1.9], 'carimbo em dobro', [.445,.245,.65,.30]],
    [tsu, n3a, [.66,.30,1.9], 'pra quem sumiu', [.665,.175,.895,.25]],
    [n3a, tan, [.66,.40,1.9], 'mimo de aniversário', [.44,.49,.89,.545]],
    [tan, n4a, [.66,.34,1.9], 'aniversariantes do mês', [.665,.27,.895,.335]],
    [n4a, tpe, [.66,.40,1.9], 'carimbo surpresa', [.44,.49,.89,.545]],
    [tpe, n5a, [.66,.40,1.9], 'perto do prêmio', [.665,.465,.895,.535]],
    [tres, tenv, [.66,.42,1.55], 'resumo', null],
  ];
  const fim=tenv, okT=tenv+.3;
"""


def build_for(tipo):
    def build(work):
        S, U, total = marcas(work)
        fl = (work / "fl").as_uri()
        nfl = len(list((work / "fl").glob("*.jpg")))
        h1, h2 = HOOK[tipo]
        caps = "".join(f'<div class="cap step" id="c{i + 2}"><span class="n">{n}</span><div>{a}<br><span class="{c}">{b}</span></div></div>'
                       for i, (n, a, b, c) in enumerate(CAPS[tipo]))
        sms = "".join(f'<div class="sms" id="s{i}"><div class="hd"><span class="ic">✉</span><span>SMS · <b>{rem}</b></span><span class="ev">{ev}</span></div>'
                      f'<div class="tx">{tx}</div></div>' for i, (rem, tx, ev) in enumerate(SMS[tipo]))
        n_ok = "8 clientes" if tipo == "sumidos" else "9 clientes"
        body = f"""{BG}{TOP}
<div class="cap" id="hook"><div class="l" id="h1">{h1}</div><div class="l small2" id="h2">{h2}</div></div>
{caps}
<div id="win"><div class="bar"><i></i><i></i><i></i><span class="url">🔒 pontua.club</span></div>
  <div class="vp"><img id="sw" src="{fl}/0001.jpg"></div></div>
<div id="lens"><img id="sl" src="{fl}/0001.jpg"><div id="lring"></div></div><div id="ltag"></div>
<div class="badge" id="ok" style="left:0;right:0;margin:auto;width:max-content;top:1200px">✓ Envio a caminho · {n_ok}</div>
<div id="stack" style="top:{660 if tipo == "sumidos" else 430}px">{sms}</div>
<div id="plano"><div class="p1">Disponível</div><div class="p2">a partir do Basic</div><div class="p3">R$ 39/mês</div></div>
{CTA}"""
        css = f"""
#hook{{top:600px}}
.cap .l.small2{{font-size:66px;font-weight:800;letter-spacing:-.035em;line-height:1.08;margin-top:44px;color:#EDE8FF}}
#win{{position:absolute;left:{(W-WW)//2}px;top:{WT}px;width:{WW}px;border-radius:26px;overflow:hidden;background:#0F1220;opacity:0;
  box-shadow:0 0 0 2px rgba(183,156,255,.45),0 0 110px rgba(123,77,255,.5),0 50px 90px rgba(0,0,0,.6);transform-origin:50% 0}}
#win .bar{{height:58px;background:#1C1A30;display:flex;align-items:center;gap:12px;padding:0 22px}}
#win .bar i{{width:16px;height:16px;border-radius:50%;background:#3C3760}}
#win .url{{margin-left:22px;flex:1;height:36px;border-radius:12px;background:#0F0D1E;color:#B9B2D9;font-size:22px;display:flex;align-items:center;padding-left:18px}}
#win .vp{{position:relative;width:{WW}px;height:{VH}px;overflow:hidden}}
#win .vp img{{position:absolute;left:0;top:0;width:{WW}px;height:{VH0}px;transform-origin:0 0}}
#lens{{position:absolute;left:0;right:0;margin:auto;top:1150px;width:{LW}px;height:{LH}px;border-radius:30px;overflow:hidden;background:#0F1220;opacity:0;
  border:4px solid {C['amber']};box-shadow:0 30px 80px rgba(0,0,0,.6),0 0 70px rgba(255,194,77,.45);transform-origin:50% 0}}
#lens img{{position:absolute;left:0;top:0;transform-origin:0 0}}
#ltag{{position:absolute;left:{(W-LW)//2+26}px;top:1114px;padding:10px 22px;border-radius:999px;background:rgba(13,10,24,.9);border:1.5px solid rgba(183,156,255,.5);
  font-size:26px;font-weight:900;color:{C['amber']};text-transform:uppercase;letter-spacing:.12em;opacity:0;z-index:5}}
#lring{{position:absolute;border-radius:16px;border:4px solid {C['amber']};box-shadow:0 0 30px rgba(255,194,77,.7);opacity:0}}
#stack{{position:absolute;left:70px;right:70px;top:470px}}
.sms{{margin-bottom:26px;padding:26px 30px;border-radius:30px;background:rgba(248,246,255,.98);color:#141024;opacity:0;
  box-shadow:0 26px 70px rgba(0,0,0,.5),0 0 60px rgba(155,120,255,.35)}}
.sms .hd{{display:flex;align-items:center;gap:14px;font-size:26px;color:#5B5473;font-weight:600}} .sms .hd b{{color:#141024}}
.sms .ic{{width:46px;height:46px;border-radius:13px;background:#5B34E8;color:#fff;display:flex;align-items:center;justify-content:center;font-size:26px}}
.sms .ev{{margin-left:auto;padding:6px 16px;border-radius:999px;background:#EDE8FF;color:#4A2BC8;font-size:21px;font-weight:800;text-transform:uppercase;letter-spacing:.05em;white-space:nowrap}}
.sms .tx{{font-size:{40 if tipo == 'sumidos' else 34}px;line-height:1.36;margin-top:14px;color:#2A2440}}
#plano{{position:absolute;left:0;right:0;margin:auto;width:max-content;top:1330px;padding:36px 64px;border-radius:36px;text-align:center;opacity:0;
  background:linear-gradient(135deg,{C['violet2']},{C['violet']});box-shadow:0 30px 80px rgba(0,0,0,.55),0 0 90px rgba(123,77,255,.8)}}
#plano .p1{{font-size:32px;font-weight:700;color:#E6E0FF}} #plano .p2{{font-size:70px;font-weight:900;letter-spacing:-.035em;margin-top:6px}}
#plano .p3{{font-size:38px;font-weight:800;color:{C['amber']};margin-top:4px}}
"""
        js = f"""
const S={json.dumps(S)}, U={json.dumps(U)}, T={total:.3f}, FL="{fl}", NFL={nfl};
const VW={WW}, VH={VH}, VH0={VH0}, LW={LW}, LH={LH}, Z={Z};
window.R=async function(t){{
  const [n1a,n1b]=S.N1,[n2a,n2b]=S.N2,[n3a,n3b]=S.N3,[n4a,n4b]=S.N4,[n5a,n5b]=S.N5,[n6a,n6b]=S.N6;
  const ps=[], q=U['N1.2'], pb=U['N5.2']||(n5b-1.6);
  {js_sumidos() if tipo == "sumidos" else js_acoes()}
  // gancho
  const h1=ease((t-(n1a-.05))/.45), h2=ease((t-(q-.1))/.45);
  $('h1').style.cssText=`opacity:${{h1}};transform:translateY(${{(1-h1)*40}}px)`;
  $('h2').style.cssText=`opacity:${{h2}};transform:translateY(${{(1-h2)*40}}px)`;
  const ho=cl((t-(n2a-.45))/.35); $('hook').style.opacity=1-ho; $('hook').style.transform=`translateY(${{-ho*60}}px)`;
  const ck=cta(t,n6a); $('top').style.opacity=1-ck;
  // janela: entra no N2, sai quando entram as mensagens (N5)
  const tsms = n5a + (tipo=='acoes' ? .62*(n5b-n5a) : .75);
  const win=ease((t-(n2a-.25))/.55), wout=ease((t-(tsms-.35))/.4);
  $('win').style.opacity=win*(1-wout); $('win').style.transform=`translateY(${{(1-win)*700-wout*100}}px) scale(${{1-wout*.06}})`;
  setImg($('sw'),`${{FL}}/${{pad(Math.min(NFL,Math.max(1,Math.round(vt*30)+1)))}}.jpg`,ps);
  const fxs = fx + 0;  // recorte: .58 tira a barra lateral; .5 centraliza o modal
  const tx=cl(VW/2-fxs*VW*Z,VW-VW*Z,0); $('sw').style.transform=`translate(${{tx}}px,0) scale(${{Z}})`;
  setImg($('sl'),$('sw').src,ps);
  // lupa
  let cena=null; for(const c of CENAS) if(t>=c[0] && t<c[1]) cena=c;
  const lv = cena ? cl((t-cena[0])/.2)*cl((cena[1]-t)/.15+ (CENAS.some(c=>Math.abs(c[0]-cena[1])<.02)?1:0)) : 0;
  const lin=back((t-CENAS[0][0])/.5);
  $('lens').style.opacity=lv; $('lens').style.transform=`scale(${{.85+.15*lin}})`; $('ltag').style.opacity=lv;
  if(cena){{
    const [lx,ly,lz]=cena[2], lw=VW*lz, lh=VH0*lz;
    $('sl').style.width=lw+'px'; $('sl').style.height=lh+'px';
    const ox=cl(LW/2-lx*lw,LW-lw,0), oy=cl(LH/2-ly*lh,LH-lh,0);
    $('sl').style.transform=`translate(${{ox}}px,${{oy}}px)`;
    $('ltag').textContent=cena[3];
    const r=cena[4];
    if(r){{ const ro=cl((t-(cena[0]+.35))/.2);
      $('lring').style.cssText=`opacity:${{ro}};left:${{ox+r[0]*lw-6}}px;top:${{oy+r[1]*lh-6}}px;width:${{(r[2]-r[0])*lw+12}}px;height:${{(r[3]-r[1])*lh+12}}px`; }}
    else $('lring').style.opacity=0;
  }}
  pop('ok',t,okT,tsms+.2,-2);
  // mensagens SMS reais
  [...document.querySelectorAll('.sms')].forEach((e,i)=>{{ const t0=tsms+i*.55, k=back((t-t0)/.5);
    e.style.opacity=cl((t-t0)/.18)*(1-.55*ease((t-(pb-.1))/.4))*(1-ck); e.style.transform=`translateY(${{(1-k)*-100}}px) scale(${{.95+.05*k}})`; }});
  const pl=back((t-pb)/.5), plo=cl((t-(n6a-.3))/.25);
  $('plano').style.opacity=cl((t-pb)/.15)*(1-plo); $('plano').style.transform=`scale(${{pl}})`;
  // legendas
  show('c2',t,n2a,n3a); show('c3',t,n3a,n4a); show('c4',t,n4a,n5a); show('c5',t,n5a,n6a-.1);
  await Promise.all(ps);
}};
const tipo="{tipo}";
"""
        return page(body, css, js), total
    return build


if __name__ == "__main__":
    tipo = sys.argv.pop(1)
    main(build_for(tipo), f"reel_{'08_sumidos' if tipo == 'sumidos' else '09_acoes'}.mp4", sys.argv)
