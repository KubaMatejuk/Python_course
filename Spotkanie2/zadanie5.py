def suma_dzielnikow(n):
    suma = []
    for i in range(1, n):
        if n % i == 0:
            suma.append(i)
    return suma


def czy_pierwsza(n):
    if len(suma_dzielnikow(n)) == 1:
        return True
    return False


def dzielniki_pierwsze(n):
    dziel_pierwsze=[]
    for element in suma_dzielnikow(n):
        if czy_pierwsza(element):
            dziel_pierwsze.append(element)
    return dziel_pierwsze

print(dzielniki_pierwsze(24))

def czy_doskonala(n):
    suma=0
    for i in suma_dzielnikow(n):
        suma=suma+i
    if suma==n:
        return True
    return False

print(czy_doskonala(6))

def liczby_doskonale():
    lic_dosk=[]
    i=1
    while len(lic_dosk)<4:
        if czy_doskonala(i):
            lic_dosk.append(i)
        i=i+1
    return lic_dosk

print(liczby_doskonale())