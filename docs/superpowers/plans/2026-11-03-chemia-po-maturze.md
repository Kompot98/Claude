# Plan pracy: bonus „Chemia po maturze”

> **Dla wykonawcy (agenta):** plan wykonywany zadanie po zadaniu, w tej sesji, według superpowers:executing-plans. Kroki mają pola wyboru (`- [ ]`) do śledzenia postępu. Po każdym zadaniu commit i wpis w `POSTEP.md`.

**Cel:** pełny szkic bonusu „Chemia po maturze” w folderze `chemia-po-maturze/` repozytorium, zgodny ze zleceniem, z rejestrami CSV, kopiami sylabusów, skryptami sprawdzającymi i raportem, na koniec spakowany do zip.

**Podejście:** najpierw szkielet folderu i skrypty sprawdzające (żeby każdy etap dało się zmierzyć), potem pilotaż na chemii organicznej i spektroskopii, który ustala format opisu zasobu i format komentarzy do źródła, dopiero potem szeroko. Każdy zasób przechodzi tę samą ścieżkę: kandydat → pobranie dowodu (tytuły playlisty, tekst strony, wpis katalogu) → opis → wiersz w CSV → drugi ślepy przegląd na końcu etapu.

**Narzędzia:** `curl` przez proxy sesji (z cookie jar dla USOS), `yt-dlp --flat-playlist` (tytuły i długości filmów; opisy filmów i transkrypcje są w tym środowisku niedostępne, YouTube wymaga logowania), `pandoc`/`pdftotext` do tekstu ze stron i PDF, agent `web-fetch` i `WebSearch` do szukania kandydatów, Python 3.13 bez zależności do skryptów, API Wikimedia Commons do licencji plików.

**Spec:** zlecenie `ZLECENIE-agent-w-chmurze.md` i `KONTEKST-KaNaU.md` (wklejone przez zleceniodawcę; kopie trafią do `chemia-po-maturze/zlecenie/` dla kompletności archiwum).

## Ograniczenia globalne (ze zlecenia, obowiązują w każdym zadaniu)

- Wszystko po polsku; źródła mogą być angielskie, z zaznaczeniem języka i poziomu.
- Słowa Adriana (punkty 1–12) w pierwszej osobie, bez łagodzenia, odwracania, zastępowania. Brak osobistego przykładu → `[ADRIAN: …]`.
- Rady nie od Adriana: bezosobowo albo z odwołaniem do źródła. Żadnych wymyślonych anegdot, liczb, nazwisk, egzaminów.
- Każdy zasób otwarty i opisany własnymi słowami, z `data_sprawdzenia`; link do playlisty/kursu, nie do strony głównej; adresów nie konstruuję z domysłu.
- Opis zasobu: co w środku, kiedy sięgnąć, poziom, język. Bez „najlepszy”, „genialny”, bez liczby subskrybentów.
- Najpierw polskie otwarte materiały uczelni, potem angielskie.
- Podręczniki: drogie i trudno dostępne (słowa Adriana zostają), drogi legalne: biblioteki, IBUK Libra i dostępy uczelni, OpenStax/LibreTexts, używane i starsze wydania, wydania angielskie. Bez nazw serwisów z kopiami.
- Sylabusy: 8 kierunków × do 3 uczelni, rok 2026/27 lub najnowszy z zapisanym rokiem, każdy w `zrodla.csv` z kopią w `zrodla/`; max 3 podejścia na brakujący; „na przykład na X”, bez uogólnień.
- Rozdział 4: źródła otwarte przeczytane w całości (OpenStax, LibreTexts), komentarz `<!-- źródło, rozdział -->` przy każdym zdaniu merytorycznym; niepodparte → `[SPRAWDZIĆ: …]`; Piela i inne płatne jako lektura dalsza z opisem ze spisu treści.
- Rysunki: tylko CC BY, CC BY-SA, domena publiczna, zgoda wydawcy; licencja plik po pliku; NC odrzucone; inaczej `[RYSUNEK: …]`.
- Głos: per „Ty” wielką literą, krótkie zdania, pojęcie wyjaśnione przy pierwszym użyciu, bez superlatywów, bez straszenia, bez obietnic wyniku, bez „to nie A, to B”, bez myślników jako przerywników, bez list z pogrubioną etykietą i dwukropkiem, cudzysłowy „polskie”, wzory w Unicode, przecinek dziesiętny.
- Nie-cele: matematyka (jedno hasło), AI, artykuły naukowe, wybór kierunku, poradnik studencki, ocenianie uczelni i wykładowców, nazywanie konkurencji.
- Markdown bez HTML (poza komentarzami źródłowymi), nagłówki `##`/`###`, odnośniki jako tekst `[R-012]`, `[Z-004]`.
- Długość orientacyjna 25–45 stron po 1800 znaków, rozdział 3 największy; odstępstwa zanotowane.
- Commit po każdym zadaniu na gałąź `claude/sleepy-fermi-u784a4`, push po każdym etapie.

