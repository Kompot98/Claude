# Rozbieżności z drugiego przeglądu

Zapis różnic między pierwszym opisem zasobu a tym, co pokazało ponowne otwarcie adresu. Szczegóły w `robocze/przeglad2-*.md`.

## Chemia organiczna (2026-11-03)

- R-007: na końcu playlisty są filmy w formie egzaminów („Can You Pass My … Exam?”), o których opis milczał. Poprawione w opisie.
- R-017: przy ponownym otwarciu przez przeglądarkę serwer LibreTexts zablokował zapytanie (CloudFront), zwykłe zapytanie HTTP przeszło. Treść bez zmian; dopisane w `uwagi`, że dostęp z automatów bywa blokowany. Dla ucznia w zwykłej przeglądarce to nie powinno mieć znaczenia, ale warto sprawdzić ręcznie przy wydaniu.
- R-018: strona wydawcy OUP odpowiada automatom różnie (403, 202, 200). Dane wydania potwierdzone raz przez agenta pobierającego strony; przy wydaniu sprawdzić ręcznie.

## R-020 do R-058 (2026-11-03)

- R-027 (Khan Academy po polsku): przy drugim odczycie serwis pokazał automatowi test antybotowy. Opis opiera się na pierwszym odczycie przez Chromium (lista 20 działów). Przy wydaniu otworzyć ręcznie.
- R-031: ostatni film playlisty to egzamin z chemii organicznej, nie zadanie z chemii ogólnej. Bez znaczenia dla opisu; dopisane w `uwagi`.
- R-033: kolejność filmów na początku i na końcu playlisty różni się od pierwszego odczytu (autor przestawia playlistę). Liczba filmów ta sama (316); opis nie podaje numerów pozycji, więc zostaje.

## R-059 do R-061 (2026-11-03, przy weryfikacji końcowej)

Bez rozbieżności: rekord BN Pieli (PWN 2011), strona Elsevier (3rd Edition, 11.01.2020, rozdziały 1–8 tomu 1) i strona książki Sandtorva w LibreTexts odpowiadają opisom.

## Weryfikacja adresów (2026-11-03)

Wszystkie 61 zasobów i 32 źródła odpowiadają (wynik w `robocze/linki-2026-11-03-pelne.csv`). Cztery adresy (sylabusy UJ i SGGW, USOS UW) wymagały pakietu CA z certyfikatami pośrednimi albo ponowienia po zerwanym połączeniu; pakiet w `robocze/ca-z-certyfikatami-posrednimi.pem`.
