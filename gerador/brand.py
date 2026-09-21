# -*- coding: utf-8 -*-
"""
Sistema visual pontua.club — trocar as cores aqui muda todo o lote de artes.
Formato de saída: 1080x1350 (4:5), o mais alto permitido no feed do Instagram.
"""

BRAND = {
    "ink":        "#0D0A18",   # fundo escuro
    "ink_soft":   "#191330",
    "primary":    "#5B34E8",   # roxo principal
    "primary_lt": "#9C7BFF",
    "accent":     "#FFC24D",   # âmbar — carimbo/ponto/recompensa
    "accent_dp":  "#E8A020",
    "paper":      "#F5F3FF",   # fundo claro
    "paper_2":    "#FFFFFF",
    "loss":       "#FF6B6B",   # perda / erro
    "gain":       "#2ED47A",   # ganho / acerto
    "muted_d":    "#A79FC4",   # texto secundário em fundo escuro
    "muted_l":    "#5B5473",   # texto secundário em fundo claro
}

HANDLE = "@pontua.club"
SITE = "pontua.club"

W, H = 1080, 1350

FONT_CSS = """
@font-face{font-family:'Inter';src:url('file://{IDIR}/inter-latin-400-normal.woff2') format('woff2');font-weight:400;font-display:block}
@font-face{font-family:'Inter';src:url('file://{IDIR}/inter-latin-500-normal.woff2') format('woff2');font-weight:500;font-display:block}
@font-face{font-family:'Inter';src:url('file://{IDIR}/inter-latin-600-normal.woff2') format('woff2');font-weight:600;font-display:block}
@font-face{font-family:'Inter';src:url('file://{IDIR}/inter-latin-700-normal.woff2') format('woff2');font-weight:700;font-display:block}
@font-face{font-family:'Inter';src:url('file://{IDIR}/inter-latin-800-normal.woff2') format('woff2');font-weight:800;font-display:block}
@font-face{font-family:'Inter';src:url('file://{IDIR}/inter-latin-900-normal.woff2') format('woff2');font-weight:900;font-display:block}
@font-face{font-family:'Lora';src:url('file://{LORA}') format('{LORA_FMT}');font-weight:400;font-style:italic;font-display:block}
"""