## Na co zwracać uwagę przy przeglądzie (ryzyka, które nie wynikają z jednego zadania)

1. Czytelnik trafia na słowo akademickie bez wyjaśnienia (kolokwium, sylabus, ECTS, konwersatorium, sesja, warunek). Pilnuje: skrypt `styl.py` (lista słów ze słownika kontekstu, sprawdza, czy pierwsze wystąpienie w całym tekście czytanym po kolei ma w tym samym akapicie wyjaśnienie) plus ręczny przegląd w zadaniu 12.
2. Link prowadzi do strony głównej kanału zamiast playlisty. Pilnuje: `sprawdz.py` odrzuca adresy `youtube.com/@…` i `youtube.com/c/…` bez `/playlists`, i adresy będące samą domeną.
3. Rysunek z licencją NC lub bez licencji trafia do kursu płatnego. Pilnuje: `sprawdz.py` dopuszcza w `rysunki.csv` tylko wartości z listy (CC BY 4.0, CC BY 3.0, CC BY-SA 4.0, CC BY-SA 3.0, CC0, domena publiczna) i wymaga `zrodlo_url` z `commons.wikimedia.org` albo `openstax.org`.
4. Liczba w tekście bez źródła, albo słowa Adriana złagodzone. Pilnuje: `styl.py` wypisuje każde zdanie z liczbą (poza numerami rozdziałów, ID i latami w cytowaniach) do ręcznej kontroli; punkty 1–12 Adriana mają w zadaniu 9 listę kontrolną „gdzie każdy punkt jest w tekście i w jakim brzmieniu”.
5. Opis zasobu z pamięci zamiast z pobranego dowodu. Pilnuje: każdy zasób ma plik dowodu w `robocze/dowody/R-xxx.txt` (tytuły playlisty, fragment strony, wpis katalogu, z datą i adresem); `sprawdz.py --dowody` sprawdza, że każdy wiersz `zasoby.csv` ma taki plik. Folder `robocze/` zostaje w archiwum jako materiał dla odbiorcy, ale nie jest cytowany w tekście.

---

## Układ plików

```
chemia-po-maturze/
  README.md, RAPORT.md, ROZBIEZNOSCI.md, DECYZJE-AGENTA.md, POSTEP.md
  zlecenie/            kopie obu plików zlecenia (dla kompletności)
  tresc/00-wstep.md … 05-zrodla.md   (9 plików jak w zleceniu)
  dane/zasoby.csv, zrodla.csv, rysunki.csv
  rysunki/             pliki SVG/PNG na wolnych licencjach
  zrodla/              kopie sylabusów: tekst z nagłówkiem (adres, uczelnia, kierunek, rok, data)
  robocze/dowody/      dowody sprawdzenia zasobów (R-xxx.txt), przegląd ślepy (przeglad2-*.md)
  skrypty/sprawdz.py, styl.py, linki.py, dlugosc.py
```

Kolumny `zasoby.csv`: `id,nazwa,url,rodzaj,jezyk,przedmiot,poziom,dla_kierunkow,opis,kiedy_siegnac,data_sprawdzenia,uwagi`.
Kolumny `zrodla.csv`: `id,typ,tytul,url,uczelnia,kierunek,przedmiot,rok_akademicki,data_odczytu,kopia_lokalna,uwagi` (typ: sylabus, podręcznik, strona, publikacja).
Kolumny `rysunki.csv`: `id,plik,zrodlo_url,autor,licencja,co_pokazuje,rozdzial,podpis`.

