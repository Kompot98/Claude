"""Krok 2: składa nową wersję połączoną z etapu 1 i nowych fragmentów.
Użycie: python3 -I krok2_scal.py ETAP1 KATALOG_SKRYPTOW WYJSCIE ZASOBY_CSV
"""
import csv, os, re, sys

etap1, skr, wyj, zasoby_csv = sys.argv[1:5]
sys.path.insert(0, skr)
from adresy import A  # noqa: E402

t = open(etap1, encoding="utf-8").read()
bledy = []


def wstaw_adresy(s):
    def zamien(m):
        k = m.group(1)
        if k not in A:
            raise SystemExit(f"nieznany klucz adresu: {k}")
        return A[k]
    return re.sub(r"\{\{(\w+)\}\}", zamien, s)


def bloki(plik):
    s = wstaw_adresy(open(os.path.join(skr, plik), encoding="utf-8").read())
    out, klucz, buf = {}, None, []
    for linia in s.split("\n"):
        m = re.match(r"^@@(\S+)\s*$", linia)
        if m:
            if klucz:
                out[klucz] = "\n".join(buf).strip("\n")
            klucz, buf = m.group(1), []
        else:
            buf.append(linia)
    if klucz:
        out[klucz] = "\n".join(buf).strip("\n")
    return out


def r(stare, nowe, ile=1):
    global t
    n = t.count(stare)
    if n != ile:
        bledy.append((n, stare[:80]))
        return
    t = t.replace(stare, nowe)


R = bloki("n_rozdz.md")
Q = bloki("n_4.md")
PH = wstaw_adresy(open(os.path.join(skr, "n_4b.md"), encoding="utf-8").read()).strip("\n")

# ---------- Wstęp ----------
r("Ten bonus nie uczy chemii. Pokazuje, gdzie ona jest. Dowiesz się, czym chemia na studiach różni się od tej z matury, skąd brać wiedzę, gdy wykład nie wystarcza, i jak nie być zdanym tylko na prowadzącego.",
  "Ten bonus nie uczy chemii. Pokazuje, gdzie ona jest. Dowiesz się, czym chemia na studiach różni się od tej z matury, skąd brać wiedzę, gdy wykład nie wystarcza, i jak nie być zdanym tylko na prowadzącego. Wyjątkiem jest rozdział 4: kilka tematów, które spotka prawie każdy, tłumaczy od podstaw, z przykładami i zadaniami.")
r("Przeczytaj go bez względu na kierunek.",
  "Przeczytaj go bez względu na kierunek. Kończy się planem: co zrobić w wakacje, w pierwszym tygodniu i przed pierwszym kolokwium.")
r("Przy każdym źródle piszę, co w nim jest i kiedy po nie sięgnąć. Na końcu jest skrót dla Twojego kierunku.",
  "Przy każdym źródle jest opis, co w nim jest i kiedy po nie sięgnąć. Na początku jest skrót dla Twojego kierunku.")
r("**Rozdział 4** to sześć wprowadzeń do rzeczy, które spotka prawie każdy: 4a entropia i energia Gibbsa, 4c aktywność, 4d chemia kwantowa, 4e mechanizmy reakcji, 4f spektroskopia i 4g laboratorium. Każde wyjaśnia, czym to jest i do czego służy, a najważniejsze rzeczy uczy dokładniej, w krótkich mini-kursach z przykładami krok po kroku.",
  "**Rozdział 4** to siedem wprowadzeń do rzeczy, które spotka prawie każdy: 4a entropia i energia Gibbsa, 4b pH i bufory, 4c aktywność, 4d chemia kwantowa, 4e mechanizmy reakcji, 4f spektroskopia i 4g laboratorium. Każde mówi na początku, dla kogo jest, potem wyjaśnia, czym to jest i do czego służy, a najważniejsze rzeczy uczy dokładniej, w mini-kursach z przykładami krok po kroku i z zadaniami do samodzielnego rozwiązania.")
r("Rozdział 4 otwórz, gdy na wykładzie pierwszy raz padnie słowo „entropia”, „aktywność” albo „mechanizm”, albo wcześniej, jeśli chcesz zacząć studia z przewagą.",
  "Rozdział 4 otwórz, gdy na wykładzie pierwszy raz padnie słowo „entropia”, „bufor”, „aktywność” albo „mechanizm”, albo wcześniej, w wakacje, jeśli masz ochotę.\n\nJeśli już studiujesz, zacznij od planu na końcu rozdziału 1, a potem otwórz w rozdziale 4 część o temacie najbliższego kolokwium.")
