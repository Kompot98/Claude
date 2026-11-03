"""Sprawdzenie zasad głosu marki i wyjaśnień pojęć (do ręcznego przejrzenia).

Użycie: python3 -I skrypty/styl.py [--liczby] [plik.md ...]
Wypisuje podejrzane miejsca. Kod wyjścia 1, gdy są twarde naruszenia
(myślnik jako przerywnik, słowa z czarnej listy, proste cudzysłowy, HTML poza komentarzami).
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wspolne import pliki_tresci, bez_komentarzy  # noqa: E402

CZARNA_LISTA = [
    r"najlepsz", r"genialn", r"must[- ]see", r"niezwykle", r"kompleksow", r"innowacyjn",
    r"dedykowan", r"\bmusisz\b", r"\bmusicie\b", r"powinien[eś]*\b", r"powinnaś", r"gwarant",
    r"na pewno", r"\bzdasz\b", r"rewelacyjn", r"świetn", r"fantastyczn", r"doskonał",
    r"absolutnie", r"subskryb", r"wyświetle",
]
# pojęcia akademickie: pierwsze wystąpienie (w kolejności rozdziałów) ma mieć wyjaśnienie w akapicie
POJECIA = {
    "kolokwium": r"sprawdzian", "wejściówk": r"sprawdzian|kolokwium", "sylabus": r"opis|karta",
    "ECTS": r"punkt", "konwersatori": r"dyskusj", "sesj": r"egzamin", "ćwiczeni": r"grup|zadani",
    "seminari": r"prezentacj|referat", "sprawozdani": r"opracowani|opis", "USOS": r"system",
    "warun": r"powtórz|mimo", "starost": r"student|łącznik", "skrypt": r"podręcznik",
    "koło naukowe": r"stowarzysz|grup", "zaliczeni": r"kolokwi|ocen|egzamin", "wykład": r"prowadzący|sala|mówi",
    "dziennik laboratoryjny": r"zeszyt|notatk", "IBUK": r"e-book|książ|bibliotek",
}
SLOWA_JEZYKA = re.compile(r"\b(\d+[,.]?\d*\s?%|\d{2,})")


def akapity(tekst):
    return [a for a in re.split(r"\n\s*\n", tekst) if a.strip()]


def main(argv):
    pokaz_liczby = "--liczby" in argv
    pliki = [a for a in argv if a.endswith(".md")] or pliki_tresci()
    twarde = 0
    znane = set()
    for sciezka in pliki:
        nazwa = os.path.basename(sciezka)
        with open(sciezka, encoding="utf-8") as f:
            surowy = f.read()
        tekst = bez_komentarzy(surowy)
        for nr, linia in enumerate(tekst.splitlines(), 1):
            if linia.startswith("|") or linia.startswith("#"):
                kontrola_myslnikow = False
            else:
                kontrola_myslnikow = True
            if "—" in linia or "–" in re.sub(r"\d–\d", "", linia):
                print(f"{nazwa}:{nr}\tMYŚLNIK\t{linia.strip()[:120]}"); twarde += 1
            if kontrola_myslnikow and re.search(r"\S - \S", linia):
                print(f"{nazwa}:{nr}\tMYŚLNIK\t{linia.strip()[:120]}"); twarde += 1
            for w in CZARNA_LISTA:
                if re.search(w, linia, re.I):
                    print(f"{nazwa}:{nr}\tSŁOWO({w})\t{linia.strip()[:120]}"); twarde += 1
            if re.search(r'"[^"]+"', linia):
                print(f"{nazwa}:{nr}\tCUDZYSŁÓW\t{linia.strip()[:120]}"); twarde += 1
            if re.search(r"<[a-zA-Z/][^>]*>", linia):
                print(f"{nazwa}:{nr}\tHTML\t{linia.strip()[:120]}"); twarde += 1
            if re.search(r"\bto nie\b[^.]{0,60}\bto\b", linia, re.I):
                print(f"{nazwa}:{nr}\tTO-NIE-A-TO-B?\t{linia.strip()[:120]}")
            if re.match(r"\s*[-*] \*\*[^*]+:\*\*", linia) or re.match(r"\s*[-*] \*\*[^*]+\*\*:", linia):
                print(f"{nazwa}:{nr}\tETYKIETA\t{linia.strip()[:120]}")
            if pokaz_liczby and SLOWA_JEZYKA.search(re.sub(r"\[(R|Z|F)-\d{3}\]", "", linia)):
                print(f"{nazwa}:{nr}\tLICZBA\t{linia.strip()[:120]}")
        for akapit in akapity(tekst):
            for pojecie, wyjasnienie in POJECIA.items():
                if pojecie in znane:
                    continue
                if re.search(pojecie, akapit, re.I):
                    znane.add(pojecie)
                    if not re.search(wyjasnienie, akapit, re.I):
                        print(f"{nazwa}\tPOJĘCIE({pojecie}) bez wyjaśnienia w akapicie:\t{akapit.strip()[:100]}")
    print(f"twarde naruszenia: {twarde}", file=sys.stderr)
    return 1 if twarde else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
