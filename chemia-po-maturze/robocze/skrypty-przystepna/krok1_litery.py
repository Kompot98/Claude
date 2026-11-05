"""Krok 1: przesuwa litery części rozdziału 4 (4b->4c ... 4f->4g) poza adresami URL."""
import re, sys
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8").read()
url = re.compile(r"https?://[^\s)>\]]+")
urls = []
def chowaj(m):
    urls.append(m.group(0)); return f"\x00{len(urls)-1}\x00"
t = url.sub(chowaj, t)
mapa = {"b": "c", "c": "d", "d": "e", "e": "f", "f": "g"}
licz = {}
def przesun(m):
    nowa = "4" + mapa[m.group(1)]
    licz[m.group(0)] = licz.get(m.group(0), 0) + 1
    return nowa
t = re.sub(r"(?<![\w.,/])4([b-f])(?![\w])", przesun, t)
t = re.sub(r"\x00(\d+)\x00", lambda m: urls[int(m.group(1))], t)
open(dst, "w", encoding="utf-8").write(t)
print("zmiany:", licz)