r("Nazwy materiałów w tekście są linkami, a pełna lista adresów jest w rozdziale 5. Wszystkie sprawdziłem w listopadzie 2026.",
  "Nazwy materiałów w tekście są linkami, a adresy kanałów, kursów i książek są zebrane jeszcze raz w rozdziale 5. Wszystkie zostały sprawdzone w listopadzie 2026.")

# ---------- Rozdział 1 ----------
r(" Zdarza się, że na jednej politechnice ten sam przedmiot ma na dwóch kierunkach inną liczbę godzin i inny zakres. Zdarza się też, że na kierunku lekarskim jednej uczelni chemia jest na pierwszym roku, a na innej dopiero na drugim. Więcej przykładów jest w rozdziale 2.",
  " Przykłady z prawdziwych sylabusów są w rozdziale 2.")
r("mówi, co musisz zaliczyć, żeby w ogóle podejść do egzaminu", "mówi, co trzeba zaliczyć, żeby w ogóle podejść do egzaminu")
r("na stronie wydziału albo w osobnym serwisie uczelni. Zacznij od trzech części:",
  "na stronie wydziału albo w osobnym serwisie uczelni. Konto na uczelni nie jest do tego potrzebne: przy pracy nad tym bonusem wszystkie sylabusy dało się otworzyć bez logowania, w katalogu przedmiotów USOS albo w serwisie uczelni. Najprościej wpisać w wyszukiwarkę „sylabus”, nazwę przedmiotu, nazwę uczelni i kierunek. Zacznij od trzech części:")
r("Te, które znalazłem, opisuję w rozdziale 3 jako pierwsze.", "Te, które są, rozdział 3 opisuje jako pierwsze.")
# plan na koniec rozdziału 1
r("\n# Co z matury zamienia się w co\n", "\n" + R["PLAN"] + "\n\n# Co z matury zamienia się w co\n")

# ---------- Rozdział 2 ----------
r("Kurs KaNaU 50/70/90 przeprowadził Cię przez 20 modułów, od budowy atomu po cukry.",
  "Kurs maturalny KaNaU 50/70/90, do którego należy ten bonus, przeprowadził Cię przez 20 modułów, od budowy atomu po cukry; moduł XI ma dwie części.")
r("W trzeciej to, co dochodzi nowego.",
  "W trzeciej to, co dochodzi nowego, a litera w nawiasie, na przykład (4a), odsyła do części rozdziału 4, w której ten temat jest wyjaśniony. Najwięcej nowego dochodzi w wierszach V (energetyka), VII (pH i roztwory elektrolitów) i XI–XVII (chemia organiczna).")
r("aktywność zamiast stężenia, siła jonowa (4c); bufory i równowaga kwasowo-zasadowa w organizmie |",
  "aktywność zamiast stężenia, siła jonowa (4c); bufory, równanie Hendersona-Hasselbalcha i równowaga kwasowo-zasadowa w organizmie (4b) |")
r("| XI. Wstęp do chemii organicznej |", "| XI. Wstęp do chemii organicznej (obie części) |")
r("**Entropia i energia Gibbsa (4a).** Odpowiadają na pytanie, czy reakcja w ogóle zajdzie sama z siebie. Pojawiają się w chemii ogólnej, potem w chemii fizycznej i w biochemii.",
  "**Entropia i energia Gibbsa (4a).** Odpowiadają na pytanie, czy reakcja w ogóle zajdzie sama z siebie. Pojawiają się w chemii ogólnej, potem w chemii fizycznej i w biochemii.\n\n**pH i bufory (4b).** pH znasz z matury, ale na studiach dochodzą bufory, liczone równaniem Hendersona-Hasselbalcha, i równowaga kwasowo-zasadowa organizmu. Na części kierunków medycznych biochemia zaczyna się właśnie od wody, pH i buforów.")
r("Jak to zrobić i na co w nich patrzeć, opisałem w rozdziale 1.", "Jak je znaleźć i na co w nich patrzeć, mówi zasada pierwsza w rozdziale 1.")

# ---------- Rozdział 3 ----------
r("Każde źródło niżej otworzyłem i sprawdziłem. Przy każdym piszę, co w nim jest, kiedy po nie sięgnąć, w jakim jest języku i na jakim poziomie.",
  "Każde źródło niżej zostało otwarte i sprawdzone w listopadzie 2026. Przy każdym jest opis, co w nim jest, kiedy po nie sięgnąć, w jakim jest języku i na jakim poziomie.")
