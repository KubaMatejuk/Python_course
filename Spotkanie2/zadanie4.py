def suma_dzielnikow(n):
    suma=[]
    for i in range(1,n):
        if n%i==0:
            suma.append(i)
    return suma


def czy_pierwsza(n):
    if len(suma_dzielnikow(n))==1:
        return True
    return False

dane = [2,3,4,5,6,7,8,9,10,11]
# for liczba in dane:
#     print("{0}: {1}".format(liczba,czy_pierwsza(liczba)))

