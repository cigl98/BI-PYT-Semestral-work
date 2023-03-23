**Grafický editor**


Implementovány jsou následující operace s příslušnými přepínači:

* převrácení obrazu směrem doprava o 90°; --rotate
* zrcadlení; --mirror
* inverzní obraz (negativ); --inverse
* převod do odstínů šedi; --bw
* zesvětlení; --lighten <percentage: 0-100>
* ztmavení; --darken <percentage: 0-100>
* zvýraznění hran (tzv. “unsharp mask”); --sharpen

Použití:
python app/Main.py [-options] infile outfile

infile - cesta ke vstupnímu obrázku

outfile - cesta pro výstupní soubor
