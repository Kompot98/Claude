"""Długość rozdziałów w znakach i stronach znormalizowanych (1800 znaków ze spacjami), bez komentarzy HTML."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wspolne import pliki_tresci, bez_komentarzy  # noqa: E402


def main():
    razem = 0
    print("| Rozdział | Znaki | Strony |")
    print("|---|---|---|")
    for s in pliki_tresci():
        with open(s, encoding="utf-8") as f:
            n = len(bez_komentarzy(f.read()))
        razem += n
        print(f"| {os.path.basename(s)} | {n} | {f'{n / 1800:.1f}'.replace('.', ',')} |")
    print(f"| razem | {razem} | {f'{razem / 1800:.1f}'.replace('.', ',')} |")


if __name__ == "__main__":
    main()
