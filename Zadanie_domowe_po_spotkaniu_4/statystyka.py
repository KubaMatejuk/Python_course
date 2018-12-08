import urllib

def statystyka(adres):
    slownik = {}
    with urllib.request.urlopen(adres) as response:
        html = response.read()
    slowa = html.split()
    for slowo in slowa:
        if slowo not in slownik.keys():
            slownik[slowo] = 1
        else:
            slownik[slowo] += 1
    return slownik


print(statystyka('https://wolnelektury.pl/media/book/txt/konopnicka-miraze.txt'))