Wartości słownikowe: `rodzaj` ∈ {kanał, playlista, strona, kurs otwarty, podręcznik, skrypt uczelni, inne}; `poziom` ∈ {wprowadzenie, pierwszy rok, dalej}; `przedmiot` ∈ {ogólna i nieorganiczna, organiczna, fizyczna, analityczna, biochemia, matematyka, ogólne}; `dla_kierunkow` jako lista po średniku z {wszystkie, chemia, medycyna, stomatologia, weterynaria, farmacja, analityka medyczna, biotechnologia, inżynieria}.

---

### Zadanie 0: Szkielet, skrypty sprawdzające, dziennik

**Pliki:** cały szkielet wyżej (puste rozdziały z nagłówkiem `## tytuł` i jedną linią „szkic w przygotowaniu”), nagłówki CSV, `skrypty/*.py`, `POSTEP.md`, `DECYZJE-AGENTA.md` (pierwszy wpis: układ CSV, słowniki wartości, folder `robocze/`), kopie zlecenia.

**Skrypty (Python 3, tylko biblioteka standardowa, uruchamiane `python3 -I skrypty/x.py` z katalogu `chemia-po-maturze/`, kod wyjścia 1 przy błędzie):**
- `sprawdz.py`: (a) każdy `[R-xxx]` w `tresc/` jest w `zasoby.csv` i odwrotnie; (b) każdy `[Z-xxx]` w `tresc/` jest w `zrodla.csv` i odwrotnie; (c) każdy plik w `rysunki/` ma wiersz w `rysunki.csv` i odwrotnie, licencja z listy dozwolonych, `zrodlo_url` z dozwolonych domen; (d) wartości słownikowe w CSV z list; (e) adresy YouTube nie są stroną główną kanału; (f) `--znaczniki` wypisuje wszystkie `[ADRIAN: …]`, `[RYSUNEK: …]`, `[SPRAWDZIĆ: …]` z plikiem i numerem linii (do raportu); (g) `--dowody` sprawdza plik dowodu dla każdego R-xxx.
- `styl.py`: wypisuje linie z: „ — ”, „ - ” między słowami, „to nie … to …”, słowami z czarnej listy (najlepszy, genialny, must, niezwykle, kompleksowy, innowacyjny, dedykowany, musisz, powinieneś, gwarant, na pewno, zdasz), listami `- **…:**`, cudzysłowami prostymi `"…"`, HTML poza komentarzami; oraz zdania z liczbami i pierwsze wystąpienia słów akademickich bez wyjaśnienia w akapicie.
- `linki.py`: dla każdego adresu w trzech CSV robi GET przez proxy (urllib, `SSL_CERT_FILE` z `/root/.ccr/ca-bundle.crt`), zapisuje kod i tytuł strony do `robocze/linki-YYYY-MM-DD.csv`.
- `dlugosc.py`: liczba znaków i stron (1800 znaków) na rozdział i razem, bez komentarzy HTML.

- [ ] Utworzyć szkielet i CSV z nagłówkami.
- [ ] Napisać cztery skrypty; sprawdzić na szkielecie, że `sprawdz.py` przechodzi na pustych danych i wykrywa wstrzyknięty błąd (R-999 w tekście bez wiersza; wiersz rysunku z licencją CC BY-NC).
- [ ] Wpis w `POSTEP.md` i `DECYZJE-AGENTA.md`; commit „chemia-po-maturze: szkielet i skrypty sprawdzające”.

### Zadanie 1: Pilotaż A, rozdział 3 dla chemii organicznej

**Pliki:** `tresc/03-skad-sie-uczyc.md` (sekcja „Chemia organiczna”), `dane/zasoby.csv`, `robocze/dowody/`, `robocze/przeglad2-organiczna.md`, `ROZBIEZNOSCI.md`.

**Metoda szukania kandydatów (ta sama dla każdego przedmiotu w zadaniu 3):**
1. Polskie: `WebSearch` po hasłach „chemia organiczna skrypt pdf site:edu.pl”, „chemia organiczna wykład site:edu.pl”, „repozytorium otwarte zasoby chemia organiczna”; sprawdzić otwarte repozytoria (open.agh.edu.pl, repozytoria UJ/UW/PW/PWr, e-podręczniki uczelni), kanały YouTube polskich wykładowców znalezione przez wyszukiwarkę (nie z pamięci). Każdy kandydat otwieram; do rejestru trafia to, co ma treść pierwszego roku i działa bez logowania.
2. Angielskie z listy startowej zlecenia: Professor Dave Explains (playlisty Organic Chemistry), Khan Academy (Organic chemistry course), The Organic Chemistry Tutor (playlista organiczna), Crash Course Chemistry (filmy o organicznej), MIT OCW 5.12, LibreTexts Organic Chemistry, Master Organic Chemistry, Chemistry Steps, Organic Chemistry Portal, Chemguide (organic). Plus OpenStax Organic Chemistry (podręcznik otwarty). Rozszerzenie: to, co wyszukiwarka pokaże jako strony z mechanizmami.
3. Podręczniki: 1–2 polskie, 1–2 angielskie, sprawdzone w katalogu Biblioteki Narodowej (katalogi.bn.org.pl) lub u wydawcy (PWN, Wiley, Oxford, Pearson); zapis wydania i roku.