r("Tam, gdzie je znalazłem, najpierw są polskie materiały, potem podręczniki, filmy i strony. Na końcu rozdziału jest skrót dla Twojego kierunku. Pamiętaj",
  "Na początku jest skrót dla Twojego kierunku: od czego zacząć. Potem rozdział idzie przedmiotami. W każdym przedmiocie akapit „Na start” mówi, od czego zacząć, jeśli masz czas na jedno albo dwa źródła; dalej są polskie materiały (tam, gdzie są), podręczniki, filmy i strony. Pamiętaj")
r("Jak zdobyć książkę bez kupowania, opisałem w rozdziale 1.", "Jak zdobyć książkę bez kupowania, mówi rozdział 1.")
# przeniesienie „Dla Twojego kierunku” na początek rozdziału 3
i = t.find("\n## Dla Twojego kierunku\n")
j = t.find("\n# Rzeczy, które spotka prawie każdy\n")
assert 0 < i < j, "nie znaleziono bloku Dla Twojego kierunku"
t = t[:i] + "\n" + t[j:]
k = t.find("\n## Chemia organiczna\n")  # pierwsze wystąpienie, w rozdziale 3
assert k > 0
t = t[:k] + "\n" + R["KIERUNKI"] + "\n" + t[k:]


def przed_naglowkiem(sekcja, naglowek, tekst):
    global t
    a = t.find(sekcja)
    b = t.find(naglowek, a)
    if a < 0 or b < 0:
        bledy.append((0, f"{sekcja} / {naglowek}"))
        return
    t = t[:b] + tekst + "\n\n" + t[b:]


przed_naglowkiem("\n## Chemia organiczna\n", "### Polskie materiały", R["START_ORG"])
przed_naglowkiem("\n## Chemia ogólna i nieorganiczna\n", "### Polskie materiały", R["START_OGOLNA"])
przed_naglowkiem("\n## Chemia fizyczna\n", "### Polskie materiały", R["START_FIZ"])
przed_naglowkiem("\n## Chemia analityczna\n", "### Polskie materiały", R["START_ANAL"])
przed_naglowkiem("\n## Biochemia\n", "### Podręczniki", R["START_BIO"])

r("(Po polsku; krótkie filmy.)", "(Po polsku; krótkie filmy, poziom pierwszego roku.)")
r("(Po polsku.)", "(Po polsku; poziom pierwszego roku.)")

# ---------- Rozdział 4: wstęp ----------
r("Sześć wprowadzeń do tematów, które na studiach wracają na wielu przedmiotach: 4a entropia i energia Gibbsa, 4c aktywność, 4d chemia kwantowa, 4e mechanizmy reakcji, 4f spektroskopia i 4g laboratorium. Każde ma ten sam układ. Najpierw czym to jest. Potem do czego to służy, osobno w świecie poza uczelnią i osobno na studiach. Potem dwa albo trzy mini-kursy, czyli najważniejsze rzeczy wyjaśnione dokładniej, z definicją, przykładem krok po kroku i typową pułapką. Na końcu lista pozostałych zagadnień, a przy każdym co najmniej dwa źródła, w tym zawsze artykuł, który je tłumaczy.",
  "Siedem wprowadzeń do tematów, które na studiach wracają na wielu przedmiotach: 4a entropia i energia Gibbsa, 4b pH i bufory, 4c aktywność, 4d chemia kwantowa, 4e mechanizmy reakcji, 4f spektroskopia i 4g laboratorium. Każde ma ten sam układ. Na początku jest akapit „Dla kogo”, więc od razu wiesz, co możesz pominąć. Potem czym to jest i do czego służy, osobno w świecie poza uczelnią i osobno na studiach. Potem dwa albo trzy mini-kursy, czyli najważniejsze rzeczy wyjaśnione dokładniej, z definicją, przykładem krok po kroku i typową pułapką. Po każdym mini-kursie są zadania „Sprawdź się”, a odpowiedzi do nich stoją na końcu części. Liczby w zadaniach są przykładowe, chyba że przy zadaniu podano źródło. Na końcu każdej części jest lista „Gdzie czytać dalej”: przy każdym zagadnieniu pierwszy link jest prostszy, na start, a drugi idzie głębiej.")
