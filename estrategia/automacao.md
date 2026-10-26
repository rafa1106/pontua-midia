# Automação do Instagram @pontua.club — como funciona (v3 · 26/10/2026)

Tudo roda na nuvem. **Não depende do PC do Rafael** (até 19/10 dependia, e foi por isso que a fila secou depois de 08/10).

| Peça | Onde | O que faz |
|---|---|---|
| Rotina de conteúdo | Tarefa agendada do Claude "pontua · conteúdo do Instagram", **seg e qui 07:41 (SP)** | Lê a fila, cria os posts que faltam para os **próximos 15 dias**, renderiza, faz o controle de qualidade, publica as artes neste repo e grava os registros na fila. |
| Hospedagem das artes | Este repo (`artes/`) → `raw.githubusercontent.com` | O Instagram exige URL pública da imagem. |
| Fila | Make · data store `pontua_fila_instagram` (154610) | 1 registro por post (`status`: agendado → publicado / erro / pausado / removido). |
| Publicador | Make · cenário 6350969 (a cada 30 min, 08h–19h) | Publica o registro `agendado` com `quando` vencido e marca `publicado` ou `erro`. |

## Calendário
Ter (ramo) · Qui (educação) · Sáb (produto/"No automático") às **09:00 SP = 12:00Z**. Regras de conteúdo: `estrategia/guia_conteudo.md` (obrigatório).
Com 15 dias de folga e 2 execuções por semana, a rotina pode falhar até ~4 vezes seguidas sem o feed parar.

## Arquivos
- `fontes/ramos/*.jpg`, `fontes/gerais/*.jpg` — artes-base (cenas IA). `fontes/inventario.json` diz o que está disponível, usado ou proibido.
- `gerador/pMMDD_tema.py` — um gerador por post (layouts de `render2.py`). `legendas/lote-AAAAMMDD.json` — legendas de cada lote.

## O que só o Rafael pode fazer
- **Renovar a conexão do Instagram no Make a cada ~60 dias** (exigência da Meta). Make → Connections → `pontua-instagram` → Reauthorize. Vence em **20/11/2026**. A rotina avisa por e-mail/push a partir de 15 dias antes.
- Segurar um post: no data store, mude `status` para `pausado` antes das 9h do dia.
