def podatek(kwota):
    if kwota <= 44490:
        podatek = kwota * 0.19
    elif kwota <= 85528:
        podatek = 44490 * 0.19 + (kwota-44490)*0.3
    else:
        podatek = 44490 * 0.19 + (85528-44490)*0.3 + (kwota - 85528)*0.4
    return podatek

print("Podatek do zapłaty wynosi {0}.".format(podatek(100000)))

def podatek2(kwota):
    if kwota <= 44490:
        podatek = kwota * 0.19
    elif kwota <= 85528:
        podatek = (kwota-44490)*0.3 + podatek2(44490)
    else:
        podatek = (kwota-85528)*0.4 + podatek2(85528)
    return podatek

print("Podatek do zapłaty wynosi {0}.".format(podatek2(100000)))

print(podatek2(50000))