r("Jak pisałem w rozdziale 1, angielski", "Jak mówi zasada czwarta z rozdziału 1, angielski")
r("Energia Gibbsa tłumaczy, dlaczego reakcje w ogóle zachodzą, a aktywność to poprawka do jej wzorów.",
  "Energia Gibbsa tłumaczy, dlaczego reakcje w ogóle zachodzą. pH i bufory to najczęstsze zastosowanie równowag, a aktywność to poprawka do ich wzorów.")

# ---------- 4a ----------
r("Z drugiego przykładu wynika najważniejsza rzecz: **nie wystarczy patrzeć na sam układ**. Trzeba liczyć też to, co dzieje się z otoczeniem. Energia Gibbsa robi to za nas.",
  "Z drugiego przykładu wynika najważniejsza rzecz: **nie wystarczy patrzeć na sam układ**. Trzeba liczyć też to, co dzieje się z otoczeniem. Entropia otoczenia rośnie o tyle, ile ciepła do niego trafiło, podzielone przez temperaturę. Ciepło oddane przez układ to −ΔH, więc ΔS(otoczenia) = −ΔH/T. To samo ciepło oddane w zimnie zwiększa więc entropię otoczenia bardziej niż w cieple, i dlatego woda zamarza w zamrażarce, a w pokoju nie.\n\nStąd bierze się energia Gibbsa. Warunek drugiej zasady, ΔS(układu) − ΔH/T > 0, pomnożony przez −T daje ΔH − TΔS < 0, czyli ΔG < 0. Energia Gibbsa to druga zasada zapisana tak, żeby wystarczyło liczyć sam układ (wyprowadzenie jest w „Chemistry 2e” z OpenStax, podrozdział 16.4).")

# ---------- 4c (aktywność) ----------
r("Gdy zmieszasz bezbarwne roztwory jonów Fe³⁺ i SCN⁻, powstaje",
  "Gdy zmieszasz rozcieńczony, jasnożółty roztwór jonów Fe³⁺ z bezbarwnym roztworem jonów SCN⁻, powstaje")
r("Współczynniki aktywności jonów szacuje się z równania Debye'a-Hückla. Na pierwszym roku wystarczy wiedzieć, że takie równanie istnieje i że wynik zależy od siły jonowej i ładunku jonu.",
  "Współczynniki aktywności jonów szacuje się z **równania Debye'a-Hückla**. W wersji, której używa podręcznik Harveya (podrozdział 6.9), dla roztworów wodnych w 25 °C wygląda ono tak:\n\nlog γ = −0,51 · z² · √I / (1 + 3,3 · α · √I)\n\nz to ładunek jonu, I to siła jonowa, a α to średnica jonu razem z otoczką cząsteczek wody, w nanometrach, odczytywana z tabeli. W bardzo rozcieńczonym roztworze √I jest małe, więc γ jest bliskie 1. Ładunek wchodzi do wzoru w kwadracie, więc współczynniki aktywności jonów dwuwartościowych maleją ze wzrostem siły jonowej dużo szybciej niż jednowartościowych.")
