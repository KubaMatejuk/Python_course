class NotStringError(Exception):
    pass

import bmi
class Osoba:

    def __init__(self, imie, nazwisko, waga, wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.waga = waga
        self.wzrost = wzrost
        if type(imie) != type("kot"):
            raise NotStringError

    def __str__(self):
        return str(self.__class__.__name__) + ": " + self.imie + " " + self.nazwisko

    def bmi(self):
        return bmi.bmi(self.waga, self.wzrost)

class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja, waga, wzrost):
        Osoba.__init__(self, imie, nazwisko, waga, wzrost)
        self.pensja = pensja

    def wyplata(self):
        return self.pensja * 1.2


class Kierownik(Pracownik):
    """
    def __init__(self, imie, nazwisko, pensja):
        Pracownik.__init__(self, imie, nazwisko, pensja)
    """

    def wyplata(self):
        return super().wyplata() + 1200.0



o = Osoba("Jan",  "Kowalski", 100, 2)
print(o)

p = Pracownik("Jan", "Nowak", 2250, 100, 2)

print("{0} wypłata {1}".format(p, p.wyplata()))

k = Kierownik("Anna", "Kowalska", 5000, 100,2)
print(k.wyplata())
print(k)
print(k.bmi())

tester = Osoba(5,"Tester", 55,1.76)