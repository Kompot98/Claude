# Raport: szkic bonusu „Chemia po maturze”

*Stan na 3.11.2026. Agent pracował samodzielnie według `zlecenie/ZLECENIE-agent-w-chmurze.md` i `zlecenie/KONTEKST-KaNaU.md`. Wszystkie decyzje z uzasadnieniem są w `DECYZJE-AGENTA.md`, dziennik etapów w `POSTEP.md`.*

## Co powstało

Wszystkie rozdziały z układu zlecenia istnieją w `tresc/` i da się je czytać po kolei i wybiórczo. Długość w stronach znormalizowanych (1800 znaków, bez komentarzy HTML):

| Rozdział | Znaki | Strony |
|---|---|---|
| 00-wstep.md | 2711 | 1,5 |
| 01-inna-gra.md | 7370 | 4,1 |
| 02-co-z-matury-zamienia-sie-w-co.md | 9514 | 5,3 |
| 03-skad-sie-uczyc.md | 26222 | 14,6 |
| 04a-aktywnosc.md | 5285 | 2,9 |
| 04b-chemia-kwantowa.md | 5245 | 2,9 |
| 04c-spektroskopia.md | 8548 | 4,7 |
| 04d-laboratorium.md | 5829 | 3,2 |
| 05-zrodla.md | 37565 | 20,9 |
| razem | 108289 | 60,2 |

Rozdziały 0–4 mają razem około 39 stron, w przedziale 25–45 ze zlecenia. Rozdział 5 to listy źródeł generowane z rejestrów (D-14). Rozdział 3 ma 14,6 strony. Wprowadzenie o spektroskopii ma 4,7 strony zamiast 2–3, bo obejmuje cztery metody i dwa zastosowania UV-Vis (D-10).

- **Rozdział 0, wstęp.** Zdanie Adriana o „ścianie na pierwszym roku”, dla kogo jest bonus, co jest w środku i jak czytać wybiórczo.
- **Rozdział 1, „Inna gra”.** Punkty 1–7 Adriana dosłownie, w pierwszej osobie. Dodane bezosobowo: jak czytać sylabus (na przykładzie prawdziwej karty przedmiotu), legalne drogi do podręczników (biblioteka, IBUK Libra na przykładzie poradnika UWr, podręczniki otwarte, starsze i angielskie wydania), czytanie podręcznika wybiórczo.
- **Rozdział 2, mapa.** Tabela 20 modułów kursu (moduł XI w jednym wierszu) na przedmioty pierwszego roku, z odwołaniami do sylabusów; cztery tematy zupełnie nowe; trzy porównania „ta sama nazwa, inna treść”.
- **Rozdział 3, zasoby.** Sześć przedmiotów (organiczna, ogólna i nieorganiczna, fizyczna, analityczna, biochemia, hasło o matematyce), w każdym najpierw polskie materiały uczelni, potem podręczniki, filmy, strony. Na końcu odgałęzienia dla sześciu grup kierunków.
- **Rozdział 4.** Cztery wprowadzenia (aktywność, chemia kwantowa, spektroskopia, laboratorium), każde z komentarzem HTML wskazującym miejsce w przeczytanym źródle otwartym przy zdaniach merytorycznych. Przeczytane fragmenty źródeł leżą w `zrodla/lektury/`.
- **Rozdział 5.** Dwie listy: 61 zasobów polecanych i 32 źródła cytowane, przy rozdziale pierwszego cytowania.

Rejestry: `dane/zasoby.csv` (61 pozycji, każda z plikiem dowodu w `robocze/dowody/`), `dane/zrodla.csv` (32 pozycje: 23 sylabusy i plany studiów z kopiami tekstowymi w `zrodla/`, 9 podręczników i stron), `dane/rysunki.csv` (pusty, D-13).

## Zasoby sprawdzone i odrzucone

Każdy otwarty. Szczegóły w `robocze/kandydaci-organiczna.md` i `robocze/kandydaci-reszta.md`.