r("**Przykład z liczbami**, z podręcznika analityki Davida Harveya (podrozdział 6.9): jodan ołowiu(II), Pb(IO₃)₂, w roztworze azotanu magnezu o stężeniu 0,020 mol/dm³. Licząc ze stężeń, dostaje się rozpuszczalność 4,0 · 10⁻⁵ mol/dm³. Licząc z aktywności, 6,0 · 10⁻⁵ mol/dm³, czyli o połowę więcej. Pominięcie aktywności zaniża wynik o jedną trzecią. Kolejność rachunku jest zawsze taka sama: policz siłę jonową, oszacuj współczynniki aktywności, zapisz stałą na aktywnościach, dopiero potem podstaw stężenia. Pierwszy krok możesz policzyć już teraz: Mg(NO₃)₂ o stężeniu 0,020 mol/dm³ daje 0,020 mol/dm³ Mg²⁺ i 0,040 mol/dm³ NO₃⁻, więc I = ½ · (0,020 · 2² + 0,040 · 1²) = 0,060 mol/dm³. Resztę, czyli współczynniki aktywności z równania Debye'a-Hückla, pokazuje Harvey.",
  "**Przykład krok po kroku**, z podręcznika analityki Davida Harveya (przykład 6.9.2): rozpuszczalność jodanu ołowiu(II), Pb(IO₃)₂, w roztworze azotanu magnezu o stężeniu 0,020 mol/dm³. Iloczyn rozpuszczalności Ksp = 2,5 · 10⁻¹³.\n\n1. Siła jonowa: Mg(NO₃)₂ daje 0,020 mol/dm³ Mg²⁺ i 0,040 mol/dm³ NO₃⁻, więc I = ½ · (0,020 · 2² + 0,040 · 1²) = 0,060 mol/dm³. Jodanu ołowiu rozpuszcza się tak mało, że jego jonów nie liczymy.\n2. Współczynniki aktywności z równania Debye'a-Hückla, dla obu jonów z α = 0,45 nm: γ(Pb²⁺) = 0,431 i γ(IO₃⁻) = 0,810.\n3. Jeśli rozpuszcza się x mol/dm³ soli, to [Pb²⁺] = x, a [IO₃⁻] = 2x. Iloczyn rozpuszczalności zapisany na aktywnościach: Ksp = 0,431 · x · (0,810)² · (2x)² = 1,131 · x³.\n4. 1,131 · x³ = 2,5 · 10⁻¹³, więc x = 6,0 · 10⁻⁵ mol/dm³.\n5. Bez aktywności byłoby 4x³ = 2,5 · 10⁻¹³ i x = 4,0 · 10⁻⁵ mol/dm³. Pominięcie aktywności zaniża wynik o jedną trzecią.\n\nKolejność rachunku jest zawsze taka sama: policz siłę jonową, oszacuj współczynniki aktywności, zapisz stałą na aktywnościach, dopiero potem podstaw stężenia.")

# ---------- 4d (kwanty) ----------
r("dlaczego 4s zapełnia się przed 3d", "dlaczego szkolna kolejność „4s przed 3d” jest uproszczeniem")
r(" Na farmacji kwanty bywają krótkim wstępem do chemii ogólnej. Na kierunku lekarskim na pierwszym roku zwykle ich nie ma. Jeśli idziesz na medycynę, ta część jest dla ciekawych.", "")
r("### Mini-kurs 1: fala, prawdopodobieństwo i nieoznaczoność\n\nZ falowej natury cząstek wynika",
  "### Mini-kurs 1: fala, prawdopodobieństwo i nieoznaczoność\n\nJak bardzo „falowa” jest cząstka, mówi **długość fali de Broglie'a**: λ = h / (m · v), gdzie h to stała Plancka (6,626 · 10⁻³⁴ J·s), m to masa, a v prędkość. Dla elektronu o prędkości 1,000 · 10⁷ m/s wychodzi λ = 7,274 · 10⁻¹¹ m, czyli fala rzędu rozmiarów atomu. Dla piłki o masie 100 g lecącej z prędkością 35 m/s wychodzi około 1,9 · 10⁻³⁴ m, czyli nic, co dałoby się zmierzyć (oba przykłady są w „Chemistry 2e”, podrozdział 6.3). Dlatego falowe zachowanie widać u elektronów, a nie u piłek.\n\nZ falowej natury cząstek wynika")

# ---------- 4e (mechanizmy) ----------
r("Jak to wygląda na rysunku, pokazuje schemat mechanizmu SN2 w pierwszym mini-kursie niżej.",
  "Jak to wygląda na rysunku, pokazuje schemat mechanizmu SN2 w pierwszym mini-kursie niżej.\n\nDwa narzędzia przydają się od pierwszego wykładu. Pierwsze to **pKa** z części 4b: reakcja kwas–zasada to najprostszy mechanizm, w którym zasada swoją wolną parą odbiera proton, a jej kierunek wyznacza porównanie pKa. Drugie to **rezonans**. Gdy jednej cząsteczki nie da się dobrze opisać jednym wzorem Lewisa, rysuje się kilka **struktur rezonansowych**, a prawdziwa cząsteczka jest czymś pośrednim. W jonie octanowym ładunek ujemny jest rozłożony na oba atomy tlenu, a w jonie etanolanowym siedzi na jednym. Dlatego kwas octowy (pKa 4,76) jest mocniejszym kwasem niż etanol (pKa około 16) mniej więcej sto miliardów razy (podręcznik McMurry'ego, podrozdział 20.2 na OpenStax).")
