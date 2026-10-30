# Automação do Instagram @pontua.club — como funciona (v5 · 30/10/2026: Reels)

Tudo roda na nuvem. **Não depende do PC do Rafael.**

```
Rotina do Claude (seg e qui 07:41 SP)          GitHub Action "renderizar fila"          Make "publicar fila"
 cria o post, renderiza, faz QA ──► Make ──►  pega pendentes, renderiza, commita  ──►  publica ter/qui/sáb 09:00 SP
 grava status "renderizar"+código    data      com GITHUB_TOKEN, confere as URLs,       (status "agendado")
                                     store     avisa a ponte → status "agendado"
```

| Peça | Onde | O que faz |
|---|---|---|
| Rotina de conteúdo | Tarefa agendada do Claude "pontua · conteúdo do Instagram", **seg e qui 07:41 SP** | Mantém posts para os **próximos 15 dias**: cria, renderiza localmente, faz o QA visual e grava no Make com `status: "renderizar"` e o código do gerador no campo `gerador`. Se a sessão tiver permissão de push (repo anexado à tarefa), publica direto e grava `agendado`. |
| Ponte | Make · cenário 6780455 "pontua · ponte GitHub" (webhook) | `acao=pendentes` devolve o próximo post a renderizar · `acao=pronto` muda para `agendado` · `acao=falhou` marca `erro_render`. |
| Renderização/hospedagem | `.github/workflows/renderizar.yml` + `automacao/render_fila.py` (todo dia 06:17 SP e seg/qui 08:37, 10:37, 14:37 SP) | Renderiza com o mesmo código, commita `artes/`, `gerador/` e `fontes/inventario.json`, espera as URLs `raw.githubusercontent.com` responderem 200 e avisa a ponte. Usa o token da própria Action (não expira, sem segredo). |
| Fila | Make · data store `pontua_fila_instagram` (154610) | `renderizar → agendado → publicado`, ou `erro_render` / `erro` / `pausado` / `removido`. `_rotina_log` = log da última execução da rotina. |
| Publicador | Make · cenário 6350969 (a cada 30 min, 08h–13h SP) | Publica o `agendado` com `quando` vencido; marca `publicado` ou `erro`. Três rotas pelo campo `tipo`: `carrossel`, `imagem` e `reel` (módulo *Create a reel post*, `share_to_feed` ligado, capa = quadro `capa_ms`). |
| Vídeos dos Reels | Branch órfã `reels` deste repo | Cópias de publicação `reel_NN.mp4` (H.264 ≤4,5 Mbps, GOP fechado, AAC 128k 48 kHz, faststart) em `https://raw.githubusercontent.com/rafa1106/pontua-midia/reels/reel_NN.mp4`. Branch separada para o `main` continuar leve: `clone --depth 1` e o checkout da Action não baixam os vídeos. |

## Calendário
Posts: Ter (ramo) · Qui (educação) · Sáb (produto/"No automático") às **09:00 SP = 12:00Z**.
Reels: **seg/qua/sex às 11:30 SP = 14:30Z**, keys `rMMDD_*`. Os 25 Reels prontos (pasta `05_reels_finais` do Rafael) estão agendados de 02/11 a 30/12/2026; legendas em `legendas/reels-20261030.json`. A rotina de conteúdo não cria nem mexe em reels, só reporta erro. Regras de conteúdo: `estrategia/guia_conteudo.md`.
Com 15 dias de folga, 2 execuções da rotina por semana e 13 tentativas semanais da Action, várias falhas seguidas ainda não param o feed.

## Arquivos
- `fontes/` — artes-base (cenas IA) + `inventario.json` (disponível/usada/proibida; a Action marca "usada" quando o gerador cita `fontes/ramos/<x>.jpg`).
- `gerador/pMMDD_tema.py` — um gerador por post; inclui a variável `LEGENDA`.
- O webhook da ponte fica no workflow em base64 (o repo é público). Ele só mexe em posts com status `renderizar`; o pior uso indevido possível é liberar um post antes da hora, e o publicador marcaria `erro`, que a rotina reprocessa.

## Manutenção que já está coberta
- GitHub desativa workflows agendados de repositórios públicos após 60 dias sem atividade; cada post renderizado é um commit, então isso não acontece enquanto a rotina estiver ativa.
- O runner está fixo em `ubuntu-24.04` para a renderização não mudar sozinha.
- Consumo do Make (plano Free, 1.000 operações/mês): publicador ~340/mês (08h–13h) + ponte ~200/mês + reels ~40/mês. O plano Free permite só 2 cenários: por isso os Reels usam o mesmo publicador.
- Rótulo de IA: o módulo do Make não tem o campo `is_ai_generated` da API. Os Reels com cenas de IA (10–19) trazem na legenda "Cenas ilustrativas criadas com IA."

## O que só o Rafael pode fazer
- **Renovar a conexão do Instagram no Make a cada ~60 dias** (regra da Meta): make.com → Connections → `pontua-instagram` → Reauthorize. Vence em **20/11/2026**; a rotina avisa por e-mail/push 15 dias antes.
- Segurar um post: no data store, mude `status` para `pausado` antes das 9h do dia.