| Kandydat | Adres | Werdykt | Powód |
|---|---|---|---|
| Khan Academy, „Organic chemistry” (angielska i polska wersja) | https://www.khanacademy.org/science/organic-chemistry, https://pl.khanacademy.org/science/organic-chemistry | odłożony | Strona wymaga JavaScriptu i zwraca automatom stronę „Client Challenge”; nie udało się odczytać listy działów. Polska wersja „Chemia” (ogólna) wyrenderowała się, więc do ponownej próby przy chemii ogólnej. |
| Akademia Chemii, „Cały kurs” | wynik wyszukiwania YouTube | odrzucony | Komercyjny kurs maturalny; zasady marki wykluczają nazywanie konkurencyjnych kursów. |
| Olimpiada Chemiczna, „Chemia organiczna cz. 2” | wynik wyszukiwania YouTube | odłożony | Materiał olimpijski, poziom szkolny rozszerzony; do sprawdzenia całej playlisty przy chemii ogólnej. |
| Wojciech Szczepankiewicz, „Wprawka z chemii organicznej”, „Podstawy reakcji cykloaddycji 1,3-dipolarnej” | wynik wyszukiwania YouTube | odrzucony | Pojedyncze filmy bez playlisty kursowej; za mało, by opisać jako zasób do pierwszego roku. |
| Jarosław Polański, filmy „introduction to organic synthesis” (2021) | wynik wyszukiwania YouTube | odrzucony | Synteza organiczna, poziom wyższych lat; po angielsku mimo dopisku „polish”. |
| UŚ, playlista „Portal edukacyjny Instytutu Chemii e-chem” | https://www.youtube.com/playlist?list=PLlhOYvtSn-fvVZQjkVELf0tS9ZNhMzkuV | odrzucony (duplikat) | Mieszanka: te same syntezy co R-003 plus matematyka, fizyka i chemia analityczna; lepiej linkować playlisty tematyczne. Wykłady z matematyki do rozważenia przy haśle o matematyce. |
| Politechnika Warszawska, konspekt wykładu, prace domowe, egzaminy z rozwiązaniami | https://zcho.ch.pw.edu.pl/dyd_inz1.html | odrzucony | Odnośniki na stronie są, ale pliki dają błąd 404. Działa tylko nazewnictwo (R-019). |
| UMW, skrypt do ćwiczeń z chemii organicznej | https://www.umw.edu.pl/sites/default/files/files/skrypt_v_beta_8_poprawa_2016.pdf | odrzucony | Oznaczony „tylko do użytku wewnętrznego studentów”. |
| Politechnika Gdańska, „Chemia organiczna dla zainteresowanych” | https://press.pg.edu.pl/ | odrzucony | Na stronie wydawnictwa tylko spis treści; brak dostępu do treści. |
| LibreTexts, „Organic Chemistry (OpenStax)” i „Organic Chemistry (Morsch et al.)” | https://chem.libretexts.org/Bookshelves/Organic_Chemistry | odrzucony (duplikat) | Przeróbki podręcznika McMurry'ego; oryginał OpenStax jest w rejestrze (R-016). |
| LibreTexts, inne książki z półki organicznej (Roberts i Caserio, Wade, Bruice, Smith) | https://chem.libretexts.org/Bookshelves/Organic_Chemistry | odrzucony | Wystarczy jeden otwarty podręcznik ogólny (R-016) i jeden pod kierunki biologiczne (R-017); więcej wydłuża listę bez nowej funkcji. |
| Przemysław Mastalerz, „Chemia organiczna” / „Elementarna chemia organiczna” | katalog BN | odrzucony | Ostatnie wydania w katalogu BN z 2000 r.; trudno dostępne. |
| CrashCourse „Chemistry” (oficjalna seria) | kanał CrashCourse | odłożony | YouTube oznacza ją jako „kurs”, którego lista filmów nie jest dostępna bez przeglądarki; kopie u innych użytkowników odrzucone (nie oryginał). Seria organiczna CrashCourse jest w rejestrze (R-009). |
| Khan Academy: „Organic chemistry”, matematyka, biologia (PL i EN) | khanacademy.org | odłożony | Test antybotowy przy każdej próbie; nie da się opisać bez zgadywania. |
| Chemistry World (Royal Society of Chemistry) | https://www.chemistryworld.com/ | odłożony | Kod 405 i test „Human Verification” dla curl, Chromium i agenta pobierającego strony. Do sprawdzenia ręcznie: to byłoby źródło artykułów popularnonaukowych z obietnicy kursu. |
| Education in Chemistry (RSC), Compound Interest | https://edu.rsc.org/, https://www.compoundchem.com/ | odłożony | Kody 405 i 403 dla automatu. |
| Polski „Orbital” | wyszukiwanie | odrzucony | Nie znaleziono wydania online; tylko pojedynczy rekord w repozytorium UJ. |
| Tomasz Rusak, „Chemia Fizyczna” | https://www.youtube.com/playlist?list=PLccNfZ38gUFCTvTWaFYJSX7t3WXG75NCj | odrzucony | Kanał prywatny bez wskazania uczelni, playlista z powtórzeniami filmów i mieszanką kierunków (analityka medyczna, farmacja II rok). |
| ICHIP studies, „Technologia Chemiczna” | https://www.youtube.com/playlist?list=PLz6Tb_9xrO-GBoges9pcSujBF-6Pdj_LD | odrzucony | Kanał bez wskazania autora wykładów i uczelni; nie wiadomo, czy nagrania są udostępnione za zgodą prowadzącego. Technologia chemiczna to też raczej wyższe lata. |
| Imago Biologia, „Biochemia” | https://www.youtube.com/playlist?list=PLoD3zZHEGfJuvBoGlR06KXJjlFE4Vkem9 | odrzucony | Materiał szkolny pod maturę z biologii; zasady marki wykluczają polecanie konkurencyjnych kursów maturalnych. |
| MaxMed, „Metabolizm – Biochemia” | https://www.youtube.com/playlist?list=PLy0mEBG4sI-nr8l6OntT9jpyBJETrBeT9 | odrzucony | Sześć filmów, autor niezidentyfikowany; za mało, by polecać obok R-051 i R-052. |
| Znitrowani, „Chemia analityczna” | https://www.youtube.com/playlist?list=PLzBTAuJbzUwRUMJRqIt1ureWLHcoAUbe6 | odrzucony | Sześć filmów na poziomie szkolnym (próba Tollensa, barwienie płomienia). |
| Witold Banasik, „Chemia wykłady” | https://www.youtube.com/playlist?list=PL30YvuB-c6JyiH0ra_bSgE73B57taB5XV | odrzucony | Scenariusze doświadczeń szkolnych, nie wykład akademicki. |
| The Organic Chemistry Tutor, „Biochemistry” | https://www.youtube.com/playlist?list=PL0o_zxa4K1BWnb_W5mEnzvmp23QZCOO7G | odrzucony | 10 filmów, w całości pokryte przez R-051 i R-052. |
| LibreTexts, „Fundamentals of Biochemistry” (Jakubowski, Flatt) | https://bio.libretexts.org/Bookshelves/Biochemistry/Fundamentals_of_Biochemistry_(Jakubowski_and_Flatt) | odrzucony | Działa, ale drugi otwarty podręcznik biochemii obok R-053 nie dodaje nowej funkcji. Można dodać przy wydaniu. |
| Lee, „Zwięzła chemia nieorganiczna”; Pajdowski, „Chemia ogólna” | katalog BN | odrzucony | Ostatnie wydania w katalogu BN z lat 1999; trudno dostępne. |
| Atkins, „Podstawy chemii fizycznej” | katalog BN | odrzucony | Jedyne wydanie w BN z 1999 r. |
| Zbigniew Kęcki, „Podstawy spektroskopii molekularnej” | katalog BN | odrzucony | Ostatnie wydanie 1998; do spektroskopii wystarczą R-023 i R-024. |
| UŚ, „Wykłady UŚ Maturzystów” | kanał UŚ | odrzucony | Pod maturzystów, nie pod studentów. |
| Piotr Skurski, kanał „Chemia kwantowa” (playlisty „Notacja Diraca”, „Twierdzenie Riesza”, „Przestrzeń dualna”, „Twierdzenie spektralne”) | https://www.youtube.com/channel/UCBLlbGsf9QyIhzONqbN1hMQ | odłożony | Formalizm matematyczny mechaniki kwantowej, poziom wyższych lat; nie pasuje do wprowadzenia na pierwszy rok. Polski i wartościowy na później. |
| Wikimedia Commons (rysunki) | https://commons.wikimedia.org/ | odłożony | API i serwer plików odpowiadały kodem 429 („too many requests”) dla adresu środowiska przez cały etap 10; licencji pojedynczych plików nie dało się sprawdzić. |