r("**Pułapki.** Strzałka pokazuje ruch elektronów, a nie ruch atomów.",
  "**Drugi przykład: addycja HBr do propenu, czyli skąd reguła Markownikowa.** Z matury znasz regułę: wodór przyłącza się do tego atomu węgla przy wiązaniu podwójnym, który ma więcej atomów wodoru. Mechanizm mówi, dlaczego.\n\n1. Nukleofilem jest wiązanie π alkenu, a elektrofilem atom wodoru w HBr.\n2. Pierwsza strzałka biegnie od wiązania π do wodoru, druga od wiązania H–Br do bromu. Powstają karbokation i jon Br⁻.\n3. Wodór może trafić na skrajny albo na środkowy węgiel. Gdy trafi na skrajny, ładunek dodatni zostaje na środkowym węglu, który ma dwa podstawniki węglowe. Taki karbokation drugorzędowy jest trwalszy niż pierwszorzędowy i to on powstaje.\n4. Jon Br⁻ atakuje karbokation. Produkt to 2-bromopropan, zgodnie z regułą Markownikowa. Krok po kroku opisuje to Chemguide, na stronie o addycji do alkenów niesymetrycznych.\n\n**Pułapki.** Strzałka pokazuje ruch elektronów, a nie ruch atomów.")
r("Ta sama „wymiana bromu na OH”, a dwie zupełnie różne drogi, z różną szybkością i różną stereochemią.",
  "W obu przypadkach brom ustępuje miejsca nukleofilowi, a drogi są zupełnie różne, z różną szybkością i różną stereochemią.\n\n**Konkurencja: eliminacja.** Ten sam halogenoalkan może zamiast substytucji ulec eliminacji: odchodzą grupa odchodząca i wodór z sąsiedniego węgla, a powstaje alken. Tu też są dwie drogi. **E2** to jeden krok: mocna zasada odrywa proton w tej samej chwili, w której odchodzi grupa odchodząca, a szybkość zależy od stężenia substratu i zasady. **E1** idzie przez ten sam karbokation co SN1, a jej szybkość zależy tylko od stężenia substratu. Eliminacji sprzyjają mocne zasady i wysoka temperatura. Gdy mogą powstać różne alkeny, zwykle przeważa alken bardziej podstawiony, czyli trwalszy. To reguła Zajcewa, którą możesz znać z matury (podręcznik McMurry'ego, podrozdziały 11.7–11.10 na OpenStax).")

# ---------- 4f (spektroskopia) ----------
r("Przykład kalibracji z prawdziwymi liczbami jest w podręczniku analityki Harveya, w podrozdziale 5.3 (link niżej).",
  "**Przykład z liczbami**, z podręcznika analityki Harveya (ćwiczenie 5.3.1): prosta kalibracyjna dla jonów Cu²⁺ ma równanie A = 29,59 dm³/mol · c + 0,015. Próbka ma absorbancję 0,114.\n\n1. Wstaw absorbancję próbki do równania prostej: 0,114 = 29,59 · c + 0,015.\n2. c = (0,114 − 0,015) / 29,59 = 3,35 · 10⁻³ mol/dm³.\n3. Dla porównania: przy kalibracji jednym wzorcem (3,16 · 10⁻³ mol/dm³, absorbancja 0,0931) wyszłoby 3,87 · 10⁻³ mol/dm³, czyli o kilkanaście procent więcej. Kilka wzorców wyrównuje przypadkowe błędy pojedynczych pomiarów.")

# ---------- 4g (laboratorium) ----------
r("3. Wyniki różnią się od średniej najwyżej o 0,05 cm³. To pierwsza, prosta ocena rozrzutu; na zajęciach policzysz ją dokładniej jako odchylenie standardowe.",
  "3. Odchylenie standardowe liczy się ze wzoru s = √[Σ(xᵢ − x̄)² / (n − 1)], gdzie x̄ to średnia, a n liczba pomiarów. Tu odchylenia od średniej to 0; 0,05 i −0,05 cm³, więc s = √[(0 + 0,0025 + 0,0025) / 2] = 0,05 cm³.")
