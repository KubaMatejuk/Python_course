from Spotkanie3 import vat


def zakupy(cennik, lista):
    ceny_netto = []
    for produkt in lista:
        if produkt in cennik:
            ceny_netto.append(lista[produkt] * cennik[produkt])
    return ceny_netto

def suma_brutto(cennik, lista):
    cena_netto = zakupy(cennik,lista)
    suma_netto = 0
    for i in range(len(lista)):
        suma_netto += cena_netto[i]
    podatek = vat.vat_paragon(cena_netto)
    return suma_netto + podatek




cennik = {
    'kawa' : 14.99,
    'pomarancze' : 3.49,
    'olej' : 4.99
    }
lista = {'olej': 2, 'kawa' : 1}

print(suma_brutto(cennik,lista))