## Sylabusy

Kierunek × uczelnia × przedmioty pierwszego roku z chemią. Źródła w `dane/zrodla.csv`, kopie w `zrodla/`.

| Kierunek | Uczelnia | Rok | Przedmioty I roku z chemią (godziny, ECTS) | Źródło |
|---|---|---|---|---|
| chemia | UJ | 2025/26 | Podstawy chemii (sem. 1; wykł. 30, konw. 30, ćw. 30; 7 ECTS; egzamin) i laboratorium; w katalogu USOS także chemia analityczna (kod I roku) | Z-003 |
| chemia | UW | b.d. | Chemia ogólna (sem. 1; wykład i proseminarium, 60 h zajęć; 6 lub 4 ECTS) i laboratorium | Z-004 |
| medycyna | UJ CM | 2026/27 | — ; Biochemia (sem. 1–2; w sem. 2 egzamin, 12 ECTS) | Z-005 |
| medycyna | WUM | 2025/26 | — ; chemia dopiero na II roku: Biochemia z elementami chemii (180 h, 17 ECTS) | Z-006 |
| medycyna | UMB | 2025/26 | Chemia (30 h, 2 ECTS) i Biochemia (145 h, 11 ECTS) | Z-007 |
| stomatologia | UJ CM | 2024/25 | — ; na II roku Biochemia z elementami chemii | Z-008 |
| stomatologia | UMB | 2026/27 (plan), 2025/26 (sylabus) | Chemia zintegrowana z materiałoznawstwem (20 h, 1 ECTS) i Biochemia (85 h, 6 ECTS) | Z-009, Z-010 |
| weterynaria | SGGW | 2026/27 | Chemia (sem. 1; wykł. 15, lab. 30; 4 ECTS; egzamin), Biochemia (1) (wykł. 15, lab. 45; 5 ECTS) | Z-011 |
| weterynaria | UP Lublin | 2025/26 (rozkład), b.d. (sylabus) | Chemia (sem. 1; 4 ECTS) | Z-012, Z-013 |
| farmacja | UJ CM | 2026/27 | Chemia ogólna i nieorganiczna (sem. 1; 7 ECTS; egzamin) | Z-014 |
| farmacja | WUM | 2024/25 | Chemia ogólna i nieorganiczna (sem. 1–2; wykł. 25, sem. 10, ćw. 90; 11 ECTS) | Z-015 |
| analityka medyczna | UJ CM | 2026/27 | Chemia ogólna i nieorganiczna (sem. 1; 4 ECTS; egzamin) | Z-016 |
| analityka medyczna | UM Łódź | 2025/26 | Chemia ogólna i nieorganiczna (sem. 1; wykł. 15, lab. 35, ćw. rach. 10, e-learning 5; 4 ECTS) | Z-017 |
| analityka medyczna | WUM | 2025/26 | Chemia analityczna, Chemia fizyczna, Chemia ogólna i nieorganiczna, Chemia organiczna | Z-018 |
| biotechnologia | UKSW | 2025/26 | Chemia ogólna I (sem. 1; wykł. 30, ćw. 30, lab. 30; 7 ECTS) | Z-019 |
| biotechnologia | UR | cykl 2023/24–2026/27 | Chemia ogólna i nieorganiczna (sem. 1; wykł. 30, lab. 30; 6 ECTS) | Z-020 |
| inżynieria (technologia chemiczna) | PP | 2026/27 | Chemia ogólna i nieorganiczna 1 (sem. 1; wykł. 45, ćw. 30; 7 ECTS), cz. 2 w sem. 2 | Z-021, Z-024 |
| inżynieria (inżynieria chemiczna i procesowa) | PP | 2026/27 | Chemia ogólna i nieorganiczna 1 (sem. 1; wykł. 30, ćw. 30; 5 ECTS) | Z-022 |
| inżynieria (technologia chemiczna) | PW | 2025/26 | Chemia (sem. 1; wykł. 45, ćw. 30; 5 ECTS), Chemia – laboratorium i Chemia nieorganiczna (sem. 2); chemia analityczna i fizyczna od sem. 3 | Z-023 |

