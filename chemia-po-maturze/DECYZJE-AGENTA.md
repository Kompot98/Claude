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

## D-05, 2026-11-03: OpenStax nie jest już źródłem rysunków (licencja NC)

**Co:** rysunków z OpenStax nie używam. Jedynym źródłem gotowych rysunków jest Wikimedia Commons z licencją sprawdzoną przy pliku. Teksty OpenStax nadal czytam i cytuję jako źródło (komentarze w rozdziale 4) i polecam jako otwarte podręczniki.
**Dlaczego:** zlecenie zakłada, że OpenStax to CC BY 4.0. W dniu sprawdzenia strony książek „Chemistry 2e”, „Chemistry: Atoms First 2e”, „Organic Chemistry” i „College Success” oraz API OpenStax podają licencję CC BY-NC-SA 4.0 („Textbook content produced by OpenStax is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike License”, stopka z lipca 2026). NC wyklucza użycie w płatnym kursie. Starsze wersje mogły być na CC BY; czy ta licencja nadal obowiązuje dla wcześniej pobranych kopii, to pytanie prawne, którego nie rozstrzygam.
**Odrzucone:** używanie rysunków OpenStax na podstawie starszej licencji. Pytanie do zleceniodawcy w raporcie.

## D-06, 2026-11-03: format rozdziału 3 po pilotażu

**Co:** (1) Nagłówki: `## Skąd się uczyć` dla wstępu, `## <przedmiot>` dla każdego przedmiotu, `### <rodzaj zasobu>` w środku, bo zlecenie dopuszcza tylko `##` i `###`, a podział jest dwupoziomowy. (2) Każdy zasób to akapit: nazwa i `[R-xxx]`, dwa, trzy zdania co w środku, zdanie „kiedy sięgnąć”, na końcu w nawiasie język i poziom. Bez tabel. (3) Kolejność rodzajów: polskie materiały uczelni, podręczniki, kanały wideo, strony i artykuły. Polskie pierwsze, bo zlecenie każe szukać najpierw po polsku. (4) Zasoby bliźniacze (dwie playlisty jednego autora) mogą dzielić akapit, ale każdy ma własne `[R-xxx]`. (5) Na początku przedmiotu krótki akapit, co się zmienia względem matury, bez twierdzeń o sylabusach, dopóki nie ma ich w `zrodla.csv`.
**Dlaczego:** akapit mieści trzy zdania i „kiedy sięgnąć”, czego tabela nie uniesie; stały szablon pozwala czytać wybiórczo.
**Odrzucone:** tabela zasobów; podział najpierw według rodzaju, potem przedmiotu (zlecenie mówi odwrotnie).

## D-07, 2026-11-03: adres płatnego podręcznika w rejestrze

**Co:** w kolumnie `url` przy płatnych podręcznikach polskich jest adres rekordu w API Biblioteki Narodowej (data.bn.org.pl), przy angielskich strona wydawcy. W tekście książka jest podana tytułem, autorem, wydaniem i wydawcą.
**Dlaczego:** BN nie ma stabilnej strony rekordu dla człowieka, a strony PWN i OUP odpowiadają automatom kodem 403. Rekord BN jest sprawdzalnym dowodem wydania. Przy wydaniu można podmienić adres na stronę wydawcy albo katalog biblioteki.
**Odrzucone:** linkowanie do księgarń (oferty się zmieniają, wygląda jak reklama).

## D-08, 2026-11-03: opisy pojedynczych filmów bywają dostępne (uzupełnienie D-04)

**Co:** strona pojedynczego filmu YouTube pobrana zwykłym zapytaniem zawiera opis i datę publikacji, ale YouTube szybko odpowiada kodem 429. Opis filmu pobieram tam, gdzie się uda, i zapisuję w dowodzie; reszta opisów wideo opiera się na pełnych listach tytułów. Transkrypcji nie pobieram.
**Dlaczego:** tak wyszło przy wykładach prof. Polańskiego (opis wykładu 1 i ukryta playlista odczytane ze strony filmu).
**Odrzucone:** obchodzenie limitu (wielokrotne ponawianie w krótkim czasie).

## D-09, 2026-11-03: format rozdziału 4 po pilotażu spektroskopii

**Co:** (1) Układ każdego wprowadzenia: `## <temat>`, krótki akapit otwierający (zdanie Adriana z punktu 9 i, gdzie pasuje, fakt z jego życiorysu), potem `### Czym to jest`, `### Dlaczego to spotkasz`, część merytoryczna (`### Co widać w widmie i po co` albo odpowiednik), `### Skąd uczyć się dalej`. (2) Komentarz źródłowy stoi po zdaniu albo po grupie zdań opartych na tym samym miejscu źródła, w formie `<!-- Z-001: 13.6, akapit o bromoetanie -->`. Identyfikator `Z-xxx` wskazuje wiersz w `zrodla.csv`, a dalej podrozdział i miejsce. (3) Każde wprowadzenie kończy się widocznym zdaniem „Źródła tego wprowadzenia: … [Z-xxx]”, żeby źródła były cytowane także w tekście, a nie tylko w komentarzach. (4) Przeczytane podrozdziały źródeł otwartych leżą w `zrodla/lektury/` jako tekst, żeby chemik sprawdzający rozdział miał je pod ręką. (5) Przykład wyprowadzony przeze mnie z tabeli źródła (alkohol i aldehyd w IR) jest oznaczony w komentarzu jako własny.
**Dlaczego:** zlecenie wymaga, żeby każde zdanie merytoryczne dało się sprawdzić w podanym miejscu; podrozdział plus akapit skraca to sprawdzenie do minuty.
**Odrzucone:** komentarz po każdym pojedynczym zdaniu (przy trzech zdaniach z jednego akapitu źródła trzy identyczne komentarze nic nie wnoszą).

## D-10, 2026-11-03: długość wprowadzenia o spektroskopii

**Co:** 04c ma około 4,8 strony zamiast 2–3. Zostawiam.
**Dlaczego:** spektroskopia to w praktyce cztery metody (MS, IR, NMR, UV-Vis), a UV-Vis ma dwa różne zastosowania (budowa w organicznej, stężenie w analityce). Skrócenie do trzech stron oznaczałoby wyrzucenie jednej metody albo zastosowania analitycznego, które dotyczy kierunków medycznych. Część o zasobach zajmuje około jednej strony.
**Odrzucone:** pominięcie spektrometrii mas (jest w podręcznikach organicznej obok IR i NMR) albo przeniesienie zasobów do rozdziału 3 (zlecenie chce „skąd uczyć się dalej” w każdym wprowadzeniu).
