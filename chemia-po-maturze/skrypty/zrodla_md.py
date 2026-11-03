"""Generuje tresc/05-zrodla.md z dane/zasoby.csv i dane/zrodla.csv.
Każda pozycja trafia pod rozdział, w którym jest cytowana po raz pierwszy (w kolejności rozdziałów);
pozostałe rozdziały są wymienione w nawiasie. Użycie: python3 -I skrypty/zrodla_md.py"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wspolne import TRESC, wczytaj_csv, odwolania  # noqa: E402

NAZWY = {
    "00-wstep.md": "Wstęp", "01-inna-gra.md": "1. Inna gra",
    "02-co-z-matury-zamienia-sie-w-co.md": "2. Co z matury zamienia się w co",
    "03-skad-sie-uczyc.md": "3. Skąd się uczyć", "04a-aktywnosc.md": "4a. Aktywność",
    "04b-chemia-kwantowa.md": "4b. Chemia kwantowa", "04c-spektroskopia.md": "4c. Spektroskopia",
    "04d-laboratorium.md": "4d. Laboratorium",
}
KOLEJNOSC = list(NAZWY)


def pierwsze_zdanie(t):
    t = t.strip()
    m = re.match(r"(.+?[.!?])(\s|$)", t)
    return (m.group(1) if m else t)


def grupuj(odw):
    grupy = {k: [] for k in KOLEJNOSC}
    for i, miejsca in odw.items():
        pliki = sorted({p for p, _ in miejsca}, key=KOLEJNOSC.index)
        grupy[pliki[0]].append((i, pliki[1:]))
    return grupy


def main():
    zasoby = {w["id"]: w for w in wczytaj_csv("zasoby.csv")}
    zrodla = {w["id"]: w for w in wczytaj_csv("zrodla.csv")}
    out = ["## Źródła", "",
           "Dwie listy. Pierwsza to zasoby polecane do nauki, opisane w rozdziale 3 i w rozdziale 4. "
           "Druga to dokumenty, na których oparty jest tekst: sylabusy, plany studiów, podręczniki i strony. "
           "Każda pozycja stoi przy rozdziale, w którym pojawia się po raz pierwszy; w nawiasie są inne rozdziały, które ją cytują. "
           "Wszystkie adresy sprawdzono w listopadzie 2026.", "",
           "## Zasoby polecane", ""]
    for plik, poz in grupuj(odwolania(r"\[(R-\d{3})\]")).items():
        if not poz:
            continue
        out += [f"### {NAZWY[plik]}", ""]
        for i, inne in sorted(poz):
            w = zasoby[i]
            dodatek = f" (także: {', '.join(NAZWY[p].split('. ')[0] for p in inne)})" if inne else ""
            out.append(f"- [{i}] {w['nazwa']}. {w['url']} Język: {w['jezyk']}; poziom: {w['poziom']}. "
                       f"Co z tego wzięliśmy: {pierwsze_zdanie(w['opis'])}{dodatek}")
        out.append("")
    out += ["## Źródła cytowane", ""]
    for plik, poz in grupuj(odwolania(r"\[(Z-\d{3})\]")).items():
        if not poz:
            continue
        out += [f"### {NAZWY[plik]}", ""]
        for i, inne in sorted(poz):
            w = zrodla[i]
            kto = ", ".join(x for x in (w["uczelnia"], w["kierunek"], w["rok_akademicki"]) if x)
            kto = f" ({kto})" if kto else ""
            dodatek = f" (także: {', '.join(NAZWY[p].split('. ')[0] for p in inne)})" if inne else ""
            out.append(f"- [{i}] {w['tytul']}{kto}. {w['url']} Odczyt: {w['data_odczytu']}. "
                       f"Co z tego wzięliśmy: {pierwsze_zdanie(w['uwagi'])}{dodatek}")
        out.append("")
    with open(os.path.join(TRESC, "05-zrodla.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("zapisano 05-zrodla.md")


if __name__ == "__main__":
    main()
