# Przegląd końcowy: `przystepna/chemia-po-maturze-polaczona.md`

Data: 2026-11-04. Przeczytany cały plik (1109 linii). Numery linii odnoszą się do tego pliku. Plik nie był edytowany.

Co sprawdzono ze źródłami (curl przez proxy, bez obchodzenia blokad): Chemguide (haber.html, deltagandk.html, elim.html, elimvsubst.html, fingerprint.html), Harvey 2.1 (4.2, 5.3, 6.9, spis rozdziału 6), OpenStax Chemistry 2e (6.3, 13.2, 16.4), OpenStax Organic Chemistry (6.5, 11.2, 11.4, 12.7, 12.8, 13.3, 13.6, 19.4), Sandtorv (rozdział 1, 1.2), Master Organic Chemistry (cztery tytuły stron), Peverati 9.2, playlista CrashCourse (plus `robocze/dowody/R-009.txt`). Dwie strony Chemguide (`entropy/deltag.html`, `eladd/carbonium.html`) odpowiedziały dziś ekranem weryfikacji antybotowej („One moment, please…”); nie obchodziłem go, więc wartość 160,4 J/(K·mol) sprawdziłem pośrednio (patrz M-10). Rachunki przeliczone ręcznie. Dane o Adrianie porównane z `zlecenie/KONTEKST-KaNaU.md`, uogólnienia o programach z `robocze/sylabusy-tabela.md`.

Format uwagi: lokalizacja; cytat; problem; poprawka; waga; źródło (dla uwag merytorycznych).

---

## 1. Poprawność merytoryczna (rozdział 4 i tabela w rozdziale 2)

### M-01. 4b, Mini-kurs 2, linia 498
Cytat: „Dla gazów, czystych cieczy, ciał stałych i substancji rozpuszczonych, które nie są jonami, γ jest w zwykłych warunkach bliskie 1, więc aktywność praktycznie równa się stężeniu.”
Problem: dla czystej cieczy i czystego ciała stałego aktywność z definicji wynosi 1, a nie „równa się stężeniu” (czyste fazy nie mają stężenia w roztworze; dlatego nie wchodzą do wyrażenia na K). Zdanie w obecnej formie miesza dwa różne przypadki.
Poprawka: „Dla czystych cieczy i ciał stałych aktywność przyjmuje się równą 1; dlatego nie wpisuje się ich do wyrażenia na stałą równowagi. Dla gazów pod niewielkim ciśnieniem i dla cząsteczek obojętnych w roztworze γ jest w zwykłych warunkach bliskie 1, więc aktywność praktycznie równa się ciśnieniu albo stężeniu.”
Waga: ważna.
Źródło: OpenStax Chemistry 2e, 13.2 (czyste fazy pomijane w K; „relative concentration and pressure values are dimensionless”); Peverati 14.1 (definicja aktywności przez potencjał chemiczny).

### M-02. 4e, Mini-kurs 2, linia 850
Cytat: „Druga pułapka: równoważne wodory nie rozszczepiają się nawzajem. Sześć wodorów acetonu daje jeden sygnał bez rozszczepienia (singlet), a nie dwa sygnały.”
Problem: przykład nie ilustruje pułapki. W acetonie dwie grupy CH₃ nie siedzą na sąsiednich węglach (rozdziela je C=O), więc brak rozszczepienia bierze się przede wszystkim z braku sąsiadów z wodorem, a nie z równoważności. Uczeń wyciągnie błędny wniosek, że „singlet = brak sąsiadów”, co nie jest treścią tej pułapki.
Poprawka: „Druga pułapka: równoważne wodory nie rozszczepiają się nawzajem. Sześć wodorów etanu CH₃–CH₃ siedzi na sąsiednich węglach, a mimo to daje jeden sygnał bez rozszczepienia (singlet), bo wszystkie są równoważne. To samo dotyczy czterech wodorów 1,2-dichloroetanu ClCH₂–CH₂Cl.”
Waga: ważna.
Źródło: OpenStax Organic Chemistry, 13.6 (reguła n + 1 dotyczy nierównoważnych protonów na sąsiednich atomach; równoważne protony nie dają wzajemnego rozszczepienia).

### M-03. 4a, Mini-kurs 3, linia 431
Cytat: „K = e¹⁹·³⁵ ≈ 2,53 · 10⁸.”
Problem: w wykładniku zapisanym indeksem górnym nie ma przecinka, więc separator dziesiętny zastąpiono kropką środkową „·”, którą w tym samym tekście używa się jako znaku mnożenia (np. „298 · 0,1188”). Czytelnik może odczytać „e do potęgi 19 razy 35”.
Poprawka: „K = e^(19,35) ≈ 2,53 · 10⁸” albo słownie: „K = e do potęgi 19,35, czyli około 2,53 · 10⁸.” Rachunek jest poprawny: 60 000 / (8,314 · 373) = 19,348; e^19,348 = 2,53 · 10⁸; dla +60 kJ/mol: 3,96 · 10⁻⁹.
Waga: ważna.
Źródło: Chemguide, „Gibbs free energy and equilibrium constants” (Example 1 i 2: ΔG° = ∓60,0 kJ mol⁻¹, 373 K, K = 3,96 · 10⁻⁹ dla wartości dodatniej), sprawdzone dziś.