**Dowód na zasób** (`robocze/dowody/R-xxx.txt`): adres, data, metoda (yt-dlp/curl/web-fetch), a potem surowe dane: lista tytułów filmów (dla playlisty), tytuły i pierwsze akapity 2–3 podstron (dla strony), wpis katalogu (dla książki). Opis w CSV piszę dopiero po przeczytaniu dowodu.

**Format opisu w tekście** (ustalany w tym pilotażu): nagłówek `###` z rodzajem (kanały wideo / strony i artykuły / podręczniki / polskie materiały uczelni), w środku akapit na zasób: nazwa z `[R-xxx]`, 2–3 zdania „co w środku”, zdanie „kiedy sięgnąć”, w nawiasie język i poziom. Bez tabel w tej sekcji (tabele słabo niosą 3 zdania).

- [ ] Zebrać kandydatów (polskie, potem angielskie), zapisać listę z werdyktem w `robocze/kandydaci-organiczna.md` (przyjęty/odrzucony/powód; odrzuceni idą potem do raportu).
- [ ] Dla przyjętych: dowód, wiersz w CSV, akapit w tekście.
- [ ] Podręczniki: sprawdzić w katalogu, wpisać.
- [ ] `sprawdz.py`, `styl.py`, `linki.py` czyste.
- [ ] Drugi ślepy przegląd: osobny przebieg, otwieram każdy adres ponownie, zapisuję kilka słów bez patrzenia na opis do `robocze/przeglad2-organiczna.md`, potem porównuję; różnice do `ROZBIEZNOSCI.md` i poprawka.
- [ ] Wpis w `DECYZJE-AGENTA.md`: co w formacie zmieniam po pilotażu. `POSTEP.md`. Commit, push.

### Zadanie 2: Pilotaż B, rozdział 4c spektroskopia

**Źródła do przeczytania w całości:** OpenStax Organic Chemistry (CC BY 4.0), rozdziały 12 (spektrometria mas i spektroskopia IR) i 13 (NMR), rozdział o UV-Vis (14.7–14.9 lub gdzie jest, do ustalenia ze spisu treści); OpenStax Chemistry 2e rozdz. 6.1 (fale elektromagnetyczne) jako podstawa; LibreTexts tam, gdzie OpenStax nie ma (np. spektroskopia atomowa/UV-Vis w analityce). Pobieram tekst stron (`curl` + `pandoc -t plain`), zapisuję w `robocze/lektury/`.

**Układ wprowadzenia** (wzorzec dla 04a, 04b, 04d): „Czym to jest” (pół strony), „Dlaczego to spotkasz” (z sylabusów, cytowane `[Z-xxx]` po zadaniu 5; na razie `[SPRAWDZIĆ: sylabusy]`), „Co widać w widmie i po co” (IR, NMR ¹H, UV-Vis, MS; po akapicie każde), „Skąd uczyć się dalej” (zasoby `[R-xxx]`, w tym nowe wiersze w `zasoby.csv`). Każde zdanie merytoryczne z komentarzem `<!-- OpenStax Organic Chemistry, 12.6 -->`. Rysunki: `[RYSUNEK: …]` albo plik z Commons/OpenStax po sprawdzeniu licencji (zadanie 11 dopina).

- [ ] Pobrać i przeczytać rozdziały; notatka „co z którego rozdziału” w `robocze/lektury/spektroskopia.md`.
- [ ] Napisać `04c-spektroskopia.md` (2–3 strony) z komentarzami.
- [ ] Zasoby do „dalej” przez tę samą ścieżkę co w zadaniu 1 (dowód, CSV).
- [ ] Przegląd: każde zdanie merytoryczne ma komentarz albo `[SPRAWDZIĆ]`; `sprawdz.py`, `styl.py` czyste. Wpis w `DECYZJE-AGENTA.md` o formacie komentarzy. Commit, push.

