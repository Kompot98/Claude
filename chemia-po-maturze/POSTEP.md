# Dziennik postępu

Każdy etap kończy się wpisem: co zrobione, stan sprawdzeń, co dalej.

## 2026-11-03, etap 0: szkielet i skrypty

Zrobione: układ folderów ze zlecenia, kopie zlecenia i kontekstu w `zlecenie/`, nagłówki trzech rejestrów CSV, puste rozdziały. Skrypty w `skrypty/`: `sprawdz.py` (spójność odwołań, słowniki wartości, licencje rysunków, linki do stron głównych kanałów, pliki dowodów, lista znaczników), `styl.py` (zasady głosu, pojęcia akademickie bez wyjaśnienia), `linki.py` (czy adresy odpowiadają), `dlugosc.py` (strony znormalizowane). Skrypty sprawdzone na kopii z wstrzykniętymi błędami: wykryły wszystkie osiem błędów spójności i trzy naruszenia stylu.

Ograniczenie środowiska wykryte przy starcie: YouTube podaje listę filmów w playliście (tytuły, długości), ale nie podaje opisów pojedynczych filmów ani transkrypcji (wymaga logowania). Serwis sylabusów Uniwersytetu Medycznego w Łodzi jest niedostępny z sieci tego środowiska.

Dalej: pilotaż, rozdział 3 dla chemii organicznej.

## 2026-11-03, etap 1: pilotaż, chemia organiczna w rozdziale 3

Zrobione: 19 zasobów (R-001 do R-019): 4 polskie materiały uczelni (wykłady UŚ, dwie playlisty z pracowni UŚ, nazewnictwo PW), 2 polskie podręczniki z katalogu BN, 5 playlist i kurs MIT, 5 stron, 3 podręczniki angielskie (dwa otwarte). Każdy ma plik dowodu. Lista kandydatów z 14 odrzuconymi lub odłożonymi w `robocze/kandydaci-organiczna.md`. Drugi przegląd zrobiony (`robocze/przeglad2-organiczna.md`), trzy rozbieżności w `ROZBIEZNOSCI.md`, poprawione. Sprawdzenia: `sprawdz.py --dowody` 0 błędów, `styl.py` 0 twardych naruszeń, `linki.py` 18/18 odpowiada (R-019 dodany później). Sekcja ma 4,7 strony.

Ustalenia pilotażu: format zapisany w D-06. Licencja OpenStax to w 2026 CC BY-NC-SA (D-05), więc rysunki tylko z Wikimedia Commons. Khan Academy odkłada automaty, do ponownej próby.

Dalej: pilotaż B, wprowadzenie o spektroskopii (04c).

## 2026-11-03, etap 2: pilotaż, wprowadzenie o spektroskopii (04c)

Zrobione: przeczytane w całości OpenStax Organic Chemistry 12.1, 12.5–12.8, 13.1–13.3, 13.5–13.6, ramka o MRI, 14.7–14.8 oraz Harvey „Analytical Chemistry 2.1” 10.1–10.2; teksty w `zrodla/lektury/`. Napisane 04c (4,8 strony, decyzja D-10) z komentarzami źródłowymi przy zdaniach merytorycznych; dwa źródła cytowane Z-001, Z-002. Sześć nowych zasobów (R-020 do R-025): książka LibreTexts o spektroskopii, NIST WebBook, SDBS, dwa polskie podręczniki z katalogu BN, playlista analityczna UŚ. Zostały trzy miejsca `[SPRAWDZIĆ]` (sylabusy, krzywa wzorcowa, „prowadzący odsyłają”) i trzy `[RYSUNEK]`. Sprawdzenia: `sprawdz.py --dowody` 0 błędów, `styl.py` 0 twardych naruszeń (poprawiony, żeby nie mylił zapisu wiązania O–H z myślnikiem).

Wniosek z pilotażu: format opisu zasobu i rejestr działają, komentarze źródłowe na poziomie „podrozdział, akapit” wystarczają. Drugi przegląd zasobów R-020 do R-025 zrobię razem z zasobami etapu 3.

Dalej: rozdział 3 dla pozostałych przedmiotów.

## 2026-11-03, etap 3: rozdział 3 dla pozostałych przedmiotów

Zrobione: sekcje chemii ogólnej i nieorganicznej, fizycznej, analitycznej, biochemii i hasło o matematyce; dopisany drugi polski cykl wykładów z organicznej (SGGW). Rejestr ma 58 zasobów, każdy z plikiem dowodu. Drugi przegląd R-020 do R-058 zrobiony (`robocze/przeglad2-reszta.md`), trzy drobne rozbieżności w `ROZBIEZNOSCI.md`. Kandydaci odrzuceni w `robocze/kandydaci-reszta.md` (18 pozycji). Rozdział 3 ma około 11,6 strony bez odgałęzień dla kierunków. R-055 (techniki laboratoryjne) czeka na cytowanie w 4d.

Ograniczenia: Khan Academy, Chemistry World, Education in Chemistry, Compound Interest i PubChem (strona) blokują automaty. Artykuły popularnonaukowe z obietnicy kursu („książki, kanały, artykuły”) są więc reprezentowane tylko przez serwisy z artykułami objaśniającymi (Master Organic Chemistry, Chemguide, Chemistry Steps, LibreTexts). Pytanie do zleceniodawcy w raporcie.

