from Spotkanie2 import komputer

stan_gry = 10

gracz = 0

def ruch_gracza(stan_gry):
    print("Na stole jest {0} zapałek.".format(stan_gry))
    ruch = int(input("Podaj liczbę zapałek"))
    return ruch


print("Zaczynamy. Jest {0} zapałek.".format(stan_gry))
while stan_gry > 0:
    if gracz == 0:
        ruch = komputer.strategiaa(stan_gry)
    else:
        ruch = komputer.strategia2(stan_gry)
    stan_gry = stan_gry - ruch
    print("Wzięto {0} zapałek. Zostało {1}".format(ruch, stan_gry))
    gracz = 1 - gracz
