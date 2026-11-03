"""Wspólne funkcje skryptów sprawdzających. Tylko biblioteka standardowa."""
import csv
import os
import re

KORZEN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRESC = os.path.join(KORZEN, "tresc")
DANE = os.path.join(KORZEN, "dane")


def wczytaj_csv(nazwa):
    with open(os.path.join(DANE, nazwa), encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def pliki_tresci():
    return sorted(
        os.path.join(TRESC, n) for n in os.listdir(TRESC) if n.endswith(".md")
    )


def bez_komentarzy(tekst):
    return re.sub(r"<!--.*?-->", "", tekst, flags=re.S)


def odwolania(wzor, pomin=("05-zrodla.md",)):
    """Zwraca {id: [(plik, nr_linii), ...]} dla odwołań w treści (bez komentarzy HTML)."""
    wynik = {}
    for sciezka in pliki_tresci():
        if os.path.basename(sciezka) in pomin:
            continue
        with open(sciezka, encoding="utf-8") as f:
            tekst = bez_komentarzy(f.read())
        for nr, linia in enumerate(tekst.splitlines(), 1):
            for m in re.finditer(wzor, linia):
                wynik.setdefault(m.group(1), []).append((os.path.basename(sciezka), nr))
    return wynik