r("5. Policz stężenie ze średniej objętości i podaj wynik z tyloma cyframi znaczącymi, ile uzasadnia najmniej dokładny pomiar. Biureta pozwala odczytać setne części cm³, więc wynik 24,1033 cm³ z kalkulatora udawałby dokładność, której nie ma. Zapis: V = 24,10 ± 0,05 cm³ (rozrzut z trzech pomiarów).",
  "5. Wynik podajesz z tyloma cyframi znaczącymi, ile uzasadnia najmniej dokładny pomiar. Biureta pozwala odczytać setne części cm³, więc wynik 24,1033 cm³ z kalkulatora udawałby dokładność, której nie ma. Zapis: V = (24,10 ± 0,05) cm³, gdzie 0,05 cm³ to odchylenie standardowe z trzech pomiarów.\n6. Ze średniej objętości liczysz stężenie. Jeśli na zmiareczkowanie 25,00 cm³ roztworu HCl zużyto średnio 24,10 cm³ NaOH o stężeniu 0,1000 mol/dm³, to c(HCl) = 0,1000 · 24,10 / 25,00 = 0,09640 mol/dm³. Wynik ma cztery cyfry znaczące, tyle co dane.")

# ---------- Rozdział 4: struktura części ----------
poczatek = t.find("\n# Rzeczy, które spotka prawie każdy\n")
koniec = t.find("\n# Źródła\n")
assert 0 < poczatek < koniec
r4 = t[poczatek:koniec]
czesci = re.split(r"(?m)^(?=## 4[a-g]\. )", r4)
wstep4, reszta = czesci[0], czesci[1:]
nowe = [wstep4.rstrip("\n") + "\n"]
for cz in reszta:
    lit = re.match(r"## 4([a-g])\.", cz).group(1)
    pod = re.split(r"(?m)^(?=### )", cz)
    intro, subs = pod[0], pod[1:]
    out = [intro.rstrip("\n") + "\n\n" + Q[f"4{lit}.DLAKOGO"] + "\n"]
    for s in subs:
        tyt = s.split("\n", 1)[0]
        m = re.match(r"### Mini-kurs (\d):", tyt)
        if m:
            out.append(s.rstrip("\n") + "\n\n" + Q[f"4{lit}.MK{m.group(1)}"] + "\n")
        elif tyt.startswith("### Pozostałe zagadnienia"):
            akap = [a for a in s.split("\n\n")[1:] if a.strip() and not a.lstrip().startswith("- ")]
            blok = "### Gdzie czytać dalej\n\n" + Q[f"4{lit}.LISTA"] + "\n\n"
            blok += "\n\n".join(a.strip() for a in akap)
            blok += "\n\n### Odpowiedzi do zadań „Sprawdź się”\n\n" + Q[f"4{lit}.ODP"] + "\n"
            out.append(blok)
        else:
            out.append(s.rstrip("\n") + "\n")
    nowe.append("\n".join(out))
    if lit == "a":
        nowe.append(PH + "\n")
r4n = "\n".join(nowe)
t = t[:poczatek] + "\n" + r4n.strip("\n") + "\n\n" + R["ZAKONCZENIE"] + "\n" + t[koniec:]

# ---------- Rozdział 5 ----------
z = t.find("\n# Źródła\n")
tresc = t[:z]
zas = list(csv.DictReader(open(zasoby_csv, encoding="utf-8")))
# poziom z nawiasów w rozdziale 3, np. „(Po polsku; poziom pierwszego roku.)”
r3 = tresc[tresc.find("\n# Skąd się uczyć\n"):tresc.find("\n# Rzeczy, które spotka prawie każdy\n")]
poziom_z_r3 = {}
for akap in r3.split("\n\n"):
    m = re.search(r"\((Po (?:polsku|angielsku)[^()]*?)\.?\)\s*$", akap.strip())
    if not m:
        continue
    opis = m.group(1)
    opis = opis[0].lower() + opis[1:]
    for u in re.findall(r"\]\((https?://[^\s]+?)\)(?=[\s.,;:]|$)", akap):
        poziom_z_r3.setdefault(u, opis)
MAPA = {"wprowadzenie": "wprowadzenie", "pierwszy rok": "poziom pierwszego roku", "dalej": "poziom dalszy"}
NADPISZ = {
    "R-005": "po polsku; poziom pierwszego roku na kierunku chemia, poza tym poziom dalszy",
    "R-018": "po angielsku; poziom pierwszego roku na kierunku chemia, poza tym poziom dalszy",
}
DZIALY = [("organiczna", "Chemia organiczna"), ("ogólna i nieorganiczna", "Chemia ogólna i nieorganiczna"),
          ("fizyczna", "Chemia fizyczna"), ("analityczna", "Chemia analityczna"), ("biochemia", "Biochemia"),
          ("matematyka", "Matematyka"), ("chemia kwantowa", "Chemia kwantowa"), ("spektroskopia", "Spektroskopia"),
          ("laboratorium", "Laboratorium"), ("ogólne", "Bazy danych i czasopisma")]