### Zadanie 3: Rozdział 3 dla pozostałych przedmiotów

Kolejno: chemia ogólna i nieorganiczna; chemia fizyczna; chemia analityczna; biochemia (dla medycznych i biotechnologii); matematyka jako jedno hasło (gdzie nadrobić logarytmy, pochodne, całki: Khan Academy, Professor Dave Mathematics, polskie otwarte materiały, jeśli są). Metoda identyczna jak w zadaniu 1, w tym `robocze/kandydaci-<przedmiot>.md` i podręczniki z katalogu. Lista startowa angielska: Professor Dave (General Chemistry, Biochemistry), Khan Academy (Chemistry library), The Organic Chemistry Tutor (General Chemistry, Physical Chemistry playlisty, jeśli są), Crash Course Chemistry, MIT OCW 5.111/5.60, LibreTexts (General, Physical, Analytical, Biochemistry), Chemguide (physical, inorganic), NIST WebBook i PubChem (jako „gdzie sprawdzić dane”), Chemistry World (artykuły).

- [ ] Każdy przedmiot: kandydaci → dowody → CSV → tekst → skrypty czyste → commit („chemia-po-maturze: rozdział 3, chemia fizyczna”).
- [ ] Na końcu etapu drugi ślepy przegląd wszystkich nowych zasobów (`robocze/przeglad2-reszta.md`), `ROZBIEZNOSCI.md`.
- [ ] `dlugosc.py`: jeśli rozdział 3 wychodzi poza 12–20 stron, notatka w `DECYZJE-AGENTA.md` dlaczego. `POSTEP.md`, commit, push.

### Zadanie 4: Sylabusy, zbiór

**Uczelnie (po trzy, pierwsza i druga to te, których systemy odpowiadają z tego środowiska; trzecia do sprawdzenia, przy braku dwie wystarczą):**

| Kierunek | Uczelnie |
|---|---|
| chemia | UJ (USOS, działa), UW (USOS, działa), UAM lub PW |
| medycyna | WUM (sylabus.wum.edu.pl, działa), UJ CM (USOS UJ), GUMed lub UM Poznań |
| stomatologia | WUM, UJ CM, UM Lublin lub UM Wrocław |
| weterynaria | SGGW, UP Wrocław, UP Lublin lub UWM |
| farmacja | WUM, UJ CM, UM Poznań lub GUMed |
| analityka medyczna | WUM, UJ CM, UM Lublin lub UM Wrocław |
| biotechnologia | UJ, UW, PWr lub PW |
| inżynieria i technologia chemiczna | PW, PWr, PŁ lub AGH |

UM Łódź odpada (serwis sylabusów odcięty przez sieć); zapis w raporcie.

**Metoda na uczelnię:** (1) katalog USOS „szukaj przedmiotu” z cookie jar, filtr po jednostce i roku 2026/27, inaczej 2025/26; (2) strona wydziału/programu studiów (plan + karty przedmiotów, często PDF, `pdftotext`); (3) archive.org, gdy strona zniknęła. Trzy podejścia, potem notatka braku. Z każdego sylabusu zapisuję: nazwę przedmiotu, semestr, formę zajęć i godziny, ECTS, treści programowe, literaturę, formę zaliczenia. Kopia: `zrodla/<kierunek>-<uczelnia>-<przedmiot>.txt` z nagłówkiem (adres, data, uczelnia, kierunek, rok), tekst skrócony do treści i literatury, gdy PDF jest duży.

- [ ] Dla każdego kierunku i uczelni: lista przedmiotów pierwszego roku z chemią w nazwie lub treści, wiersze `Z-xxx` w `zrodla.csv`, kopie.
- [ ] Tabela zbiorcza kierunek × uczelnia × przedmioty do `robocze/sylabusy-tabela.md` (trafi do raportu), z brakami.
- [ ] Wybrać 2–3 pary/trójki przedmiotów o tej samej nazwie na różnych uczelniach do porównania zakresu (np. „Chemia organiczna” na chemii UJ i technologii chemicznej PW; „Chemia” na lekarskim WUM i UJ CM). Commit, push.

### Zadanie 5: Rozdział 2 i odgałęzienia w rozdziale 3

