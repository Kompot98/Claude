"""Generuje RYSUNKI-DO-ZNALEZIENIA.md z dane/rysunki-plan.csv (lista dla agenta od obrazków)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wspolne import KORZEN, wczytaj_csv  # noqa: E402


def main():
    plan = wczytaj_csv("rysunki-plan.csv")
    out = ["# Rysunki do znalezienia i do narysowania", "",
           "Lista dla agenta od obrazków. W tekście każdy rysunek ma wstawkę `[RYSUNEK: F-xx, typ. Opis. Podpis: „…”]` "
           "w miejscu, gdzie ma stanąć. Po znalezieniu pliku: zapisz go w `rysunki/`, dodaj wiersz w `dane/rysunki.csv` "
           "(autor, licencja, adres pliku), zamień wstawkę na odwołanie do pliku i uruchom `python3 -I skrypty/sprawdz.py`.", "",
           "Zasady licencji: tylko CC BY, CC BY-SA, CC0 albo domena publiczna, sprawdzone przy konkretnym pliku. "
           "Odrzucać NC i ND (kurs jest płatny). OpenStax i większość LibreTexts są w 2026 na licencjach NC, więc ich rysunków nie używać. "
           "Bez zrzutów z podręczników i stron. Gdy wolnego pliku nie ma, rysunek trzeba narysować.", ""]
    for typ in ("do znalezienia", "do narysowania"):
        out += [f"## {typ.capitalize()}", ""]
        for w in plan:
            if w["typ"] != typ:
                continue
            out += [f"### {w['id']} ({w['rozdzial']})", "",
                    f"- Co pokazuje: {w['co_pokazuje']}",
                    f"- Podpis: „{w['podpis']}”"]
            if w["frazy_wyszukiwania"]:
                out.append(f"- Szukać: {w['frazy_wyszukiwania']}")
            out.append(f"- Gdzie: {w['gdzie_szukac']}")
            out.append(f"- Licencja: {w['licencja_wymagana']}")
            if w["uwagi"]:
                out.append(f"- Uwagi: {w['uwagi']}")
            out.append("")
    with open(os.path.join(KORZEN, "RYSUNKI-DO-ZNALEZIENIA.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(len(plan))


if __name__ == "__main__":
    main()
