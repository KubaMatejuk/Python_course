class NotPositiveValueError(Exception):
    pass

def odsetki(oproc,czas,kwota):
    if kwota <0 or czas < 0 or oproc<0:
        raise NotPositiveValueError
    return kwota*(oproc/100)*(czas/12)

kwota=1000
oprocentowanie=3

print("Kwota = {0}zł, oprocentowanie {1}%.".format(kwota,oprocentowanie))
print("Odsetki przy lokacie rocznej: {0}".format(odsetki(oprocentowanie,12,kwota)))

kapital=kwota
for i in range(4):
    kapital=kapital+odsetki(oprocentowanie,3, kapital)

print("Odsetki przy lokacie odnawianej co 3 miesiące: {0}".format(kapital-kwota))

print(odsetki(3,-5,2000))