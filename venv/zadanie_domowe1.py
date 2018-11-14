def bmi(masa, wzrost):
    return round(masa/(wzrost*wzrost),2)

def komentarz(bmi):
    if bmi <16:
        tekst = "wygłodzenie"
    elif bmi <17:
        tekst = "wychudzenie"
    elif bmi < 18.5:
        tekst = "niedowaga"
    elif bmi < 25:
        tekst = "wartość prawidłowa"
    elif bmi < 30:
        tekst = "nadwaga"
    elif bmi < 35:
        tekst = "I stopień otyłości"
    elif bmi < 40:
        tekst = "II stopień otyłości"
    else:
        tekst = "III stopień otyłości(otyłość skrajna)"
    return tekst

waga=85
wzrost_w_metrach = 1.76
print("Twoje BMI wynosi {0} i oznacza: {1}".format(bmi(waga,wzrost_w_metrach),komentarz(bmi(waga,wzrost_w_metrach))))