### M-04. 4a, Mini-kurs 2, linia 407
Cytat: „Wynik jest dodatni: w temperaturze pokojowej, pod ciśnieniem standardowym, woda nie wrze.”
Problem: zdanie jest prawdziwe, ale uczeń, który wie, że kałuża wysycha w 25 °C, zobaczy sprzeczność. ΔG° dodatnie mówi tylko, że przejście do pary o ciśnieniu 1 bar nie jest samorzutne; parowanie do powietrza, w którym pary jest mało (Q < K), zachodzi. To dokładnie różnica ΔG i ΔG° z pułapki w Mini-kursie 3, więc warto ją tu zapowiedzieć jednym zdaniem.
Poprawka: po zdaniu dodać: „Woda mimo to paruje z otwartego naczynia, bo nad nią nie ma pary o ciśnieniu 1 bar; o tym, czym różni się ΔG° od ΔG w konkretnych warunkach, jest pułapka w Mini-kursie 3.”
Waga: ważna (dydaktyka).
Źródło: OpenStax Chemistry 2e, 16.4 (Example 16.11: ΔH° = 44,01 kJ, ΔS° = 118,8 J/K, ΔG° = +8,6 kJ w 298 K, T = 370,5 K = 97,3 °C; dalej ΔG = ΔG° + RT ln Q). Liczby w tekście zgadzają się ze źródłem.

### M-05. 4b, Mini-kurs 3, linia 512
Cytat: „Licząc ze stężeń, dostaje się rozpuszczalność 4,0 · 10⁻⁵ mol/dm³. Licząc z aktywności, 6,0 · 10⁻⁵ mol/dm³ […] Kolejność rachunku jest zawsze taka sama: policz siłę jonową, oszacuj współczynniki aktywności, zapisz stałą na aktywnościach, dopiero potem podstaw stężenia.”
Problem: liczby zgadzają się z Harveyem (Example 6.9.2; „ignoring activity […] underestimates […] by 33%”), ale uczeń nie widzi żadnego kroku, a pierwszy krok jest dokładnie tym, czego nauczył go Mini-kurs 1. Warto go pokazać, żeby trzy mini-kursy 4b złożyły się w jedną całość.
Poprawka: po zdaniu o kolejności rachunku dodać: „Pierwszy krok policzysz już teraz: Mg(NO₃)₂ 0,020 mol/dm³ daje 0,020 mol/dm³ Mg²⁺ i 0,040 mol/dm³ NO₃⁻, więc I = ½ · (0,020 · 2² + 0,040 · 1²) = 0,060 mol/dm³. Resztę, czyli współczynniki aktywności z równania Debye'a-Hückla, pokazuje Harvey.”
Waga: ważna (dydaktyka).
Źródło: Harvey 6.9, Example 6.9.2 („μ = 0.060”, rozpuszczalność 6,0 · 10⁻⁵ mol/L, wcześniej w wodzie 4,0 · 10⁻⁵ mol/L).

### M-06. 4c, „Czym to jest”, linia 536
Cytat: „Pokazali interferencję elektronów przechodzących przez kryształ niklu”.
Problem: Davisson i Germer rejestrowali elektrony rozproszone (odbite) na powierzchni kryształu niklu; przez cienkie folie przepuszczał elektrony G. P. Thomson. Tekst idzie za sformułowaniem OpenStax („electrons travelling through a regular atomic pattern in a crystal”), więc nie jest to błąd względem źródła, ale sformułowanie neutralne jest dokładniejsze.
Poprawka: „Pokazali interferencję elektronów rozproszonych na krysztale niklu”.
Waga: drobna.
Źródło: OpenStax Chemistry 2e, 6.3 (cytat wyżej; „Davisson and Germer used a crystalline nickel target”).

### M-07. 4a, Mini-kurs 2, linia 404
Cytat: „ΔH° = 44,01 kJ.”
Problem: brak odniesienia do ilości; w całym mini-kursie jednostki są pilnowane (pułapka o jednostkach), a tu kJ bez „na mol” może zmylić. OpenStax też pisze „44.01 kJ”, ale dla równania zapisanego na 1 mol wody.
Poprawka: „ΔH° = 44,01 kJ na mol wody (dalej liczymy dla 1 mola).”
Waga: drobna.
Źródło: OpenStax Chemistry 2e, 16.4.

### M-08. 4a, Mini-kurs 2, linia 408
Cytat: „Z dwóch liczb z tablic wyszła temperatura wrzenia z dokładnością do trzech stopni.”
Problem: w kroku 1 i 2 użyto trzech wartości tablicowych (ΔH° oraz S° cieczy i gazu), a nie dwóch; różnica to 2,7 °C, więc „trzech stopni” jest w porządku.
Poprawka: „Z kilku liczb z tablic wyszła temperatura wrzenia z dokładnością do trzech stopni.”
Waga: drobna.
Źródło: OpenStax Chemistry 2e, 16.4 (S° = 70,0 i 188,8 J/(K·mol); ΔH° = 44,01 kJ).

### M-09. 4b, Mini-kurs 1, linie 485 i 488
Cytat: „(dwa jony z każdej cząsteczki soli)” oraz „Ta sama ilość soli w roztworze, a siła jonowa trzy razy większa.”
Problem: sól jonowa nie ma cząsteczek; „ta sama ilość” jest nieprecyzyjna (to samo stężenie molowe, inna masa i inna liczba jonów). Liczby 0,10 mol/dm³ nie są oznaczone jako przykładowe (wymóg właściciela).
Poprawka: linia 481: „**Przykład krok po kroku: NaCl i Na₂SO₄, oba o stężeniu 0,10 mol/dm³ (stężenia przykładowe).**”; linia 485: „(z każdego mola Na₂SO₄ powstają dwa mole Na⁺)”; linia 488: „To samo stężenie soli, a siła jonowa trzy razy większa.”
Waga: drobna.
Źródło: rachunek własny: ½(0,10 + 0,10) = 0,10; ½(0,20 + 0,40) = 0,30. Poprawny.