- [ ] Mapa: dla każdego z 20 modułów kursu wiersz tabeli: moduł → przedmioty pierwszego roku, w których wraca (z `[Z-xxx]`), co dochodzi nowego (z treści sylabusa). Tabela w Markdown plus 2–4 strony tekstu: jak czytać tabelę, co jest zupełnie nowe (aktywność, kwanty, spektroskopia, laboratorium, odesłania do rozdziału 4).
- [ ] Porównanie 2–3 przedmiotów o tej samej nazwie: tekst „na przykład na X… a na Y…”, jako ilustracja punktu 2 Adriana (jego zdanie stoi samo).
- [ ] Odgałęzienia na końcu rozdziału 3: cztery krótkie sekcje (medycyna, stomatologia, weterynaria, farmacja, analityka medyczna razem jako „kierunki medyczne” z rozróżnieniem tam, gdzie sylabusy się różnią; chemia; biotechnologia; inżynieria i technologia), każda: które zasoby z rozdziału są dla Ciebie i w jakiej kolejności, z `[Z-xxx]` tam, gdzie powołuję się na sylabus.
- [ ] Uzupełnić w 04c sekcję „Dlaczego to spotkasz” sylabusami. Skrypty czyste, commit, push.

### Zadanie 6: Rozdziały 1 i 0

- [ ] Rozdział 1 „Inna gra” (3–5 stron): punkty 1–3 Adriana jako rdzeń (pierwsza osoba, brzmienie ze zlecenia, rozwinięte, nie zmienione), cztery zasady z punktów 4–7 jako podrozdziały `###`. Dodatki ze źródeł (bezosobowo, z `[Z-xxx]`): jak czytać sylabus (na przykładzie prawdziwego sylabusa z zadania 4: gdzie są treści, literatura, forma zaliczenia), jak czytać podręcznik akademicki wybiórczo (źródło otwarte do znalezienia: np. OpenStax „College Success”, CC BY, rozdział o czytaniu; jeśli nic odpowiedniego, bez tego dodatku). Słownik akademicki wyjaśniany w miejscu użycia. Miejsca `[ADRIAN: …]` tam, gdzie potrzebny przykład z korepetycji.
- [ ] Lista kontrolna w `robocze/adrian-punkty.md`: punkt 1–12 → plik, linia, brzmienie.
- [ ] Rozdział 0 „Wstęp” (1–2 strony): dla kogo, po co, zdanie o „ścianie na pierwszym roku” w pierwszej osobie, zdanie „bonus nie uczy chemii, pokazuje, gdzie ona jest”, jak czytać wybiórczo (mapa rozdziałów, ścieżki dla kierunków).
- [ ] `styl.py` czysty, commit, push.

### Zadanie 7: Rozdział 4a aktywność

- [ ] Źródła: OpenStax Chemistry 2e (rozdziały o równowadze i roztworach: 13.x, 11.x; sprawdzić, gdzie wspomina aktywność i współczynnik aktywności), LibreTexts Physical Chemistry (strony o aktywności, roztworach elektrolitów, Debye–Hückel jako nazwa, bez wyprowadzeń); lektura dalsza płatna: Atkins „Chemia fizyczna” (wydanie PWN, sprawdzone w katalogu). Notatka w `robocze/lektury/aktywnosc.md`.
- [ ] Tekst (2–3 strony) według wzorca z 04c: dlaczego stężenie z matury przestaje wystarczać, czym jest aktywność i współczynnik aktywności, gdzie to spotkasz (sylabusy chemii fizycznej, analitycznej, chemii na farmacji), skąd dalej. Komentarze źródłowe przy każdym zdaniu merytorycznym. Commit.

### Zadanie 8: Rozdział 4b chemia kwantowa

- [ ] Źródła: OpenStax Chemistry 2e rozdz. 6 (struktura elektronowa, od fal przez Bohra do orbitali i liczb kwantowych) i 8 (orbitale molekularne), LibreTexts Physical Chemistry (wstęp do mechaniki kwantowej: równanie Schrödingera jako idea). Piela „Idee chemii kwantowej”: aktualne wydanie sprawdzone u wydawcy (PWN) i w katalogu BN, opis ze spisu treści, jako lektura dalsza; angielska wersja „Ideas of Quantum Chemistry” (Elsevier) również z katalogu.
- [ ] Sylabusy: co mówią o kwantach na chemii i inżynierii (przedmioty „chemia kwantowa”, „chemia teoretyczna”, „podstawy chemii kwantowej”) i że na medycznych ich zwykle nie ma; zdanie Adriana z punktu 9 zostaje.
- [ ] Tekst (2–3 strony), komentarze, zasoby „dalej”. Commit.

