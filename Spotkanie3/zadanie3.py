import re

def statystyka(nazwa_pliku):
    with open(nazwa_pliku, 'r') as fh:
        tekst = fh.read()
        p = re.compile(r'\.|\?|\!')
        zdania = p.split(tekst)
        if zdania[-1] == '':
            del(zdania[-1])
        slowa = tekst.split()
        print('Ilość znaków w pliku:  {0}'.format(len(tekst)))
        print('Ilość słów w pliku:  {0}'.format(len(slowa)))
        print('Ilość zdań w pliku:  {0}'.format(len(zdania)))


statystyka('.\\test.txt')