### Czego nie znaleziono

(najwyżej trzy podejścia na uczelnię)

| Kierunek | Uczelnia | Co próbowano | Wynik |
|---|---|---|---|
| chemia | trzecia uczelnia (UWr, UAM) | wyszukiwarka; strona wydziału UWr | znaleziono tylko sylabusy II roku (UWr, chemia medyczna); pominięto, dwie uczelnie wystarczają |
| medycyna | PUM | plik PDF z 2023/24 ze strony dziekanatu | 404, plik usunięty |
| medycyna | UM Łódź | sylabusy.umed.pl | serwis niedostępny z sieci środowiska (502 na bramce) |
| stomatologia | WUM | folder „Sylabusy 25-26” na wls.wum.edu.pl (wyszukiwarka) | brak sylabusu chemii I roku w wynikach; w programie lekarskim WUM chemia jest na II roku |
| weterynaria | UPWr | sylabus.upwr.edu.pl (wynik wyszukiwarki) | trafiony sylabus farmakologii, nie chemii; nie szukano dalej (dwie uczelnie są) |
| weterynaria | SGGW | szczegółowa karta przedmiotu „Chemia” | serwis pokazuje listę przedmiotów z godzinami i ECTS, karta wymaga JavaScriptu |
| biotechnologia | UJ | USOS UJ (WBT-BT636) | przedmiot w katalogu bez aktywnego cyklu |
| inżynieria | PW | karty ects.coi.pw.edu.pl | przekierowanie na stronę główną; użyto informatora kierunku (Z-023) |

