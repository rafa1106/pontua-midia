# -*- coding: utf-8 -*-
"""Realce de legibilidade das telas gravadas (UI escura): levanta sombras e meios-tons,
um pouco de contraste local e nitidez — sem mudar cores/layout do app.
Uso: python3 realce.py <entrada_dir> <saida_dir> [gamma]"""
import sys
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter


def lut(g=0.8, lift=6):
    t = []
    for x in range(256):
        y = 255 * ((x / 255) ** g)
        y = lift + y * (255 - lift) / 255
        t.append(max(0, min(255, round(y))))
    return t * 3


def realca(im, g=0.8):
    im = im.convert("RGB").point(lut(g))
    im = ImageEnhance.Contrast(im).enhance(1.05)
    im = ImageEnhance.Color(im).enhance(1.10)
    return im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=70, threshold=2))


if __name__ == "__main__":
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    g = float(sys.argv[3]) if len(sys.argv) > 3 else 0.8
    dst.mkdir(parents=True, exist_ok=True)
    for f in sorted(src.glob("*.jpg")):
        realca(Image.open(f), g).save(dst / f.name, quality=92)


def realca_local(im, clip=2.5, g=0.9, tiles=8):
    """Realce com contraste local (CLAHE na luminância) — para telas com texto de baixo contraste
    (cards verdes, textos cinza sobre fundo escuro). Cores preservadas (só mexe no canal L)."""
    import cv2, numpy as np
    a = np.array(im.convert("RGB"))
    lab = cv2.cvtColor(a, cv2.COLOR_RGB2LAB)
    l, A, B = cv2.split(lab)
    l = cv2.createCLAHE(clipLimit=clip, tileGridSize=(tiles, tiles)).apply(l)
    return realca(Image.fromarray(cv2.cvtColor(cv2.merge((l, A, B)), cv2.COLOR_LAB2RGB)), g)