### Zadanie 9: Rozdział 4d laboratorium

- [ ] Źródła otwarte: LibreTexts (Chemistry Lab Techniques / „Organic Chemistry Lab Techniques” Nicholsa, CC BY-NC-SA, cytowanie dozwolone, kopiowanie rysunków nie), publicznie dostępne regulaminy BHP pracowni polskich wydziałów (jako `[Z-xxx]`, „na przykład regulamin pracowni X”), sylabusy laboratoriów z zadania 4 (forma zaliczenia: wejściówki, sprawozdania). Punkt 10 Adriana jako rama.
- [ ] Tekst (2–3 strony): BHP w jednym akapicie, dziennik laboratoryjny, sprawozdanie (co zawiera, z sylabusów), kolokwium wejściowe (czym jest, jak się do niego uczyć z instrukcji do ćwiczenia), skąd dalej. Komentarze źródłowe. Commit, push.

### Zadanie 10: Rysunki

- [ ] Lista potrzebnych rysunków z `[RYSUNEK: …]` w tekście (głównie 04c, 04b, 04a).
- [ ] Dla każdego: szukanie w Wikimedia Commons (API `imageinfo`/`extmetadata`: `LicenseShortName`, `Artist`, `Attribution`), odrzucanie NC i braków; alternatywnie rysunki OpenStax (CC BY 4.0, atrybucja według zasad OpenStax, bez logo). Pobranie do `rysunki/`, wiersz w `rysunki.csv`, podpis w tekście zastępuje `[RYSUNEK]` tam, gdzie znaleziono.
- [ ] `sprawdz.py` czysty (licencje z listy). Commit.

### Zadanie 11: Rozdział 5, weryfikacja całości, raport, README, zip

- [ ] `05-zrodla.md` generowany skryptem `skrypty/zrodla_md.py` z obu CSV: dwie listy, podział na rozdziały (z tego, w którym pliku `[R-xxx]`/`[Z-xxx]` występuje), „co z tego wzięliśmy” z kolumny `opis`/`uwagi`.
- [ ] Pełny przebieg: `sprawdz.py`, `sprawdz.py --dowody`, `styl.py`, `linki.py` (wszystkie adresy raz jeszcze, wynik w `robocze/`), `dlugosc.py`.
- [ ] Przeczytanie całości po kolei jako 19-latek: słownik akademicki, przejścia między rozdziałami, powtórzenia; poprawki.
- [ ] `RAPORT.md`: rozdziały z długościami (z `dlugosc.py`), odrzucone zasoby z powodem (z `robocze/kandydaci-*.md`), tabela sylabusów z brakami, lista znaczników (z `sprawdz.py --znaczniki`), pytania do zleceniodawcy z rekomendacją, ograniczenia środowiska (transkrypcje YouTube, UM Łódź).
- [ ] `README.md` folderu: co tu jest, stan, jak czytać, jak uruchomić skrypty. `POSTEP.md` zamknięty.
- [ ] `zip -r chemia-po-maturze.zip chemia-po-maturze/` obok folderu w repo; commit, push.

---

## Samokontrola planu względem zlecenia

- Cztery rzeczy do oddania: rozdziały (zad. 1–9), rejestry (0, 1, 3, 4, 10), rysunki (10), raport (11). ✔
- Kolejność pracy ze zlecenia: pilotaż organiczna + spektroskopia (1–2), reszta rozdz. 3 (3), sylabusy i rozdz. 2 z odgałęzieniami (4–5), rozdz. 1 i 0 (6), reszta rozdz. 4 (7–9), rozdz. 5, rysunki, weryfikacja, raport (10–11). ✔
- Weryfikacja 1–4 ze zlecenia: ślepy przegląd (1, 3), skrypt (0, 11), komentarze w rozdz. 4 (2, 7–9), lektura jako 19-latek (11). ✔
- „Kiedy gotowe”: każdy punkt listy ma zadanie. ✔
- Ryzyko otwarte: transkrypcje YouTube niedostępne; zapis w `uwagi` każdego zasobu wideo i w raporcie, nie blokuje pracy.
