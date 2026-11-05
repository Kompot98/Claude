"""Krok 3: numeruje rysunki w kolejności czytania i tworzy listę dla agenta od obrazków.
Użycie: python3 -I krok3_rysunki.py WEJSCIE WYJSCIE PLAN_CSV LISTA_MD PLAN_NOWY_CSV
"""
import csv, re, sys

wej, wyj, plan_csv, lista_md, plan_nowy = sys.argv[1:6]
t = open(wej, encoding="utf-8").read()
stary_plan = {w["id"]: w for w in csv.DictReader(open(plan_csv, encoding="utf-8"))}

WZOR = re.compile(r"\[RYSUNEK: (F-[A-Z0-9]+), (do znalezienia|do narysowania)\. (.*?)\]$", re.M)

# kontekst: ostatni nagłówek rozdziału i części
naglowki = [(m.start(), m.group(0).strip()) for m in re.finditer(r"(?m)^#{1,2} .+$", t)]


def gdzie(poz):
    rozdz, czesc = "", ""
    for p, h in naglowki:
        if p > poz:
            break
        if h.startswith("# "):
            rozdz, czesc = h[2:], ""
        else:
            czesc = h[3:]
    return rozdz + (" / " + czesc if czesc else "")


# rysunki kluczowe: bez nich tekst w tym miejscu jest trudny do zrozumienia
KLUCZOWE = {"F-06", "F-29", "F-14", "F-18", "F-19", "F-25", "F-20", "F-NEW1"}

wpisy, mapa = [], {}
for i, m in enumerate(WZOR.finditer(t), start=1):
    stary, typ, reszta = m.group(1), m.group(2), m.group(3)
    nowy = f"F-{i:02d}"
    mapa[stary] = nowy
    opis, _, podpis = reszta.rpartition(" Podpis: ")
    podpis = podpis.strip()
    if podpis.startswith("„") and podpis.endswith("”"):
        podpis = podpis[1:-1]
    miejsce = gdzie(m.start())
    if stary in KLUCZOWE:
        prio = "A"
    elif miejsce.startswith("4."):
        prio = "B"
    else:
        prio = "C"
    sp = stary_plan.get(stary, {})
    wpisy.append({
        "id": nowy, "dawny_id": stary, "miejsce": miejsce, "typ": typ, "priorytet": prio,
        "co_pokazuje": opis.strip(), "podpis": podpis,
        "frazy_wyszukiwania": sp.get("frazy_wyszukiwania", ""),
        "gdzie_szukac": sp.get("gdzie_szukac", "") or ("rysunek własny w stylu kursu" if typ == "do narysowania" else ""),
        "licencja_wymagana": sp.get("licencja_wymagana", "") or ("własny" if typ == "do narysowania" else "CC BY, CC BY-SA, CC0 albo domena publiczna"),
    })

if len(set(mapa)) != len(mapa):
    raise SystemExit("powtórzony identyfikator rysunku")


def podmien(m):
    return f"[RYSUNEK: {mapa[m.group(1)]}, {m.group(2)}. {m.group(3)}]"


t2 = WZOR.sub(podmien, t)
open(wyj, "w", encoding="utf-8").write(t2)

pola = ["id", "dawny_id", "miejsce", "typ", "priorytet", "co_pokazuje", "podpis", "frazy_wyszukiwania", "gdzie_szukac", "licencja_wymagana"]
with open(plan_nowy, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=pola)
    w.writeheader()
    w.writerows(wpisy)

L = ["# Rysunki do wersji połączonej: lista dla agenta od obrazków", "",
     f"Plik `przystepna/chemia-po-maturze-polaczona.md` ma {len(wpisy)} wstawek `[RYSUNEK: F-xx, …]`, ponumerowanych w kolejności czytania. Ta sama lista jest w `dane/rysunki-plan-polaczona.csv`. Numery różnią się od numerów w `tresc/` i w `RYSUNKI-DO-ZNALEZIENIA.md` (wersja pierwotna); kolumna „dawny numer” pozwala je powiązać.", "",
     "Kolejność pracy: najpierw priorytet A, czyli rysunki, bez których tekst w danym miejscu jest trudny do zrozumienia (mechanizmy, diagram orbitali, widma, wykresy energii Gibbsa i krzywej wzorcowej, schemat buforu). Potem B (reszta rozdziału 4), na końcu C (rozdziały 1–3).", "",
     "Zasady: zdjęcia i rysunki z zewnątrz tylko na licencji CC BY, CC BY-SA, CC0 albo z domeny publicznej (bez NC), z atrybucją w podpisie i wpisem w `dane/rysunki.csv`. Rysunki „do narysowania” powstają w stylu kursu; opis podaje, co ma być widać, a podpis jest gotowy do wstawienia.", ""]
for prio, tyt in [("A", "Priorytet A"), ("B", "Priorytet B"), ("C", "Priorytet C")]:
    L += [f"## {tyt}", ""]
    for e in [x for x in wpisy if x["priorytet"] == prio]:
        L.append(f"### {e['id']} ({e['typ']}; dawny numer {e['dawny_id']})")
        L.append("")
        L.append(f"Gdzie: {e['miejsce']}.")
        L.append("")
        L.append(f"Co pokazuje: {e['co_pokazuje']}")
        L.append("")
        L.append(f"Podpis: „{e['podpis']}”")
        if e["frazy_wyszukiwania"]:
            L += ["", f"Frazy do wyszukania: {e['frazy_wyszukiwania']}"]
        if e["typ"] == "do znalezienia":
            L += ["", f"Gdzie szukać: {e['gdzie_szukac'] or 'Wikimedia Commons'}. Licencja: {e['licencja_wymagana']}."]
        L.append("")
open(lista_md, "w", encoding="utf-8").write("\n".join(L).rstrip("\n") + "\n")
print("rysunków:", len(wpisy), "| A:", sum(e["priorytet"] == "A" for e in wpisy),
      "B:", sum(e["priorytet"] == "B" for e in wpisy), "C:", sum(e["priorytet"] == "C" for e in wpisy))
print("mapa:", mapa)