### M-10. 4a, Mini-kurs 1, linia 385
Cytat: „Z tablic wychodzi ΔS = +160,4 J/(K·mol) […] (wartość ze strony Chemguide o energii Gibbsa).”
Problem: strony Chemguide `entropy/deltag.html` nie dało się dziś otworzyć (ekran weryfikacji antybotowej, nie obchodzony). Wartość jest jednak zgodna z tablicami: S°(CaO) 39,7 + S°(CO₂) 213,6 − S°(CaCO₃) 92,9 = 160,4 J/(K·mol). Nic do poprawy w tekście; zgłaszam tylko, że dzisiejsza weryfikacja była pośrednia.
Waga: drobna (informacja).
Źródło: standardowe entropie molowe (Atkins, tablice), rachunek własny.

### M-11. 4c, Mini-kurs 2, linia 583 wobec linii 621
Cytat: „Od czego zaczyna się zwykle wykład z chemii kwantowej? Od modelu cząstki w pudle” oraz (linia 621) „Efekt fotoelektryczny, od którego zaczyna się wiele wykładów”.
Problem: dwa zdania w tej samej części mówią, że wykład „zwykle” zaczyna się od dwóch różnych rzeczy. Oba uogólnienia są niesprawdzalne; wystarczy jedno, osłabione.
Poprawka: linia 583: „Pierwszy model, który liczy się na wykładzie z chemii kwantowej, to zwykle **cząstka w pudle**: elektron zamknięty między dwiema ścianami.”
Waga: drobna.

