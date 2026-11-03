"""Dopisuje lub nadpisuje wiersze w dane/zasoby.csv. Użycie: python3 -I robocze/dodaj_zasoby.py plik.json"""
import csv, json, sys, os
K = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(K, "dane", "zasoby.csv")
KOL = "id,nazwa,url,rodzaj,jezyk,przedmiot,poziom,dla_kierunkow,opis,kiedy_siegnac,data_sprawdzenia,uwagi".split(",")
with open(P, encoding="utf-8", newline="") as f:
    wiersze = {w["id"]: w for w in csv.DictReader(f)}
for w in json.load(open(sys.argv[1], encoding="utf-8")):
    w.setdefault("data_sprawdzenia", "2026-11-03")
    w.setdefault("uwagi", "")
    wiersze[w["id"]] = {k: w.get(k, "") for k in KOL}
with open(P, "w", encoding="utf-8", newline="") as f:
    z = csv.DictWriter(f, fieldnames=KOL)
    z.writeheader()
    for i in sorted(wiersze):
        z.writerow(wiersze[i])
print(len(wiersze))
