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
