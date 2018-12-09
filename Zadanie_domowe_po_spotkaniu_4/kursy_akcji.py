import re

def wartosc_akcji(akcje, nazwa_pliku):
    wartosc = 0
    with open(nazwa_pliku, 'r') as fh:
        tekst = fh.read()
    p = re.compile(r'\n')
    linie = p.split(tekst)
    for linia in linie:
        linia_lista = linia.split(",")
        if linia_lista[0] in akcje.keys():
            wartosc += float(linia_lista[1]) * akcje[linia_lista[0]]
    return wartosc


akcje = {"Agora SA": 10, "Archicom SA" : 10}
print(wartosc_akcji(akcje,".\\raport.csv"))
