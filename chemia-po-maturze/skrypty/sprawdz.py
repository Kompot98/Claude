"""Sprawdzenia spójności bonusu (sekcja „Weryfikacja”, punkt 2 zlecenia).

Użycie (z katalogu chemia-po-maturze/):
  python3 -I skrypty/sprawdz.py              wszystkie sprawdzenia spójności
  python3 -I skrypty/sprawdz.py --dowody     dodatkowo: plik dowodu dla każdego zasobu
  python3 -I skrypty/sprawdz.py --znaczniki  lista [ADRIAN], [RYSUNEK], [SPRAWDZIĆ]
Kod wyjścia 1, gdy jest błąd.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wspolne import KORZEN, TRESC, wczytaj_csv, pliki_tresci, odwolania  # noqa: E402

RODZAJ = {"kanał", "playlista", "strona", "kurs otwarty", "podręcznik", "skrypt uczelni", "inne"}
POZIOM = {"wprowadzenie", "pierwszy rok", "dalej"}
PRZEDMIOT = {"ogólna i nieorganiczna", "organiczna", "fizyczna", "analityczna", "biochemia",
             "matematyka", "ogólne", "spektroskopia", "chemia kwantowa", "laboratorium"}
KIERUNKI = {"wszystkie", "chemia", "medycyna", "stomatologia", "weterynaria", "farmacja",
            "analityka medyczna", "biotechnologia", "inżynieria"}
TYP_ZRODLA = {"sylabus", "podręcznik", "strona", "publikacja", "program studiów", "katalog"}
LICENCJE = {"CC BY 4.0", "CC BY 3.0", "CC BY 2.5", "CC BY 2.0", "CC BY-SA 4.0", "CC BY-SA 3.0",
            "CC BY-SA 2.5", "CC BY-SA 2.0", "CC0", "domena publiczna"}
DOMENY_RYSUNKOW = ("https://commons.wikimedia.org/", "https://openstax.org/")


def blad(lista, tekst):
    lista.append(tekst)


def sprawdz_rejestr(bledy, plik_csv, prefiks, kolumny_wymagane):
    wiersze = wczytaj_csv(plik_csv)
    ids = {}
    for w in wiersze:
        i = w.get("id", "")
        if not re.fullmatch(prefiks + r"-\d{3}", i):
            blad(bledy, f"{plik_csv}: zły identyfikator {i!r}")
        if i in ids:
            blad(bledy, f"{plik_csv}: powtórzony identyfikator {i}")
        ids[i] = w
        for k in kolumny_wymagane:
            if not (w.get(k) or "").strip():
                blad(bledy, f"{plik_csv}: {i} ma pustą kolumnę {k}")
    return ids


def main(argv):
    bledy = []

    # zasoby
    zasoby = sprawdz_rejestr(bledy, "zasoby.csv", "R",
                             ["nazwa", "url", "rodzaj", "jezyk", "przedmiot", "poziom",
                              "dla_kierunkow", "opis", "kiedy_siegnac", "data_sprawdzenia"])
    for i, w in zasoby.items():
        if w["rodzaj"] not in RODZAJ:
            blad(bledy, f"zasoby.csv: {i} rodzaj {w['rodzaj']!r} spoza listy")
        if w["poziom"] not in POZIOM:
            blad(bledy, f"zasoby.csv: {i} poziom {w['poziom']!r} spoza listy")
        if w["przedmiot"] not in PRZEDMIOT:
            blad(bledy, f"zasoby.csv: {i} przedmiot {w['przedmiot']!r} spoza listy")
        for k in [x.strip() for x in w["dla_kierunkow"].split(";")]:
            if k not in KIERUNKI:
                blad(bledy, f"zasoby.csv: {i} kierunek {k!r} spoza listy")
        u = w["url"].strip()
        if not u.startswith("http"):
            blad(bledy, f"zasoby.csv: {i} adres nie jest adresem WWW: {u!r}")
        if re.match(r"https?://(www\.)?youtube\.com/(@[^/]+|c/[^/]+|channel/[^/]+|user/[^/]+)/?$", u):
            blad(bledy, f"zasoby.csv: {i} prowadzi do strony głównej kanału, nie do playlisty: {u}")
        if re.match(r"https?://[^/]+/?$", u) and w["rodzaj"] != "podręcznik" \
                and "Spis treści artykułów jest na stronie głównej" not in w["uwagi"]:
            blad(bledy, f"zasoby.csv: {i} prowadzi do samej domeny: {u}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", w["data_sprawdzenia"]):
            blad(bledy, f"zasoby.csv: {i} data_sprawdzenia nie w formacie RRRR-MM-DD")

    # źródła
    zrodla = sprawdz_rejestr(bledy, "zrodla.csv", "Z", ["typ", "tytul", "url", "data_odczytu"])
    for i, w in zrodla.items():
        if w["typ"] not in TYP_ZRODLA:
            blad(bledy, f"zrodla.csv: {i} typ {w['typ']!r} spoza listy")
        if w["typ"] == "sylabus":
            for k in ("uczelnia", "kierunek", "rok_akademicki", "kopia_lokalna"):
                if not w[k].strip():
                    blad(bledy, f"zrodla.csv: sylabus {i} bez kolumny {k}")
        kopia = w.get("kopia_lokalna", "").strip()
        if kopia and not os.path.exists(os.path.join(KORZEN, kopia)):
            blad(bledy, f"zrodla.csv: {i} kopia lokalna {kopia} nie istnieje")

    # odwołania w treści
    r_tekst = odwolania(r"\[(R-\d{3})\]")
    z_tekst = odwolania(r"\[(Z-\d{3})\]")
    for i, miejsca in r_tekst.items():
        if i not in zasoby:
            blad(bledy, f"treść: {i} cytowany w {miejsca[0][0]}:{miejsca[0][1]}, brak w zasoby.csv")
    for i in zasoby:
        if i not in r_tekst:
            blad(bledy, f"zasoby.csv: {i} nie jest cytowany w żadnym rozdziale")
    for i, miejsca in z_tekst.items():
        if i not in zrodla:
            blad(bledy, f"treść: {i} cytowany w {miejsca[0][0]}:{miejsca[0][1]}, brak w zrodla.csv")
    for i in zrodla:
        if i not in z_tekst:
            blad(bledy, f"zrodla.csv: {i} nie jest cytowany w żadnym rozdziale")
    # sylabusy cytowane w rozdziale 2 muszą być sylabusami
    for i, miejsca in z_tekst.items():
        if any(p.startswith("02-") for p, _ in miejsca) and i in zrodla:
            if zrodla[i]["typ"] not in ("sylabus", "program studiów", "katalog", "strona", "podręcznik"):
                blad(bledy, f"rozdział 2 cytuje {i} typu {zrodla[i]['typ']}")

    # rysunki
    rysunki = sprawdz_rejestr(bledy, "rysunki.csv", "F",
                              ["plik", "zrodlo_url", "autor", "licencja", "co_pokazuje", "rozdzial", "podpis"])
    pliki_rys = set(os.listdir(os.path.join(KORZEN, "rysunki")))
    pliki_rys.discard(".gitkeep")
    w_rejestrze = set()
    for i, w in rysunki.items():
        w_rejestrze.add(w["plik"])
        if w["licencja"] not in LICENCJE:
            blad(bledy, f"rysunki.csv: {i} licencja {w['licencja']!r} niedozwolona")
        if not w["zrodlo_url"].startswith(DOMENY_RYSUNKOW):
            blad(bledy, f"rysunki.csv: {i} źródło spoza dozwolonych domen: {w['zrodlo_url']}")
        if w["plik"] not in pliki_rys:
            blad(bledy, f"rysunki.csv: {i} plik {w['plik']} nie istnieje w rysunki/")
    for p in pliki_rys - w_rejestrze:
        blad(bledy, f"rysunki/: plik {p} bez wiersza w rysunki.csv")

    # pliki dowodów
    if "--dowody" in argv:
        katalog = os.path.join(KORZEN, "robocze", "dowody")
        for i in zasoby:
            if not os.path.exists(os.path.join(katalog, f"{i}.txt")):
                blad(bledy, f"dowody: brak pliku robocze/dowody/{i}.txt")

    if "--znaczniki" in argv:
        for sciezka in pliki_tresci():
            with open(sciezka, encoding="utf-8") as f:
                for nr, linia in enumerate(f, 1):
                    for m in re.finditer(r"\[(ADRIAN|RYSUNEK|SPRAWDZIĆ): ([^\]]*)\]", linia):
                        print(f"{os.path.basename(sciezka)}:{nr}\t{m.group(1)}\t{m.group(2)}")

    for b in bledy:
        print("BŁĄD:", b)
    print(f"zasoby: {len(zasoby)}, źródła: {len(zrodla)}, rysunki: {len(rysunki)}, błędy: {len(bledy)}",
          file=sys.stderr)
    return 1 if bledy else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
