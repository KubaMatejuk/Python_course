import random

def strategiaa(stan_gry):
    """To jest prosta strategia"""
    ruch = min(random.randint(1,3), stan_gry)
    return ruch

def strategia2(stan_gry):
    ruch = min(3, stan_gry)
    return ruch