### M-12. 4e, Mini-kurs 2, linia 842
Cytat: „jej sygnał leży dalej od TMS, przy około 3,4 ppm. Sygnał CH₃ leży bliżej, przy około 1,7 ppm.”
Problem: liczby są poprawne, ale jako jedyne w tym mini-kursie nie mają podanego źródła (wymóg: liczby ze źródeł albo oznaczone jako przykładowe).
Poprawka: „[…] przy około 3,4 ppm. Sygnał CH₃ leży bliżej, przy około 1,7 ppm (wartości z widma bromoetanu w podręczniku McMurry'ego, podrozdział 13.6 na OpenStax).”
Waga: drobna.
Źródło: OpenStax Organic Chemistry, 13.6 (Figure 13.8: kwartet CH₂Br przy 3,42 δ, tryplet CH₃ przy 1,68 δ, J = 7 Hz).

### M-13. 4d, Mini-kurs 2, linia 716
Cytat: „Dla bromometanu z jonem wodorotlenkowym w acetonie te same trzy pytania wskazują SN2.”
Problem: NaOH słabo rozpuszcza się w acetonie, a jon wodorotlenkowy reaguje z acetonem (kondensacja aldolowa); to nie jest układ, który uczeń zobaczy w podręczniku ani w pracowni. Klasyczny przykład SN2 w rozpuszczalniku aprotonowym to jodek albo cyjanek.
Poprawka: „Dla bromometanu z jonem cyjankowym w DMSO te same trzy pytania wskazują SN2.” (albo „z jonem jodkowym w acetonie”).
Waga: drobna.
Źródło: OpenStax Organic Chemistry, 11.4 i 11.5 (SN2 sprzyja „negatively charged nucleophile in a polar aprotic solvent”).

### M-14. 4d, Mini-kurs 1, linia 662
Cytat: „Zasady rysowania strzałek, za podręcznikiem McMurry'ego (podrozdział 6.5 na OpenStax):”
Problem: cztery reguły McMurry'ego brzmią inaczej (1: elektrony idą od źródła nukleofilowego do ujścia elektrofilowego; 2: nukleofil może być obojętny albo ujemny; 3: elektrofil może być obojętny albo dodatni; 4: reguła oktetu). Reguły 1 i 4 w tekście pokrywają się z McMurrym, reguły 2 i 3 (dokąd strzałka, bilans ładunku) są własnym streszczeniem. Zwrot „za podręcznikiem” sugeruje przekład.
Poprawka: „Zasady rysowania strzałek, na podstawie podręcznika McMurry'ego (podrozdział 6.5 na OpenStax):”
Waga: drobna.
Źródło: OpenStax Organic Chemistry, 6.5 („RULE 1 Electrons move from a nucleophilic source […] to an electrophilic sink”, „RULE 4 The octet rule must be followed”).

### M-15. 4e, Mini-kurs 1, linie 813–818 i rysunek F-18
Cytat: „Przykład krok po kroku: czy utlenianie etanolu do etanalu się udało?”
Problem: merytorycznie poprawne (O–H 3400–3650 znika, C=O 1670–1780 pojawia się; zakresy zgodne z McMurrym 12.7 i 12.8), ale etanal wrze w 20 °C i na pracowni pierwszego roku rzadko ktoś go izoluje i mierzy jego widmo. Przykład działa jako ćwiczenie myślowe; jeśli ma pachnieć pracownią, lepszy jest cykloheksanol → cykloheksanon (ten sam test, pasmo C=O ketonu około 1715 cm⁻¹).
Poprawka (opcjonalna): zamienić etanol/etanal na cykloheksanol/cykloheksanon w kroku 1–4 i w podpisie F-18.
Waga: drobna (dydaktyka).
Źródło: OpenStax Organic Chemistry, 12.8 („sharp, intense peak in the range 1670 to 1780 cm⁻¹”; ketony nasycone około 1715 cm⁻¹).

### M-16. 4f, Mini-kurs 1, linia 939
Cytat: „**Pułapki.** Na pracowni groźne są przede wszystkim nie wybuchy […]. „To tylko rozcieńczony roztwór” nie zwalnia z okularów. Trzecia pułapka: czytać kartę dosłownie”.
Problem: jest „Trzecia pułapka”, a nie ma „Pierwsza” ani „Druga”; czytelnik szuka brakującej.
Poprawka: „**Pułapki.** Pierwsza: na pracowni groźne są przede wszystkim nie wybuchy, tylko oparzenia […]. Druga: „to tylko rozcieńczony roztwór” nie zwalnia z okularów. Trzecia: czytać kartę dosłownie, bez myślenia o skali.”
Waga: drobna.
Źródło (dla przykładu z NaCl): Sandtorv 1.2 („let us examine the SDS of sodium chloride (NaCl)”), potwierdzone.

### M-17. Rozdział 2, tabela, linia 111
Cytat: „równanie Nernsta, potencjał normalny”.
Problem: dziś w podręcznikach i na zajęciach używa się nazwy „potencjał standardowy”; „normalny” to starsza nazwa, uczeń spotka ją rzadko.
Poprawka: „równanie Nernsta, potencjał standardowy elektrody”.
Waga: drobna.
Źródło: OpenStax Chemistry 2e, 17.3 („standard electrode potential”); polskie wydanie Atkinsa używa „potencjał standardowy”.

### M-18. 4b, „Do czego to służy”, linia 469
Cytat: „Krew i woda morska to roztwory o dużej sile jonowej, więc różnica między aktywnością a stężeniem jest w nich realna.”
Problem: siła jonowa krwi (rzędu 0,15 mol/dm³) nie jest „duża” w skali, o której mówi Mini-kurs 1 (0,10 mol/dm³ dla samego NaCl); woda morska (około 0,7 mol/dm³) tak. Zdanie zestawia dwa różne rzędy.
Poprawka: „Krew ma siłę jonową na tyle dużą, że różnica między aktywnością a stężeniem jest mierzalna, a woda morska jeszcze kilka razy większą.”
Waga: drobna.
Źródło: Harvey 11.2 (pomiary potencjometryczne we krwi w przeliczeniu na aktywność); rząd wielkości siły jonowej krwi i wody morskiej z Harveya 6.9 i tablic.

### M-19. 4f, „Do czego to służy”, linia 904
Cytat: „a wynik bez podanej niepewności jest bezwartościowy.”
Problem: zbyt absolutne; w kursie, który unika mocnych słów, lepiej rzeczowo.
Poprawka: „a wynik bez podanej niepewności niewiele znaczy.”
Waga: drobna.

### Sprawdzone i poprawne (bez uwag)
Haber: 400–450 °C, katalizator żelazowy, „only about 15%” (Chemguide, dziś). Woda: ΔH° 44,01 kJ, ΔS° 118,8 J/K, TΔS° 35,4 kJ, ΔG° +8,6 kJ, T = 370,5 K (OpenStax 16.4). K z ΔG° (Chemguide, dziś). Tabela czterech przypadków znaków. I = ½Σcz². Fe³⁺/SCN⁻ z KNO₃ i „oba bezbarwne” (Harvey 6.9, dosłownie „both of which are colorless”). Pb(IO₃)₂ 4,0 i 6,0 · 10⁻⁵, 33% (Harvey 6.9). Liczby kwantowe, powłoka n = 2, 2l + 1. O₂: 12 elektronów walencyjnych, 8 wiążących, 4 antywiążące, rząd 2, dwa niesparowane na π*. Reguły SN1/SN2 i tabela. Addycja nukleofilowa, jon alkoholanowy, NaBH₄ wobec LiAlH₄. Zakres IR 4000–400 cm⁻¹, tabela pasm (OpenStax 12.7/12.8, co do liczby). 0–10 δ i 1–220 δ (OpenStax 13.3, dosłownie). Bromoetan: tryplet/kwartet 3 : 2. A = εbc, „co najmniej trzy wzorce” (Harvey 5.3: „at least three standards”). SDS: 16 sekcji, sekcje 2, 4, 7, 8. Aspiryna: M = 138,12 i 180,16, 0,01448 mol, 2,61 g, 80,5%. Pipeta 10 mL ±0,02 mL, biureta ±0,01–0,03 mL (Harvey 4.2, dosłownie). Średnia 24,10 cm³. Sandtorv 1.4 „The Notebook – Making Sure the Numbers Add Up” istnieje. CrashCourse: odcinki 5 (IR i MS), 26 (¹H NMR), 41 (UV-Vis) zgadzają się z listą playlisty.

---

## 2. Spójność

### S-01. Rozdział 2, tabela, linia 108
Cytat: „entropia, energia Gibbsa, wykresy fazowe, rzędy reakcji, równanie Arrheniusa (4a)”.
Problem: odsyłacz na końcu komórki sugeruje, że 4a omawia też wykresy fazowe, rzędy reakcji i Arrheniusa; 4a ich nie ma (Arrhenius jest tylko linkiem w 4d).
Poprawka: „entropia i energia Gibbsa (4a), wykresy fazowe, rzędy reakcji, równanie Arrheniusa”.
Waga: ważna.

### S-02. Rozdział 2, tabela, linia 105
Cytat: „orbitale molekularne, hybrydyzacja jako narzędzie opisu, symetria cząsteczek, budowa kryształów (4c)”.
Problem: jak wyżej; 4c nie dotyka symetrii ani kryształów.
Poprawka: „orbitale molekularne i hybrydyzacja jako narzędzia opisu (4c), symetria cząsteczek, budowa kryształów”.
Waga: drobna.

### S-03. Rozdział 3, linia 164 wobec 4d, linia 635
Cytat (oba miejsca): „Z matury znasz organiczną jako katalog: grupa funkcyjna, nazwa, kilka reakcji do zapisania.” plus niemal identyczne trzy pytania („Skąd atakuje odczynnik? Dlaczego powstaje ten produkt, a nie inny?”).
Problem: ten sam akapit otwierający powtórzony słowo w słowo w dwóch rozdziałach. Czytelnik, który przejdzie z 3 do 4d (a tekst go tam odsyła w linii 166), przeczyta go drugi raz.
Poprawka: w linii 164 zostawić wersję krótką: „Z matury znasz organiczną jako katalog grup funkcyjnych i reakcji. Na studiach do tego samego materiału dochodzi pytanie „dlaczego”, a odpowiedzią jest **mechanizm reakcji** rysowany zakrzywionymi strzałkami. Większość materiałów niżej jest po to, żeby te strzałki zaczęły mieć sens.” Pełną wersję z trzema pytaniami zostawić w 4d.
Waga: ważna.

### S-04. Wstęp, linia 15
Cytat: „ułożone według przedmiotów: chemia ogólna i nieorganiczna, organiczna, fizyczna, analityczna, biochemia i trochę matematyki.”
Problem: w rozdziale 3 kolejność jest inna: organiczna (linia 162) przed ogólną (linia 216).
Poprawka: „ułożone według przedmiotów: chemia organiczna, ogólna i nieorganiczna, fizyczna, analityczna, biochemia i trochę matematyki.” (albo zamienić kolejność sekcji w rozdziale 3; ogólna pierwsza jest naturalniejsza dla pierwszego semestru).
Waga: drobna.

### S-05. Rozdział 3, linia 160
Cytat: „W każdym przedmiocie najpierw są polskie materiały, potem podręczniki, filmy i strony.”
Problem: biochemia i matematyka nie mają sekcji „Polskie materiały”, analityczna nie ma filmów. Zdanie obiecuje układ, którego nie ma wszędzie.
Poprawka: „Tam, gdzie je znalazłem, najpierw są polskie materiały, potem podręczniki, filmy i strony.”
Waga: drobna.

### S-06. Wstęp, linia 19 i rozdział 5, linia 1015
Cytat: „**Rozdział 5** to spis wszystkich polecanych materiałów z adresami” wobec „Artykuły internetowe z list „Pozostałe zagadnienia” […] nie są tu powtórzone.”
Problem: „wszystkich” we wstępie, „nie wszystkie” w rozdziale 5. Dodatkowo dwie książki z rozdziału 4 nie trafiły do rozdziału 5, choć rozdział 5 mówi, że książki tam są: Nichols, „Organic Chemistry Lab Techniques” (4f, linia 1002) i „Physical Chemistry” z LibreTexts (4b, linia 520; 4c, linia 624).
Poprawka: linia 19: „**Rozdział 5** to spis polecanych kanałów, kursów, stron i książek z adresami, w jednym miejscu.” Do rozdziału 5 dopisać: w „Laboratorium”: „LibreTexts: Lisa Nichols, „Organic Chemistry Lab Techniques” (po angielsku; pierwszy rok): <https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Organic_Chemistry_Lab_Techniques_(Nichols)>”; w „Chemia fizyczna”: „LibreTexts: „Physical Chemistry” (po angielsku; dalej): <https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Physical_Chemistry_(LibreTexts)>”.
Waga: drobna.

### S-07. 4c, linia 530 wobec linii 631
Cytat: „Polecam podręcznik Lucjana Pieli, „Idee chemii kwantowej”.” (akapit otwierający)
Problem: zalecenie Adriana (z notatek, zostaje), ale w akapicie otwierającym trafia do czytelnika, który jeszcze nie wie, czym są kwanty, i bez zastrzeżenia, które jest dopiero w linii 631 („Gdy chemia kwantowa stanie się osobnym przedmiotem”). Piela to podręcznik na lata wyższe; polecony w pierwszym akapicie brzmi jak lektura na start.
Poprawka: usunąć zdanie z linii 530 i zostawić polecenie tylko w linii 631, gdzie ma kontekst (ewentualnie w 631 dodać „Polecam go…” w pierwszej osobie, żeby zalecenie Adriana nie zginęło).
Waga: drobna.

### S-08. 4b, 4c, 4e, linie 453, 530, 766
Cytat: „Każdy na studiach dowie się…”, „Każdy na studiach usłyszy…”, „Każdy na studiach spotka…”.
Problem: trzy z sześciu części zaczynają się tą samą formułą. Z `robocze/adrian-punkty.md` wynika, że to celowe (punkt 9 notatek Adriana „dosłownie”). Jeśli tak ma zostać, nic nie robić; jeśli nie, zróżnicować dwie z trzech.
Poprawka (jeśli zróżnicować): linia 530: „O chemii kwantowej usłyszysz na studiach na pewno, choć w bardzo różnej dawce.”; linia 766: „Spektroskopię spotkasz na każdym kierunku z chemią. Sam pracowałem w niej kilka lat: […]”.
Waga: drobna.

### S-09. Rozdział 3, linia 188
Cytat: „W drugim wydaniu angielskim rozdziały są ułożone głównie według typów reakcji i mechanizmów, a nie według klas związków.”
Problem: to cecha całego Claydena, także pierwszego wydania i polskiego przekładu; zdanie sugeruje, że to nowość drugiego wydania.
Poprawka: „Clayden, także w polskim przekładzie, układa rozdziały głównie według typów reakcji i mechanizmów, a nie według klas związków. Po angielsku jest już [drugie wydanie](…).”
Waga: drobna.

### S-10. Rozdział 2, linia 146
Cytat: „Na biotechnologii wykład i laboratorium mają często tyle samo godzin.”
Problem: w `sylabusy-tabela.md` są dwa sylabusy biotechnologii (30/30 i 30/30). Dwa przypadki to za mało na „często”.
Poprawka: „Na biotechnologii bywa, że wykład i laboratorium mają tyle samo godzin.”
Waga: drobna.

### S-11. Rozdział 3, linia 338
Cytat: „W pierwszym semestrze matematyki bywa tyle samo co chemii albo więcej.”
Problem: tabela sylabusów nie zawiera godzin matematyki; zdanie nie ma pokrycia w zebranych danych. „Bywa” jest uczciwe, ale marka mówi „wszystko da się sprawdzić”.
Poprawka: albo sprawdzić w planie studiów PP/PW i dopisać źródło do `dane/zrodla.csv`, albo skrócić: „Na politechnikach chemia idzie w parze z dużą ilością matematyki od pierwszego semestru.”
Waga: drobna.

### S-12. 4f, lista, linia 1005
Cytat: „**Bufory, które przygotowuje się na wielu pracowniach:** Chemguide „Buffer solutions” i Harvey „9.2 Acid–Base Titrations”.”
Problem: Harvey ma osobny podrozdział o buforach; 9.2 dotyczy miareczkowań i jest już użyty w punkcie wyżej.
Poprawka: zamienić drugi link na „[Harvey, „6.8 Buffer Solutions”](https://chem.libretexts.org/Bookshelves/Analytical_Chemistry/Analytical_Chemistry_2.1_by_David_Harvey/Analytical_Chemistry_2.1_(Harvey)/06%3A_Equilibrium_Chemistry/6.08%3A_Buffer_Solutions)”. Tytuł 6.8 „Buffer Solutions” potwierdzony dziś w spisie rozdziału 6.
Waga: drobna.

### S-13. 4f, lista, linia 1001
Cytat: „Sandtorv, rozdział 1 […] i Sandtorv, „1.2 Safety is Key” […]. Dane o zagrożeniach […] PubChem.”
Problem: 1.2 jest podrozdziałem rozdziału 1, więc formalnie to jedno źródło podane dwa razy plus baza danych; wymóg „co najmniej 2 źródła, w tym artykuł” jest spełniony tylko na styk.
Poprawka: zamienić link do całego rozdziału 1 na „[Sandtorv, „1.4 The Notebook”](…/1.04%3A_THE_NOTEBOOK_%E2%80%93_MAKING_SURE_THE_NUMBERS_ADD_UP)” (adres do sprawdzenia w spisie rozdziału) albo dodać artykuł spoza Sandtorva, np. OpenStax Chemistry 2e, 1.1 „Chemistry in Context” nie pasuje; lepiej PubChem zostawić i dodać Nichols „1.1 Safety” z „Organic Chemistry Lab Techniques” (rozdział General Techniques, który i tak jest w kolejnym punkcie).
Waga: drobna.

### S-14. 4d, lista, linie 748 i 750
Cytat: „Grupy odchodzące: […] OpenStax „11.2 The SN2 Reaction”” oraz „Rola rozpuszczalnika: […] OpenStax „11.4 The SN1 Reaction””.
Problem: u McMurry'ego grupy odchodzące i rozpuszczalnik omawia 11.3 „Characteristics of the SN2 Reaction” (dla SN2) i 11.5 „Characteristics of the SN1 Reaction” (dla SN1); 11.2 i 11.4 opisują sam mechanizm. Etykiety są poprawne, ale link prowadzi obok tematu.
Poprawka: w punkcie „Grupy odchodzące” dodać „[OpenStax, „11.3 Characteristics of the SN2 Reaction”](https://openstax.org/books/organic-chemistry/pages/11-3-characteristics-of-the-sn2-reaction)”; w punkcie „Rola rozpuszczalnika” zamienić 11.4 na „[OpenStax, „11.5 Characteristics of the SN1 Reaction”](https://openstax.org/books/organic-chemistry/pages/11-5-characteristics-of-the-sn1-reaction)” (oba adresy do potwierdzenia curlem; dziś sprawdzałem 11.2 i 11.4, które zwracają 200, a tekst o rozpuszczalniku w 11.4 jest tylko w podsumowaniu).
Waga: drobna.

### S-15. 4d, lista, linia 754
Cytat: „artykuł Master Organic Chemistry o kwasowej hydratacji alkenów”.
Problem: tytuł strony to „Acid Catalyzed Hydration of Alkenes Follows A Key Mechanistic Pattern” (adres: addition-pattern-1-the-carbocation-pathway). Etykieta pasuje; jedyny punkt listy bez tytułu w cudzysłowie, inaczej niż pozostałe.
Poprawka: „[Master Organic Chemistry, „Acid Catalyzed Hydration of Alkenes”](…)”.
Waga: drobna.

### S-16. Rysunki
F-01…F-30 bez F-05: każdy numer występuje dokładnie raz, F-05 nie ma wcale. Jeśli F-05 został usunięty celowo, w porządku; jeśli numeracja ma być ciągła, warto to odnotować w `RYSUNKI-DO-ZNALEZIENIA.md` (nie sprawdzałem tego pliku pod tym kątem).
Waga: drobna.

### Spójność potwierdzona
Wstęp (linia 17) zapowiada 4a–4f i taką listę ma rozdział 4 (linia 342). Każda część 4a–4f ma: „Czym to jest”, „Do czego to służy” (W świecie / Na studiach), trzy mini-kursy, „Pozostałe zagadnienia”. Każdy punkt list ma co najmniej dwa linki, w tym artykuł (poza zastrzeżeniami S-13 i punktem „Prawdziwe widma do ćwiczeń”, linia 888, gdzie są dwie bazy i książka, co jest sensowne). Angielski jako domyślny język nauki jest powiedziany wprost w liniach 82 i 344. Fakty o Adrianie (5 lat ze studentami, UJ, prace po angielsku, nikiel(II), TiO₂/SERS, doktorat ze spektroskopii wzmocnionej powierzchniowo) zgadzają się z `KONTEKST-KaNaU.md`. Trzy układy chemii na kierunku lekarskim (linia 148) mają pokrycie w tabeli sylabusów (UMB, UJ CM, WUM). Opisy playlist US (analityczna: cztery miareczkowania i trzy metody instrumentalne; matematyka: filmy 19–28) i PW („Uwagi do sprawozdań”, 33 min) zgadzają się z `robocze/zasoby-*.json`. Dane bibliograficzne książek (Harper wyd. VIII 2026, Kocjan wyd. III 2023, Atkins/Jones/Laverman 2020, Atkins/de Paula/Keeler 2022, Berg wyd. V 2019) pochodzą z katalogu BN według `dane/zasoby.csv`.

---

## 3. Źródła w listach „Pozostałe zagadnienia”
Sprawdzone tytuły stron (dziś): Master Organic Chemistry „Hydrohalogenation of Alkenes and Markovnikov's Rule”, „How To Use Curved Arrows in Organic Chemistry, With Examples”, „Aldehydes and Ketones: 14 Reactions With The Same Mechanism”, Chemguide „elimination from 2-bromopropane to give propene”, „elimination v nucleophilic substitution in halogenoalkanes”, „infra-red spectra - the fingerprint region”, Peverati „9.2: Temperature Dependence of ΔG”. Wszystkie etykiety w tekście pasują. Uwagi do konkretnych linków są wyżej: S-12 (Harvey 9.2 zamiast 6.8), S-13 (Sandtorv podwójnie), S-14 (OpenStax 11.2/11.4 zamiast 11.3/11.5), S-15 (brak tytułu). Chemguide `eladd/carbonium.html` (linie 747, 754) odpowiedział dziś ekranem antybotowym; w rozdziale jest opisany jako „carbocations”, co zgadza się ze znanym tytułem strony, ale warto sprawdzić go jeszcze raz przed wydaniem.

---

## 4. Styl i czytelność

### T-01. Rozdział 4, wstęp, linie 344 i 346
Cytat: „To nie przypadek: […]” oraz „Kolejność tematów nie jest przypadkowa.”
Problem: ta sama figura retoryczna dwa akapity pod rząd; typowy chwyt tekstu generowanego.
Poprawka: linia 344: „Prawie wszystkie linki prowadzą do stron po angielsku. Jak pisałem w rozdziale 1, angielski jest na studiach domyślnym językiem nauki, a dobre, bezpłatne wyjaśnienia chemii akademickiej są prawie wyłącznie po angielsku.”; linia 346: „Tematy są ułożone tak, że każdy korzysta z poprzedniego.”
Waga: drobna.

### T-02. 4d, Mini-kurs 3, linie 733 i 737
Cytat: „Teraz widzisz, co się dzieje.” oraz „Jeden mechanizm, cała rodzina reakcji.”
Problem: dwie puenty w jednym mini-kursie; druga jest dobra, pierwsza pusta.
Poprawka: usunąć „Teraz widzisz, co się dzieje.”
Waga: drobna.

### T-03. Rozdział 1, linia 63
Cytat: „Na początek najlepiej odezwać się do starosty roku.”
Problem: stopień najwyższy bez potrzeby (zasada marki).
Poprawka: „Na początek odezwij się do starosty roku.”
Waga: drobna.

### T-04. Rozdział 3, linia 236
Cytat: „ma też ogromną playlistę z chemii ogólnej”.
Poprawka: „ma też bardzo długą playlistę z chemii ogólnej”.
Waga: drobna.

### T-05. 4b, linia 457
Cytat: „Zacznijmy od doświadczenia.”
Problem: jedyna forma „my” w tekście pisanym per „Ty”.
Poprawka: „Najpierw doświadczenie.”
Waga: drobna.

### T-06. 4a, „Do czego to służy”, linia 366
Cytat: „Tak samo liczy się, w jakiej temperaturze rozkłada się węglan wapnia w piecu wapiennym, przy jakim reduktorze uda się wydobyć metal z rudy i jakie napięcie da bateria albo ogniwo paliwowe.”
Problem: akapit ma 9 zdań i to jedno z najdłuższych; łatwo je rozbić.
Poprawka: „Tak samo liczy się, w jakiej temperaturze rozkłada się węglan wapnia w piecu wapiennym. Albo przy jakim reduktorze uda się wydobyć metal z rudy. Albo jakie napięcie da bateria lub ogniwo paliwowe.”
Waga: drobna.

### T-07. 4b, Mini-kurs 3, linia 508
Cytat: „Podręcznik „Chemistry 2e” z OpenStax mówi o tym wprost w podrozdziale o stałych równowagi: wzory ze stężeniami to uproszczenie, które na poziomie wstępnym daje niewielki błąd.”
Problem: zgodne ze źródłem (13.2: „For purposes of this introductory text, it will suffice to use the simplified equations […] only modest errors”), ale zdanie-cytat z podręcznika w środku wyjaśnienia hamuje tempo; wystarczy krótsze odesłanie.
Poprawka: „OpenStax pisze o tym wprost w podrozdziale 13.2: wzory ze stężeniami to uproszczenie, zwykle z niewielkim błędem.”
Waga: drobna.

### Zasady marki: wynik sprawdzenia
Brak „—” i „ – ” jako znaków w zdaniu (półpauza występuje tylko w zakresach „400–450 °C”, „0–10 ppm” i w zapisie wiązań „C–O”, co jest poprawne typograficznie). Brak form rodzajowych do czytelnika (wszystkie „-łem” to zdania Adriana w pierwszej osobie, dozwolone). Brak obietnic wyniku („zdasz”, „zaliczysz”). Zaimki „Ty/Twój/Cię” konsekwentnie wielką literą. Nazwy uczelni w zdaniach o godzinach, punktach i programach nie występują; nazwy pojawiają się tylko jako autor materiału (US, SGGW, PW) i „UJ” u Adriana, zgodnie z regułą. Superlatywy: poza T-03 i T-04 tylko opisowe („najczęstszy błąd”, „najważniejsze zagrożenie”), które nie są przechwałką.

---

## 5. Dydaktyka

### D-01. 4b Mini-kurs 2 (linie 492–504) i 4c Mini-kurs 1 (linie 548–558)
Cytat: „**Przykład rozumowania.**” (w obu).
Problem: wymóg właściciela to „przykład krok po kroku” w każdym mini-kursie; te dwa mają akapit ciągły. Treść jest dobra, brakuje tylko struktury, którą uczeń może odtworzyć.
Poprawka (4b MK2): „**Przykład krok po kroku: kwas octowy w czystej wodzie i w roztworze NaCl.** 1. W roztworze z NaCl siła jonowa jest większa. 2. Większa siła jonowa oznacza mniejsze współczynniki aktywności jonów H₃O⁺ i CH₃COO⁻. 3. Stała termodynamiczna, liczona z aktywności, jest taka sama w obu roztworach. 4. Skoro γ zmalało, a iloczyn γ · [jon] ma zostać ten sam, stężenia jonów muszą wzrosnąć. 5. Wniosek: w słonym roztworze kwas jest trochę bardziej zdysocjowany, a stała liczona ze stężeń wychodzi większa niż w czystej wodzie.”
Poprawka (4c MK1): „**Przykład krok po kroku: jak czytać rysunek orbitalu 1s.** 1. Kula na rysunku to nie tor ani skorupka. 2. To powierzchnia, wewnątrz której elektron przebywa na przykład przez 90 procent czasu. 3. Gęstość prawdopodobieństwa jest największa przy jądrze i maleje na zewnątrz bez ostrej granicy. 4. Gdyby narysować powierzchnię dla 99 procent, kula byłaby większa; granica jest umowna.”
Waga: ważna (zgodność z szablonem rozdziału).
Źródło (4b): Harvey 6.9 (wpływ siły jonowej na stałą stężeniową); (4c): OpenStax Chemistry 2e, 6.3 (interpretacja ψ² i powierzchni granicznej).

### D-02. 4a, Mini-kurs 1, linia 383
Cytat: „Trzy sygnały, że ΔS > 0: z cieczy albo ciała stałego powstaje gaz, rośnie liczba moli gazu, ciało stałe rozpuszcza się w cieczy.”
Problem: trzeci sygnał ma wyjątki (sole z silnie hydratowanymi jonami, np. siarczan(VI) wapnia, mają ujemną entropię rozpuszczania); dla pierwszego roku reguła kciuka jest w porządku, ale warto dać słowo „zwykle”, bo mini-kurs zaraz uczy, że intuicja o ΔH też ma wyjątki.
Poprawka: „[…] rośnie liczba moli gazu, ciało stałe rozpuszcza się w cieczy (to ostatnie zwykle, nie zawsze).”
Waga: drobna.
Źródło: Chemguide, „entropy change” (lista sygnałów); wyjątki: tablice ΔS rozpuszczania w Atkinsie.

### D-03. 4e, Mini-kurs 3, linie 860–867
Problem: procedura krzywej wzorcowej jest poprawna i kompletna. Brakuje jednego zdania, po co w ogóle ε się nie zna (zależy od rozpuszczalnika, pH, przyrządu), bo uczeń może zapytać, czemu nie wziąć ε z tablic.
Poprawka: linia 860: „W praktyce ε zwykle nie znasz dokładnie, bo zależy od rozpuszczalnika, pH i samego przyrządu, więc stosuje się **krzywą wzorcową**:”.
Waga: drobna.
Źródło: Harvey 10.2 (odstępstwa od prawa Beera, zależność od warunków).

### D-04. 4f, Mini-kurs 3, linia 993
Cytat: „Wyniki różnią się od średniej najwyżej o 0,05 cm³. To pierwsza, prosta ocena rozrzutu; na zajęciach policzysz ją dokładniej jako odchylenie standardowe.”
Problem: dobre. Można dodać jedno zdanie, jak zapisać wynik, bo krok 5 mówi o cyfrach znaczących, ale nie pokazuje zapisu.
Poprawka: po kroku 5 dodać: „Zapis: V = 24,10 ± 0,05 cm³ (rozrzut z trzech pomiarów).”
Waga: drobna.

### Dydaktyka: co działa
Kolejność w 4a (entropia → ΔG → K) i w 4d (strzałki → SN → C=O) jest właściwa dla maturzysty; pułapki w 4a (jednostki, ΔG a szybkość, ΔG° a ΔG), 4d (strzałka od H⁺, SN2 na trzeciorzędowym, addycja a substytucja acylowa), 4e (brak pasma, zakres liniowości, ślepa próba) i 4f (mokry produkt, przepisywanie instrukcji, cyfry z kalkulatora) są trafne i odpowiadają typowym błędom z pierwszych ćwiczeń. Przykład O₂ w 4c jest dobrze dobrany jako „to, czego nie tłumaczy matura”.

---

## Podsumowanie

Liczba uwag według wagi:
- krytyczne: 0
- ważne: 8 (M-01, M-02, M-03, M-04, M-05, S-01, S-03, D-01)
- drobne: 35 (M-06…M-19, S-02, S-04…S-16, T-01…T-07, D-02…D-04)

Ocena gotowości: tekst jest merytorycznie solidny. Wszystkie rachunki się zgadzają, liczby w przykładach mają pokrycie w cytowanych źródłach (poza wartościami ppm bromoetanu, którym brakuje tylko odsyłacza), zasady marki są przestrzegane, uogólnienia o programach studiów są ostrożne i w większości mają pokrycie w tabeli sylabusów. Do wydania potrzebne są poprawki ośmiu uwag „ważnych”: dwie z nich usuwają stwierdzenia, które mogą utrwalić błędne wyobrażenie (aktywność czystych faz, singlet acetonu), jedna zapis, który da się źle odczytać (e¹⁹·³⁵), dwie wzmacniają spójność między mini-kursami (parowanie wody a ΔG°, siła jonowa w przykładzie Harveya), dwie porządkują odsyłacze i powtórzenie między rozdziałami, jedna dostosowuje dwa mini-kursy do szablonu „krok po kroku”. Drobne można wprowadzić hurtem w jednym przebiegu redakcyjnym. Po tych poprawkach tekst nadaje się do składu.
