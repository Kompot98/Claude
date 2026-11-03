"""Sprawdza, czy adresy z trzech rejestrów odpowiadają. Wynik do robocze/linki-RRRR-MM-DD.csv.

Użycie: python3 -I skrypty/linki.py [R-001 Z-004 ...]
Korzysta z proxy ze zmiennych środowiska i z pakietu CA w SSL_CERT_FILE lub /root/.ccr/ca-bundle.crt.
"""
import csv
import datetime
import html
import os
import re
import ssl
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wspolne import KORZEN, wczytaj_csv  # noqa: E402


def kontekst():
    ca = os.environ.get("SSL_CERT_FILE") or "/root/.ccr/ca-bundle.crt"
    if os.path.exists(ca):
        return ssl.create_default_context(cafile=ca)
    return ssl.create_default_context()


def sprawdz(url, ctx):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (sprawdzanie linkow)",
                                               "Accept-Language": "pl,en;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=40, context=ctx) as r:
            dane = r.read(400000)
            tytul = ""
            m = re.search(rb"<title[^>]*>(.*?)</title>", dane, re.S | re.I)
            if m:
                tytul = html.unescape(m.group(1).decode("utf-8", "ignore")).strip()[:150]
            return r.status, r.geturl(), tytul
    except urllib.error.HTTPError as e:
        return e.code, url, ""
    except Exception as e:  # noqa: BLE001
        return 0, url, f"{type(e).__name__}: {e}"[:150]


def main(argv):
    ctx = kontekst()
    wybrane = set(argv)
    wiersze = []
    for plik, kol in (("zasoby.csv", "url"), ("zrodla.csv", "url"), ("rysunki.csv", "zrodlo_url")):
        for w in wczytaj_csv(plik):
            if wybrane and w["id"] not in wybrane:
                continue
            kod, koncowy, tytul = sprawdz(w[kol], ctx)
            wiersze.append([w["id"], w[kol], kod, koncowy, tytul])
            print(f"{w['id']}\t{kod}\t{tytul[:70]}\t{w[kol]}")
    data = datetime.date.today().isoformat()
    wyj = os.path.join(KORZEN, "robocze", f"linki-{data}.csv")
    with open(wyj, "w", encoding="utf-8", newline="") as f:
        z = csv.writer(f)
        z.writerow(["id", "url", "kod", "adres_koncowy", "tytul_lub_blad"])
        z.writerows(wiersze)
    zle = [w for w in wiersze if not (200 <= int(w[2]) < 400)]
    print(f"sprawdzone: {len(wiersze)}, niedziałające: {len(zle)}", file=sys.stderr)
    return 1 if zle else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
