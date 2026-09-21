# pontua-midia

Mídia pública do Instagram @pontua.club. Este repositório existe porque a API do
Instagram exige que as imagens estejam em uma URL pública — o GitHub serve isso.

- `artes/` — JPEGs 1080x1350 prontos para publicar (referenciados pela fila no Make)
- `gerador/` — código que gera as artes (HTML → JPEG via Chromium). Cores em `brand.py`.
- `legendas/` — legenda, primeiro comentário e alt text de cada post

Publicação: cenário "pontua · publicar fila do Instagram" no Make lê o data store
`pontua_fila_instagram` e publica os posts vencidos. Gerido pelo Claude.
