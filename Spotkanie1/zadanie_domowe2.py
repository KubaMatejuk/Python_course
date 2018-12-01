def wyplata(kwota):
    nominaly = [20,10,5,2,1]
    print("Kwota do wypłaty: {0}".format(kwota))
    for i in range(len(nominaly)):
        ile_nominalow = kwota // nominaly[i]
        kwota=kwota % nominaly[i]
        if ile_nominalow != 0:
            print("nominał {0:<2}: {1:>3}".format(nominaly[i],ile_nominalow))

wyplata(123)
wyplata(4878)