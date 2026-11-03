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
