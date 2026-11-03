# Chemia po maturze: szkic bonusu

Szkic czwartego bonusu do kursu KaNaU 50/70/90, przygotowany według zlecenia z 3.11.2026 (kopie w `zlecenie/`). Stan: komplet rozdziałów w wersji roboczej, gotowy do adaptacji (sprawdzenie chemii w rozdziale 4, miejsca `[ADRIAN]`, rysunki, głos marki).

## Od czego zacząć

1. `RAPORT.md`: co powstało, odrzucone zasoby, tabela sylabusów, lista miejsc do uzupełnienia, pytania do zleceniodawcy.
2. `tresc/`: rozdziały do czytania po kolei (00 do 05).
3. `DECYZJE-AGENTA.md`: wszystkie decyzje z uzasadnieniem (D-01 do D-14), w tym zmiana licencji OpenStax (D-05).

## Co tu jest

| Ścieżka | Zawartość |
|---|---|
| `tresc/` | rozdziały w Markdown: wstęp, „Inna gra”, mapa z matury na studia, zasoby, cztery wprowadzenia, źródła |
| `dane/zasoby.csv` | 61 polecanych zasobów (R-001 do R-061) z opisem, poziomem, kierunkami i datą sprawdzenia |
| `dane/zrodla.csv` | 32 źródła cytowane (Z-001 do Z-032): sylabusy, plany studiów, podręczniki |
| `dane/rysunki.csv` | rejestr rysunków; pusty, brakujące rysunki są opisane w tekście jako `[RYSUNEK: …]` |
| `rysunki/` | pusty (D-13) |
| `zrodla/` | tekstowe kopie sylabusów i planów studiów z nagłówkiem (adres, uczelnia, rok, data odczytu) |
| `zrodla/lektury/` | tekst przeczytanych fragmentów podręczników otwartych, na których opiera się rozdział 4 |
| `robocze/dowody/` | dowód sprawdzenia każdego zasobu (lista filmów, fragment strony, rekord katalogu) |
| `robocze/` | listy kandydatów z odrzuconymi, drugi przegląd, tabela sylabusów, lista kontrolna słów Adriana, wyniki sprawdzania adresów, pliki JSON, z których zbudowano `zasoby.csv` |
| `skrypty/` | sprawdzenia z sekcji „Weryfikacja” zlecenia i generator rozdziału 5 |
| `ROZBIEZNOSCI.md` | różnice wykryte w drugim przeglądzie zasobów |
| `POSTEP.md` | dziennik etapów |

## Skrypty

Python 3, tylko biblioteka standardowa. Uruchamiać z tego katalogu:

```
python3 -I skrypty/sprawdz.py --dowody --znaczniki   # spójność odwołań, rejestrów, licencji, lista znaczników
python3 -I skrypty/styl.py                            # zasady głosu, pojęcia akademickie
python3 -I skrypty/linki.py --ca robocze/ca-z-certyfikatami-posrednimi.pem   # czy adresy odpowiadają
python3 -I skrypty/dlugosc.py                         # długość w stronach znormalizowanych
python3 -I skrypty/zrodla_md.py                       # wygeneruj tresc/05-zrodla.md z rejestrów
```

Po każdej zmianie `dane/*.csv` trzeba wygenerować rozdział 5 od nowa. Nowe zasoby dopisuje się przez `robocze/dodaj_zasoby.py plik.json` albo bezpośrednio w CSV.

## Konwencje w tekście

`[R-xxx]` to zasób z `zasoby.csv`, `[Z-xxx]` to źródło z `zrodla.csv`; oba zostają jako zwykły tekst do obsługi przy konwersji. Komentarze HTML w rozdziale 4 (`<!-- Z-026: Harvey 6.9, … -->`) wskazują miejsce w źródle dla zdań merytorycznych. Znaczniki do uzupełnienia: `[ADRIAN: …]`, `[RYSUNEK: …]`, `[SPRAWDZIĆ: …]`.
