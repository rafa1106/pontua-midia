"""Junta 3 faixas (1152xH) capturadas do Chrome numa imagem 1152x2048.
Faixas nos deslocamentos 0, H e 2048-H. Uso: costura.py saida.png H t1 t2 t3"""
import sys
from PIL import Image
out, H, a, b, c = sys.argv[1], int(sys.argv[2]), *sys.argv[3:6]
im = Image.new("RGB", (1152, 2048))
im.paste(Image.open(a).convert("RGB").crop((0, 0, 1152, H)), (0, 0))
im.paste(Image.open(b).convert("RGB").crop((0, 0, 1152, H)), (0, H))
o3 = 2048 - H
im.paste(Image.open(c).convert("RGB").crop((0, 2 * H - o3, 1152, H)), (0, 2 * H))
im.save(out)
print(out, im.size)
