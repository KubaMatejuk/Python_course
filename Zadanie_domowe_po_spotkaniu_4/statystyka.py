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


def porownanie(adres1, adres2):
    slownik1 = statystyka(adres1)
    slownik2 = statystyka(adres2)
    powtarzajace = {}
    tylko_adres1 = []
    tylko_adres2 = []
    for slowo in slownik1:
        if slowo in slownik2.keys():
            powtarzajace[slowo] = max(slownik1[slowo],slownik2[slowo])-min(slownik1[slowo],slownik2[slowo])
        else:
            tylko_adres1.append(slowo)
    for slowo in slownik2:
        if slowo not in slownik1.keys():
            tylko_adres2.append(slowo)
    print("Powtarzające się słowa i rożnice w ilości występowań: {0}".format(powtarzajace))
    print("Słowa występujące tylko w adresie 1: {0}".format(tylko_adres1))
    print("Słowa występujące tylko w adresie 2: {0}".format(tylko_adres2))


print(statystyka('https://wolnelektury.pl/media/book/txt/konopnicka-miraze.txt'))
porownanie('https://wolnelektury.pl/media/book/txt/konopnicka-miraze.txt', 'https://wolnelektury.pl/media/book/txt/grzebalski-widoki.txt')
