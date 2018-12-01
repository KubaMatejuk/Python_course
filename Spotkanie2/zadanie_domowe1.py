def rozmien(portfel, kwota):
    suma_portfel=0
    for i in range(len(portfel)):
        suma_portfel = suma_portfel + i*portfel[i]
    if kwota > suma_portfel:
        print("Nie da się rozmienić - kwota w portfelu jest zbyt mała.")
        return None
    nominal = len(portfel)-1
    ilosc_nominalow = [0]*len(portfel)
    while nominal > 0 and kwota > 0:
        if portfel[nominal] != 0:
            ile_nominalow = kwota // nominal
            if ile_nominalow > portfel[nominal]:
                ile_nominalow = portfel[nominal]
            kwota = kwota - nominal * ile_nominalow
            ilosc_nominalow[nominal] = ile_nominalow
        nominal = nominal-1
    if kwota > 0:
        for i in range(len(ilosc_nominalow)):
            if ilosc_nominalow[i] < portfel[i]:
                ilosc_nominalow[i] = ilosc_nominalow[i] + 1
                break
    return ilosc_nominalow


portfel = [0, 20, 2, 0, 0, 10]
kwota = 58
ilosc_nominalow = rozmien(portfel,kwota)
if ilosc_nominalow != None:
    for i in range(len(ilosc_nominalow)):
        if ilosc_nominalow[i] != 0:
            print("nominał {0}zł: {1:>3}".format(i, ilosc_nominalow[i]))







