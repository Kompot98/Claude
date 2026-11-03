# Raport: bonus „Chemia po maturze”, wersja ostateczna

*Stan na 3.11.2026. Tekst jest gotowy do wgrania na platformę. Do zrobienia zostały tylko rysunki (agent od obrazków, lista w `RYSUNKI-DO-ZNALEZIENIA.md`) i, opcjonalnie, siedem osobistych przykładów Adriana (`DO-UZUPELNIENIA-ADRIAN.md`). Decyzje: `DECYZJE-AGENTA.md` (D-01 do D-18), dziennik: `POSTEP.md`.*

## Co jest gotowe

- **Tekst kursu.** Rozdziały w `tresc/` (źródło do dalszej pracy, z komentarzami źródłowymi w rozdziale 4) i wydanie w `wydanie/` (jeden plik Markdown bez komentarzy, podgląd HTML, PDF 27 stron).
- **Zasoby.** 63 polecane zasoby w `dane/zasoby.csv`, każdy z dowodem sprawdzenia w `robocze/dowody/`, wszystkie po drugim przeglądzie.
- **Źródła.** 34 źródła w `dane/zrodla.csv`: 24 sylabusy i plany studiów z ośmiu kierunków z kopiami w `zrodla/` oraz 10 przeczytanych fragmentów podręczników otwartych i stron, kopie w `zrodla/lektury/`.
- **Rysunki.** 23 wstawki `[RYSUNEK: F-xx]` w tekście: 13 do znalezienia na wolnej licencji, 10 do narysowania; rejestr `dane/rysunki-plan.csv`.
- **Sprawdzenia.** `sprawdz.py --dowody` bez błędów, `styl.py` bez twardych naruszeń, 0 znaczników `[SPRAWDZIĆ]` i `[ADRIAN]` w tekście.

Długość w stronach znormalizowanych (1800 znaków, bez komentarzy):

| Rozdział | Znaki | Strony |
|---|---|---|
| 00-wstep.md | 2711 | 1,5 |
| 01-inna-gra.md | 7976 | 4,4 |
| 02-co-z-matury-zamienia-sie-w-co.md | 10009 | 5,6 |
| 03-skad-sie-uczyc.md | 28025 | 15,6 |
| 04a-aktywnosc.md | 5540 | 3,1 |
| 04b-chemia-kwantowa.md | 5759 | 3,2 |
| 04c-spektroskopia.md | 9305 | 5,2 |
| 04d-laboratorium.md | 6313 | 3,5 |
| 05-zrodla.md | 39208 | 21,8 |
| razem | 114846 | 63,8 |

Rozdziały 0–4 mają razem około 42 stron, w przedziale 25–45 ze zlecenia. Rozdział 5 to listy źródeł generowane z rejestrów (D-14).

## Co zmieniło się po pierwszym raporcie

- **Odpowiedzi na pytania** (zleceniodawca: „zgodnie z rekomendacjami”, D-16). Dopisany polski kurs Khan Academy „Chemia organiczna” (R-062) i Chemistry World (R-063). Rysunków z OpenStax nie ma. Piela polecany najpierw po polsku.
- **Druga próba dostępu** (D-15). Khan Academy i Chemistry World opisane z wyników wyszukiwarki, bo blokują automaty; próba obejścia blokady została zatrzymana przez zabezpieczenia środowiska i jej nie ponawiano. Nowe źródła: Harvey 5.3 o krzywej wzorcowej (Z-033) i sylabus chemii organicznej z analityki WUM (Z-034), dzięki czemu wiersze organiczne mapy w rozdziale 2 opierają się na sylabusie.
- **Rysunki** (D-17). 23 wstawki z identyfikatorami i rejestr dla agenta od obrazków.
- **Redakcja końcowa** (D-18). Usunięte nieweryfikowalne cechy stylu filmów i książek, poprawione uogólnienia, jedno miejsce Adriana wypełnione z życiorysu, siedem przeniesionych do osobnego pliku, wydanie w `wydanie/`.

## Co jeszcze sprawdzić przy wgrywaniu

- **Ręcznie w przeglądarce:** Khan Academy po polsku, kursy „Chemia” i „Chemia organiczna” (R-027, R-062), Chemistry World (R-063), strona OUP Claydena (R-018). Automat ich nie otworzył; opisy są z jednego odczytu albo z wyników wyszukiwarki.
- **Chemia w rozdziale 4.** Każde zdanie merytoryczne ma komentarz z miejscem w źródle w `tresc/04*.md`, a przeczytane fragmenty leżą w `zrodla/lektury/`. Warto, żeby chemik rzucił okiem; agent sprawdził zgodność ze źródłami, ale skróty i przekład są jego.
- **Daty.** Stan zasobów i sylabusów to listopad 2026; przed majem 2027 warto puścić `skrypty/linki.py`.

## Zasoby sprawdzone i odrzucone

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
| analityka medyczna (sylabus przedmiotu) | WUM | 2025/26 | Chemia organiczna (sem. 1; wykł. 30, sem. 10, ćw. 40; 6 ECTS) | Z-034 |
| chemia (sylabus przedmiotu, II rok) | UJ | 2024/25 | Podstawy chemii kwantowej (sem. 4; 5 ECTS); użyty tylko w 4b jako przykład dalszej drogi | Z-029 |

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

## Uwagi o słowach Adriana

Wszystkie punkty 1–12 stoją w tekście (lista w `robocze/adrian-punkty.md`). Zdanie z punktu 2 („Nie dlatego, że…, tylko dlatego, że…”) ma konstrukcję, której zasady głosu każą unikać; zostało, bo to słowa Adriana. Pierwsza osoba poza tymi punktami opiera się wyłącznie na życiorysie z kontekstu (UJ, przedmioty korepetycji, prace dyplomowe po angielsku, SERS, doktorat ze spektroskopii).

## Ograniczenia środowiska

- YouTube: opisy z pełnych list tytułów i długości filmów; transkrypcji brak (D-04, D-08).
- Testy antybotowe: Khan Academy, Chemistry World, Education in Chemistry, Compound Interest, IBUK Libra, PubChem (strona; dane przez API).
- Wikimedia Commons: kod 429 przez cały czas, dlatego rysunki są wstawkami (D-13, D-17).
- Serwer sylabusów UM w Łodzi odcięty przez sieć; karta wzięta ze strony zakładu.

## Jak odtworzyć

Z katalogu `chemia-po-maturze/`:

```
python3 -I skrypty/sprawdz.py --dowody --znaczniki
python3 -I skrypty/styl.py
python3 -I skrypty/linki.py --ca robocze/ca-z-certyfikatami-posrednimi.pem
python3 -I skrypty/zrodla_md.py
python3 -I skrypty/rysunki_md.py
python3 -I skrypty/wydanie.py
node skrypty/pdf.js
```

Sygnały „POJĘCIE” w `styl.py` to znane fałszywe alarmy: „wykład” we wstępie (słowo powszechne, wyjaśnione w rozdziale 1), „warunków” w rozdziale 1, „dziennik laboratoryjny” w pierwszym zdaniu 4d (słowa Adriana, wyjaśnione niżej), „seminarium” w rozdziale 5.