## Miejsca do uzupełnienia

### `[ADRIAN: …]`

- 01-inna-gra.md, linia 17: tu jeden przykład z Twoich korepetycji ze studentem, który uczył się „z książki”, a wykładowca pytał o coś, co było tylko na jego slajdach.
- 01-inna-gra.md, linia 35: tu przykład, jeśli masz: jak materiały od starszego rocznika zmieniły przygotowanie Twojego ucznia do konkretnego kolokwium.
- 01-inna-gra.md, linia 56: tu jedno zdanie o tym, że Twoje prace licencjacka i magisterska były pisane po angielsku, jeśli chcesz to podać jako przykład.
- 02-co-z-matury-zamienia-sie-w-co.md, linia 61: tu jedno zdanie z Twojego doświadczenia z korepetycji, jeśli pasuje, np. przykład studenta, którego zaskoczyło, że przedmiot o znanej nazwie wyglądał zupełnie inaczej niż u kolegi z innej uczelni.
- 03-skad-sie-uczyc.md, linia 25: tu jedno zdanie, czy znasz polskie materiały do organicznej, które Twoi studenci faktycznie wykorzystywali, np. skrypty konkretnych katedr; wyszukiwanie znalazło niewiele otwartych polskich materiałów poza nagraniami UŚ.
- 03-skad-sie-uczyc.md, linia 141: jeśli masz doświadczenie z korepetycji z biochemii na kierunku lekarskim, tu jedno zdanie o tym, z czym studenci mają największy kłopot; jeśli nie uczysz biochemii, ten akapit można usunąć.
- 04b-chemia-kwantowa.md, linia 33: tu jedno zdanie, dlaczego polecasz właśnie Pielę, jeśli chcesz to dopowiedzieć.
- 04d-laboratorium.md, linia 21: tu przykład z korepetycji, jeśli masz: jak student przygotowywał się do wejściówki i co okazało się najważniejsze.