DODATKOWE = {
    "fizyczna": [("LibreTexts: „Physical Chemistry” (podręcznik, rozdziały o aktywności i chemii kwantowej)", "po angielsku; poziom dalszy",
                  "https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Physical_Chemistry_(LibreTexts)")],
    "laboratorium": [("LibreTexts: Lisa Nichols, „Organic Chemistry Lab Techniques”", "po angielsku; poziom pierwszego roku",
                      "https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Organic_Chemistry_Lab_Techniques_(Nichols)")],
    "ogólne": [("IBUK Libra: platforma e-booków z polskimi podręcznikami akademickimi; dostęp i adres logowania podaje biblioteka uczelni", "po polsku", None)],
}


SEKCJE = {"organiczna": "## Chemia organiczna", "ogólna i nieorganiczna": "## Chemia ogólna i nieorganiczna",
          "fizyczna": "## Chemia fizyczna", "analityczna": "## Chemia analityczna", "biochemia": "## Biochemia",
          "matematyka": "## Matematyka"}


def pozycja(wpis):
    """Miejsce pierwszego wystąpienia w sekcji przedmiotu w rozdziale 3, potem w całym tekście."""
    u = wpis["url"]
    nazw = re.split(r"[,:]", wpis["nazwa"])[0].split()[-1]
    klucze = [u] if "data.bn.org.pl" not in u else []
    klucze.append(nazw)
    sek = SEKCJE.get(wpis["przedmiot"])
    if sek:
        a = r3.find("\n" + sek + "\n")
        b = r3.find("\n## ", a + 5)
        kawalek = r3[a:b if b > 0 else len(r3)]
        for k in klucze:
            i = kawalek.find(k)
            if i >= 0:
                return i
    for k in klucze:
        i = tresc.find(k)
        if i >= 0:
            return 10**6 + i
    return 10**9


wyj5 = ["# Źródła", "",
        "Tu są w jednym miejscu kanały, kursy, strony i książki polecane w rozdziałach 3 i 4, w tej samej kolejności przedmiotów co w rozdziale 3, z adresami do przepisania, gdyby link nie działał albo kurs był czytany na papierze. Artykuły z list „Gdzie czytać dalej” w rozdziale 4 mają adresy w samym tekście. Książki nie mają adresów: szukaj ich po autorze i tytule w katalogu biblioteki. Wszystkie adresy zostały sprawdzone w listopadzie 2026; gdy któryś przestanie działać, wpisz w wyszukiwarkę tytuł albo autora.", ""]
for klucz, tytul in DZIALY:
    w = sorted([x for x in zas if x["przedmiot"] == klucz], key=pozycja)
    if not w and klucz not in DODATKOWE:
        continue
    wyj5 += [f"## {tytul}", ""]
    for x in w:
        jez = "po polsku" if x["jezyk"] == "polski" else "po angielsku"
        opis = NADPISZ.get(x["id"]) or poziom_z_r3.get(x["url"]) or (jez + "; " + MAPA.get(x["poziom"].strip(), x["poziom"].strip()))
        if "data.bn.org.pl" in x["url"]:
            wyj5.append(f"- {x['nazwa']} (książka; {opis})")
        else:
            wyj5.append(f"- {x['nazwa']} ({opis}): <{x['url']}>")
    for nazwa, opis, u in DODATKOWE.get(klucz, []):
        wyj5.append(f"- {nazwa} ({opis})" + (f": <{u}>" if u else ""))
    wyj5.append("")
t = tresc + "\n" + "\n".join(wyj5).rstrip("\n") + "\n"

# ---------- Numery rozdziałów ----------
for stary, nowy in [("# Inna gra", "# 1. Inna gra"), ("# Co z matury zamienia się w co", "# 2. Co z matury zamienia się w co"),
                    ("# Skąd się uczyć", "# 3. Skąd się uczyć"), ("# Rzeczy, które spotka prawie każdy", "# 4. Rzeczy, które spotka prawie każdy"),
                    ("# Źródła", "# 5. Źródła")]:
    r("\n" + stary + "\n", "\n" + nowy + "\n")

open(wyj, "w", encoding="utf-8").write(t)
print("błędy dopasowania:", bledy if bledy else "brak")
print("poziomy z rozdziału 3:", len(poziom_z_r3))
