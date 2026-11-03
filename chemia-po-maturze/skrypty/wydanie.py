"""Składa wydanie do czytania: wydanie/chemia-po-maturze.md (bez komentarzy HTML ze źródłami),
wydanie/chemia-po-maturze.html (podgląd, pandoc). PDF robi skrypty/pdf.js.
Użycie: python3 -I skrypty/wydanie.py"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wspolne import KORZEN, pliki_tresci  # noqa: E402

WYD = os.path.join(KORZEN, "wydanie")
CSS = """
body{font-family:Georgia,'Times New Roman',serif;max-width:46rem;margin:2rem auto;padding:0 1rem;line-height:1.6;color:#1d1d1d;background:#fff}
h1{font-size:1.9rem;margin-top:3rem;border-bottom:2px solid #333;padding-bottom:.3rem} h1.title{border:none;margin-top:0} h2{margin-top:2.2rem} h3{margin-top:1.6rem}
table{border-collapse:collapse;font-size:.9rem;margin:1rem 0} th,td{border:1px solid #bbb;padding:.35rem .5rem;vertical-align:top}
p.rysunek{border:1px dashed #999;background:#f6f6f6;padding:.6rem .8rem;font-size:.9rem;color:#444}
li{margin:.3rem 0} @media print{h1:not(.title){page-break-before:always} body{max-width:none;margin:0}}
"""


def main():
    os.makedirs(WYD, exist_ok=True)
    czesci = []
    for p in pliki_tresci():
        nazwa = os.path.basename(p)
        t = open(p, encoding="utf-8").read()
        t = re.sub(r"[ \t]*<!--.*?-->", "", t, flags=re.S)
        t = re.sub(r"\n{3,}", "\n\n", t).strip()
        if nazwa.startswith("04a"):
            czesci += ["# Rzeczy, które spotka prawie każdy", "",
                       "Cztery krótkie wprowadzenia: aktywność, chemia kwantowa, spektroskopia i laboratorium. "
                       "Każde mówi, czym to jest, dlaczego to spotkasz i skąd uczyć się dalej.", ""]
        elif not nazwa.startswith("04"):
            t = re.sub(r"^## ", "# ", t, count=1)
        czesci += [t, ""]
    md = "\n".join(czesci)
    sciezka_md = os.path.join(WYD, "chemia-po-maturze.md")
    open(sciezka_md, "w", encoding="utf-8").write(md)
    css = os.path.join(WYD, "styl-podgladu.css")
    open(css, "w", encoding="utf-8").write(CSS)
    html = subprocess.run(["pandoc", "-f", "markdown", "-t", "html5", "--standalone", "--toc", "--toc-depth=2",
                           "--metadata", "title=Chemia po maturze", "--metadata", "lang=pl",
                           "--metadata", "subtitle=Bonus do kursu KaNaU 50/70/90 · stan zasobów i sylabusów: listopad 2026",
                           "--css", "styl-podgladu.css", sciezka_md], capture_output=True, text=True, check=True).stdout
    html = re.sub(r"<p>(\[RYSUNEK: [^<]*)</p>", r'<p class="rysunek">\1</p>', html)
    open(os.path.join(WYD, "chemia-po-maturze.html"), "w", encoding="utf-8").write(html)
    print(len(md), "znaków")


if __name__ == "__main__":
    main()