### `[RYSUNEK: …]`

- 04a-aktywnosc.md, linia 19: schemat jonu Fe³⁺ otoczonego „atmosferą jonową” z przewagą anionów, obok jonu SCN⁻ otoczonego przewagą kationów; podpis: atmosfera jonowa zmniejsza „widoczny” ładunek jonu
- 04b-chemia-kwantowa.md, linia 13: porównanie modelu Bohra (elektron na kołowej orbicie) z orbitalem 1s przedstawionym jako chmura gęstości prawdopodobieństwa; podpis: na maturze orbita, na studiach prawdopodobieństwo
- 04c-spektroskopia.md, linia 13: widmo elektromagnetyczne od promieniowania gamma do fal radiowych, z zaznaczonymi zakresami używanymi w spektroskopii UV-Vis, IR i NMR oraz strzałką „rośnie energia fotonu”
- 04c-spektroskopia.md, linia 36: porównanie widm IR etanolu i etanalu z zaznaczonym szerokim pasmem O–H w etanolu i ostrym pasmem C=O w etanalu
- 04c-spektroskopia.md, linia 40: widmo ¹H NMR bromoetanu z podpisanym trypletem CH₃ i kwartetem CH₂ oraz zaznaczonym sygnałem wzorca TMS przy 0 ppm
- 04d-laboratorium.md, linia 29: przykładowa strona dziennika laboratoryjnego: tytuł ćwiczenia, równanie reakcji, tabela odczynników z kolumnami „masa molowa, gęstość, ilość zaplanowana, ilość użyta, liczba moli”, pole na obserwacje

### `[SPRAWDZIĆ: …]`

- 02-co-z-matury-zamienia-sie-w-co.md, linia 35: wiersze XII–XVII opierają się na spisie przedmiotów (Z-018, Z-023), bez szczegółowych treści sylabusów chemii organicznej pierwszego roku; „co dochodzi” jest wzięte z typowego podręcznika (R-016, rozdziały odpowiednich grup) i warto je potwierdzić sylabusem organicznej przy wydaniu.
- 04a-aktywnosc.md, linia 37: w których rozdziałach Atkinsa i Minczewskiego jest aktywność; książek nie przeglądano.
- 04c-spektroskopia.md, linia 42: opis procedury krzywej wzorcowej zweryfikować z rozdziałem 5 Harveya „Standardizing Analytical Methods”, którego nie przeczytano w całości.

Do tego chemik powinien przejrzeć cały rozdział 4: każde zdanie merytoryczne ma komentarz z miejscem w źródle, ale przekład na polski i skróty są agenta. Przykład z IR (alkohol i aldehyd) jest wyprowadzony z tabeli źródła i oznaczony w komentarzu jako własny.

## Uwagi o słowach Adriana

Żadne zdanie z punktów 1–12 nie wydało się nie do obrony; wszystkie stoją w tekście (lista w `robocze/adrian-punkty.md`). Dwie uwagi redakcyjne. Zdanie z punktu 2 („Nie dlatego, że chemia jest wszędzie inna, tylko dlatego, że…”) ma konstrukcję, której zasady głosu każą unikać; zostało bez zmian, bo to słowa Adriana. Punkt 12 („matematyka to matematyka”) stoi w trzeciej osobie w zdaniu o tym, dlaczego bonus nie ma rozdziału o matematyce.

