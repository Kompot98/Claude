# Decyzje agenta

Format wpisu: co, dlaczego, co odrzucone. Wpisów nie kasuję; zmianę zapisuję nowym wpisem.

## D-01, 2026-11-03: układ rejestrów i słowniki wartości

**Co:** `zasoby.csv` ma kolumny ze zlecenia. Wartości słownikowe: `rodzaj` z listy zlecenia; `poziom` ∈ {wprowadzenie, pierwszy rok, dalej}; `przedmiot` ∈ {ogólna i nieorganiczna, organiczna, fizyczna, analityczna, biochemia, matematyka, ogólne, spektroskopia, chemia kwantowa, laboratorium}; `dla_kierunkow` jako lista po średniku z {wszystkie, chemia, medycyna, stomatologia, weterynaria, farmacja, analityka medyczna, biotechnologia, inżynieria}. `zrodla.csv`: `id,typ,tytul,url,uczelnia,kierunek,przedmiot,rok_akademicki,data_odczytu,kopia_lokalna,uwagi`, typ ∈ {sylabus, program studiów, katalog, podręcznik, strona, publikacja}. Identyfikatory rysunków `F-001`.
**Dlaczego:** stałe słowniki pozwalają skryptowi wyłapać literówki i dają odbiorcy filtrowanie bez czyszczenia danych. Trzy dodatkowe wartości przedmiotu (spektroskopia, chemia kwantowa, laboratorium) są dla zasobów z rozdziału 4.
**Odrzucone:** wolny tekst w tych kolumnach.

## D-02, 2026-11-03: folder `robocze/` z dowodami

**Co:** każdy zasób ma plik `robocze/dowody/R-xxx.txt` z adresem, datą, metodą i surowymi danymi, z których powstał opis (lista filmów w playliście, fragmenty podstron, wpis katalogu). Tam też listy kandydatów z werdyktem, notatki z lektur do rozdziału 4 i zapis drugiego przeglądu. Folder zostaje w archiwum, w tekście bonusu nie jest cytowany.
**Dlaczego:** zlecenie wymaga, żeby opis nie powstał z pamięci; plik dowodu pozwala to sprawdzić bez powtarzania pracy.
**Odrzucone:** trzymanie dowodów tylko w kolumnie `uwagi` (za mało miejsca na listę filmów).

## D-03, 2026-11-03: dodatkowy folder `zlecenie/`

**Co:** kopie `ZLECENIE-agent-w-chmurze.md` i `KONTEKST-KaNaU.md` w archiwum.
**Dlaczego:** archiwum ma być samowystarczalne; odbiorca widzi, według jakiej wersji zlecenia powstał szkic.
**Odrzucone:** nic.

## D-04, 2026-11-03: wideo opisuję z tytułów filmów, bez transkrypcji

**Co:** dla playlist YouTube dowodem jest pełna lista tytułów filmów z długościami, pobrana bez logowania, oraz opis playlisty, gdy jest. Transkrypcji i opisów pojedynczych filmów to środowisko nie pobiera (YouTube żąda logowania), więc w `uwagi` każdego zasobu wideo piszę, z czego powstał opis.
**Dlaczego:** zlecenie zabrania logowania i opisów z pamięci; tytuły całej playlisty wystarczają, żeby opisać zakres i kolejność tematów, ale nie styl tłumaczenia.
**Odrzucone:** logowanie do YouTube (zabronione zleceniem); opisywanie stylu filmów z pamięci.