Dalej: sylabusy (etap 4).

## 2026-11-03, etap 4: sylabusy

Zrobione: 22 źródła (Z-003 do Z-024) dla ośmiu kierunków, kopie tekstowe w `zrodla/`, tabela zbiorcza i lista braków w `robocze/sylabusy-tabela.md`. Najciekawsze ustalenia do rozdziału 2: na kierunku lekarskim WUM i na stomatologii UJ CM pierwszy rok nie ma przedmiotu chemicznego, a w UMB chemia i biochemia są na pierwszym roku; na analityce medycznej WUM pierwszy rok ma cztery przedmioty chemiczne; „Chemia ogólna i nieorganiczna” na PP ma inny wymiar na technologii chemicznej (45+30 h, 7 ECTS) i na inżynierii chemicznej i procesowej (30+30 h, 5 ECTS); w tym przedmiocie już w pierwszym semestrze jest „stężenie a aktywność”.

Dalej: rozdział 2 i odgałęzienia w rozdziale 3.

## 2026-11-03, etap 5: rozdział 2 i odgałęzienia w rozdziale 3

Zrobione: rozdział 2 (5,1 strony z tabelą 19 wierszy dla 20 modułów; obie części modułu XI w jednym wierszu): mapa modułów kursu na przedmioty pierwszego roku z odwołaniami do sylabusów, cztery tematy zupełnie nowe z odesłaniem do rozdziału 4, trzy porównania „ta sama nazwa, inna treść” (PP technologia vs inżynieria; chemia ogólna i nieorganiczna na farmacji, analityce i biotechnologii; chemia na kierunku lekarskim WUM, UMB i UJ CM). Odgałęzienia dla sześciu grup kierunków na końcu rozdziału 3. Uzupełnione z sylabusów miejsca `[SPRAWDZIĆ]` w rozdziałach 3 i 4c; zostały dwa (wiersze organiczne w mapie, procedura krzywej wzorcowej). Wszystkie 24 źródła są cytowane. Rozdział 3 ma 14,1 strony.

Dalej: rozdziały 1 i 0.

## 2026-11-03, etap 6: rozdziały 1 i 0, wstęp do rozdziału 3

Zrobione: rozdział 1 (4,1 strony) z punktami 1–7 Adriana dosłownie i dodatkami bezosobowymi (jak czytać sylabus na przykładzie karty UM w Łodzi, legalne drogi do książek na przykładzie poradnika UWr o IBUK Libra, czytanie podręcznika wybiórczo). Wstęp (1,5 strony) ze zdaniem o „ścianie” i mapą czytania. Wstęp do rozdziału 3 z punktem 8. Lista kontrolna punktów Adriana w `robocze/adrian-punkty.md`. Nowe źródło Z-025.

Dalej: wprowadzenia 4a, 4b, 4d.

## 2026-11-03, etap 7: wprowadzenia 4a, 4b, 4d

Zrobione: 4a aktywność (Harvey 6.9, Peverati 14.1, OpenStax 13.2; przykład z Fe(SCN)²⁺ i rozpuszczalnością Pb(IO₃)₂), 4b chemia kwantowa (OpenStax 6.3 i 8.4; sylabusy UJ, UW, WUM; Piela: wydanie polskie 2011 z BN, angielskie 3. z 2020 ze strony wydawcy i Open Library), 4d laboratorium (sylabusy UM Łódź, UKSW, UR; Sandtorv 1.2, 1.4, 6.1). Każde ma komentarze źródłowe przy zdaniach merytorycznych. Nowe źródła Z-026 do Z-032, nowe zasoby R-059 do R-061. Wszystkie 61 zasobów i 32 źródła są cytowane; `sprawdz.py --dowody` bez błędów. Całość ma 39 stron.

Dalej: rysunki, rozdział 5, weryfikacja całości, raport.

## 2026-11-03, etap 8: rysunki, rozdział 5, weryfikacja

Zrobione: rozdział 5 generowany skryptem (61 zasobów, 32 źródła, każda pozycja przy rozdziale pierwszego cytowania). Rysunków nie dodano (D-13). Weryfikacja: `sprawdz.py --dowody` bez błędów, `styl.py` bez twardych naruszeń, wszystkie 93 adresy odpowiadają, drugi przegląd R-059 do R-061 zgodny, pojęcia akademickie wyjaśnione przy pierwszym użyciu w kolejności czytania (pozostałe sygnały skryptu to fałszywe alarmy opisane w raporcie). Usunięte cztery przysłówki w stopniu najwyższym bez podstawy.

Dalej: raport, README, archiwum.

## 2026-11-03, etap 9: raport, README, archiwum

Zrobione: `RAPORT.md` (rozdziały z długością, 29 odrzuconych lub odłożonych zasobów, tabela sylabusów z brakami, 17 znaczników do uzupełnienia, pięć pytań z rekomendacją), `README.md` folderu, archiwum `chemia-po-maturze.zip` obok folderu. Wszystkie sprawdzenia przechodzą.