## Ograniczenia środowiska, które wpłynęły na wynik

- YouTube: listy filmów w playlistach dostępne, opisy pojedynczych filmów tylko czasem (limit 429), transkrypcji brak. Opisy zasobów wideo powstały z pełnych list tytułów i długości (D-04, D-08).
- Khan Academy, Chemistry World, Education in Chemistry, Compound Interest, IBUK Libra: testy antybotowe lub kody 403/405. Khan Academy po polsku („Chemia”) udało się odczytać raz przez przeglądarkę; reszta odłożona.
- Wikimedia Commons: kod 429 przez cały etap rysunków (D-13).
- Serwis sylabusów UM w Łodzi (sylabusy.umed.pl) odcięty przez sieć środowiska; kartę przedmiotu wzięto ze strony zakładu.
- Kilka serwerów uczelni nie wysyła certyfikatu pośredniego; dociągnięto go z adresu AIA przy włączonej weryfikacji (D-11).

## Pytania do zleceniodawcy

1. **Licencja OpenStax.** W 2026 OpenStax publikuje „Chemistry 2e” i „Organic Chemistry” na CC BY-NC-SA 4.0, nie na CC BY, jak zakłada zlecenie (D-05). Rekomendacja: nie używać rysunków OpenStax w kursie; teksty polecać i cytować jak teraz, a siedem rysunków z opisów `[RYSUNEK]` narysować u siebie.
2. **„Artykuły” z obietnicy kursu.** Strona kursu obiecuje „książki, kanały, artykuły”. Artykuły objaśniające są (Master Organic Chemistry, Chemistry Steps, Chemguide, LibreTexts), ale serwisy z artykułami popularnonaukowymi (Chemistry World, Education in Chemistry) były dla agenta niedostępne. Rekomendacja: przy wydaniu otworzyć Chemistry World ręcznie i, jeśli część artykułów jest bezpłatna, dopisać jedno hasło w rozdziale 3 przy chemii ogólnej.
3. **Khan Academy.** Polska „Chemia” jest w rejestrze (R-027) na podstawie jednego odczytu. Rekomendacja: sprawdzić ręcznie, czy polska Khan Academy ma też kurs chemii organicznej, i jeśli tak, dopisać go jako polski materiał w rozdziale 3.
4. **Piela.** Polskie wydanie „Idei chemii kwantowej” jest z 2011 roku, angielskie trzecie z 2020. Rekomendacja: polecać polskie na start, angielskie jako nowsze; jedno zdanie Adriana w miejscu `[ADRIAN]` w 4b, dlaczego Piela.
5. **Materiały od starszych roczników.** Rozdział 1 mówi o nich zgodnie z punktem 5, bez wskazywania konkretnych serwisów z notatkami. Rekomendacja: zostawić tak; serwisy z cudzymi materiałami mają te same problemy prawne co serwisy z kopiami książek.

## Jak sprawdzić i odtworzyć

Z katalogu `chemia-po-maturze/`:

```
python3 -I skrypty/sprawdz.py --dowody --znaczniki
python3 -I skrypty/styl.py --liczby
python3 -I skrypty/linki.py --ca robocze/ca-z-certyfikatami-posrednimi.pem
python3 -I skrypty/dlugosc.py
python3 -I skrypty/zrodla_md.py
```

`styl.py` zgłasza też sygnały do ręcznej kontroli (pojęcia akademickie); obecne sygnały to fałszywe alarmy: „wykład” we wstępie (słowo powszechne, wyjaśnione w rozdziale 1), „warunków” w rozdziale 1 (nie „warunek” jako pojęcie), „kolokwium” we wstawce `[ADRIAN]`, „dziennik laboratoryjny” w pierwszym zdaniu 4d (słowa Adriana, wyjaśnione kilka akapitów niżej), „seminarium” w rozdziale 5 (lista źródeł).
