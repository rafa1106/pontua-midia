# pontua-midia

Mídia pública do Instagram @pontua.club. Este repositório existe porque a API do
Instagram exige que as imagens estejam em uma URL pública — o GitHub serve isso.

- `artes/` — JPEGs 1080x1350 prontos para publicar (referenciados pela fila no Make)
- `gerador/` — código que gera as artes (HTML → JPEG via Chromium). Cores em `brand.py`.
- `legendas/` — legenda, primeiro comentário e alt text de cada post

## Regenerar as artes

```bash
npm install                      # @fontsource/inter e @fontsource/lora
pip install playwright           # Chromium: usa $CHROMIUM_PATH ou /opt/pw-browsers/chromium
cd gerador && python3 c1.py && python3 c2.py && python3 c3.py
```

A saída é determinística: rodar sem mudar `brand.py` reproduz os mesmos JPEGs
byte a byte. Mudou a paleta em `brand.py` → todo o lote muda junto.

Publicação: cenário "pontua · publicar fila do Instagram" no Make lê o data store
`pontua_fila_instagram` e publica os posts vencidos. Gerido pelo Claude.
