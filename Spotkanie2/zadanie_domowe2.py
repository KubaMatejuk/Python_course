import random


def gra():
    liczba_zapalek=random.randint(7, 36)
    print("Rozpoczynamy grę! Komputer wylosował pewną ilość zapałek. Po kolei Ty i komputer zabieracie zapałki. W ruchu możesz wziąć od 1 do 3 zapałek. Przegrywa ten, kto weźmie ostatnią zapałkę. Ty zaczynasz. Przegrywa ten, kto weźmie ostatni zapałkę.")
    liczba_zapalek=liczba_zapalek-ile_zapalek(liczba_zapalek, 0)
    while liczba_zapalek > 1:
        for i in range(1, 4):
            if (liczba_zapalek - i) % 4 == 1:
                liczba_zapalek = liczba_zapalek - i
                break
            if i == 3:
                i = 1
                liczba_zapalek = liczba_zapalek - i
                break
        liczba_zapalek = liczba_zapalek - ile_zapalek(liczba_zapalek, i)
    if liczba_zapalek == 1:
        print("\nWziąłem ostatnią zapałkę. Przegrałem i gratuluję!")
    else:
        print("\nWziąłeś ostatnią zapałkę. Wygrałem!")
    input("Naciśnij Enter aby kontynuować...")


def ile_zapalek(ile_jest_zapałek, ile_wzial_komputer):
    if ile_wzial_komputer == 1:
        print("\nWziąłem {0} zapałkę.".format(ile_wzial_komputer))
    if ile_wzial_komputer > 1:
        print("\nWziąłem {0} zapałki.".format(ile_wzial_komputer))
    print("W tym momencie jest {0} zapałek.".format(ile_jest_zapałek))
    we = 0
    while we <= 0 or we > 3 or we > ile_jest_zapałek:
        we = int(input("Ile zapałek bierzesz? "))
        if we <= 0 or we > 3:
            print("Możesz wziąć od jednej do trzech zapałek!")
        if we > ile_jest_zapałek:
            print("Nie możesz wziąć więcej zapałek niż jest!")
    return we


gra()
