# Chemia po maturze: bonus do kursu KaNaU 50/70/90

Czwarty bonus do kursu KaNaU 50/70/90, przygotowany według zlecenia z 3.11.2026 (kopie w `zlecenie/`). Stan: wersja ostateczna tekstu. Do zrobienia zostały rysunki (lista dla agenta od obrazków) i, opcjonalnie, siedem osobistych przykładów Adriana.

## Od czego zacząć

1. `wydanie/chemia-po-maturze.pdf` albo `.html`: cały kurs w jednym pliku, do przeczytania od początku do końca.
2. `RAPORT.md`: co powstało, co zmieniło się po pierwszym raporcie, co sprawdzić ręcznie przy wgrywaniu, odrzucone zasoby, tabela sylabusów.
3. `RYSUNKI-DO-ZNALEZIENIA.md`: 23 rysunki do znalezienia albo narysowania, z frazami wyszukiwania i wymaganą licencją.
4. `DO-UZUPELNIENIA-ADRIAN.md`: siedem miejsc, w których można dopisać przykład z własnych korepetycji (tekst jest kompletny bez nich).
5. `DECYZJE-AGENTA.md`: wszystkie decyzje z uzasadnieniem (D-01 do D-18).

## Co tu jest

| Ścieżka | Zawartość |
|---|---|
| `wydanie/` | kurs w jednym pliku: Markdown bez komentarzy, podgląd HTML ze spisem treści, PDF; `styl-podgladu.css` to tylko styl podglądu |
| `tresc/` | rozdziały źródłowe w Markdown (00 do 05), z komentarzami źródłowymi w rozdziale 4; tu się poprawia tekst |
| `dane/zasoby.csv` | 63 polecane zasoby (R-001 do R-063) z opisem, poziomem, kierunkami i datą sprawdzenia |
| `dane/zrodla.csv` | 34 źródła cytowane (Z-001 do Z-034): sylabusy, plany studiów, podręczniki |
| `dane/rysunki-plan.csv` | plan 23 rysunków (F-01 do F-23): co pokazuje, podpis, frazy wyszukiwania, gdzie szukać, wymagana licencja |
| `dane/rysunki.csv` | rejestr rysunków już dodanych; na razie pusty |
| `rysunki/` | miejsce na pliki rysunków; na razie puste |
| `zrodla/` | tekstowe kopie sylabusów i planów studiów z nagłówkiem (adres, uczelnia, rok, data odczytu) |
| `zrodla/lektury/` | tekst przeczytanych fragmentów podręczników otwartych, na których opiera się rozdział 4 |
| `robocze/dowody/` | dowód sprawdzenia każdego zasobu (lista filmów, fragment strony, rekord katalogu) |
| `robocze/` | listy kandydatów z odrzuconymi, drugi przegląd, tabela sylabusów, lista kontrolna słów Adriana, wyniki sprawdzania adresów, pliki JSON, z których zbudowano `zasoby.csv` |
| `skrypty/` | sprawdzenia z sekcji „Weryfikacja” zlecenia, generatory rozdziału 5 i listy rysunków, budowa wydania |
| `ROZBIEZNOSCI.md` | różnice wykryte w drugim przeglądzie zasobów |
| `POSTEP.md` | dziennik etapów i checkpointów |

## Skrypty

Python 3, tylko biblioteka standardowa (wydanie potrzebuje jeszcze `pandoc`, PDF `node` z Playwright). Uruchamiać z tego katalogu:

```
python3 -I skrypty/sprawdz.py --dowody --znaczniki   # spójność odwołań, rejestrów, licencji, planu rysunków
python3 -I skrypty/styl.py                            # zasady głosu, pojęcia akademickie
python3 -I skrypty/linki.py --ca robocze/ca-z-certyfikatami-posrednimi.pem   # czy adresy odpowiadają
python3 -I skrypty/dlugosc.py                         # długość w stronach znormalizowanych
python3 -I skrypty/zrodla_md.py                       # wygeneruj tresc/05-zrodla.md z rejestrów
python3 -I skrypty/rysunki_md.py                      # wygeneruj RYSUNKI-DO-ZNALEZIENIA.md z planu rysunków
python3 -I skrypty/wydanie.py                         # zbuduj wydanie/chemia-po-maturze.md i .html
node skrypty/pdf.js                                   # zbuduj wydanie/chemia-po-maturze.pdf z .html
```

Po każdej zmianie `dane/*.csv` trzeba wygenerować rozdział 5 od nowa, a po każdej zmianie w `tresc/` wydanie. Nowe zasoby dopisuje się przez `robocze/dodaj_zasoby.py plik.json` albo bezpośrednio w CSV.

## Konwencje w tekście

`[R-xxx]` to zasób z `zasoby.csv`, `[Z-xxx]` to źródło z `zrodla.csv`; oba zostają jako zwykły tekst do obsługi przy konwersji na platformę. Komentarze HTML w rozdziale 4 (`<!-- Z-026: Harvey 6.9, … -->`) wskazują miejsce w źródle dla zdań merytorycznych; w wydaniu są usunięte. Wstawki `[RYSUNEK: F-xx, …]` oznaczają miejsce na rysunek z `dane/rysunki-plan.csv`. Gdy rysunek się znajdzie: plik do `rysunki/`, wiersz do `dane/rysunki.csv` (licencja tylko CC BY, CC BY-SA, CC0 albo domena publiczna), wstawkę zamienić na obrazek z podpisem i atrybucją, a potem `sprawdz.py` i wydanie od nowa.
