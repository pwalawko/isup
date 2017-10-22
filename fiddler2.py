import sys
from decimal import Decimal
from collections import OrderedDict


biliard = {
    1: 'biliard',
    2: 'biliardy',
    3: 'biliardy',
    4: 'biliardy',
    5: 'biliardów',
    6: 'biliardów',
    7: 'biliardów',
    8: 'biliardów',
    9: 'biliardów',
    0: 'biliardów'
}

bilion = {
    1: 'bilion',
    2: 'biliony',
    3: 'biliony',
    4: 'biliony',
    5: 'bilionów',
    6: 'bilionów',
    7: 'bilionów',
    8: 'bilionów',
    9: 'bilionów',
    0: 'bilionów'
}

miliard = {
    1: 'miliard',
    2: 'miliardy',
    3: 'miliardy',
    4: 'miliardy',
    5: 'miliardów',
    6: 'miliardów',
    7: 'miliardów',
    8: 'miliardów',
    9: 'miliardów',
    0: 'miliardów'
}


milion = {
    1: 'milion',
    2: 'miliony',
    3: 'miliony',
    4: 'miliony',
    5: 'milionów',
    6: 'milionów',
    7: 'milionów',
    8: 'milionów',
    9: 'milionów',
    0: 'milionów'
}

tysiac = {
    1: 'tysiąc',
    2: 'tysiące',
    3: 'tysiące',
    4: 'tysiące',
    5: 'tysięcy',
    6: 'tysięcy',
    7: 'tysięcy',
    8: 'tysięcy',
    9: 'tysięcy',
    0: 'tysięcy'
}

liczby = OrderedDict([
    (1000000000000000, biliard),
    (1000000000000, bilion),
    (1000000000, miliard),
    (1000000, milion),
    (1000, tysiac)
])

JEDNOSCI = {
    '1': 'jeden',
    '2': 'dwa',
    '3': 'trzy',
    '4': 'cztery',
    '5': 'pięć',
    '6': 'sześć',
    '7': 'siedem',
    '8': 'osiem',
    '9': 'dziewięć'
}
NASTKI = {
    '0': 'dziesięć',
    '1': 'jedenaście',
    '2': 'dwanaście',
    '3': 'trzynaście',
    '4': 'czternaście',
    '5': 'piętnaście',
    '6': 'szesnaście',
    '7': 'siedemnaście',
    '8': 'osiemnaście',
    '9': 'dziewiętnaście'
}
DZIESIATKI = {
    '2': 'dwadzieścia',
    '3': 'trzydzieści',
    '4': 'czterdzieści',
    '5': 'pięćdziesiąt',
    '6': 'sześćdziesiąt',
    '7': 'siedemdziesiąt',
    '8': 'osiemdziesiąt',
    '9': 'dziewięćdziesiąt'
}
SETKI = {
    '1': 'sto',
    '2': 'dwieście',
    '3': 'trzysta',
    '4': 'czterysta',
    '5': 'pięćset',
    '6': 'sześćset',
    '7': 'siedemset',
    '8': 'osiemset',
    '9': 'dziewięćset'
}

SETKI_SLOWNIE = {
    1: 'złoty',
    2: 'złote',
    3: 'złote',
    4: 'złote',
    5: 'złotych',
    6: 'złotych',
    7: 'złotych',
    8: 'złotych',
    9: 'złotych',
    0: 'złotych',
    'nic': ''
}
GROSZE_SLOWNIE = {
    1: 'grosz',
    2: 'grosze',
    3: 'grosze',
    4: 'grosze',
    5: 'groszy',
    6: 'groszy',
    7: 'groszy',
    8: 'groszy',
    9: 'groszy',
    0: 'groszy',
    'nic': ''
}


def podzial_na_trojki(kwota):
    trojki = []
    for liczba, slownik_jednostek in liczby.items():
        ilosc = kwota // liczba
        if ilosc > 0:
            slownie, jednostka = trojki_na_slowa(ilosc)
            trojki.append(slownie)
            jednostka = slownik_jednostek[jednostka] + ' '
            trojki.append(jednostka)
            kwota = kwota - liczba*ilosc
    trojki.append(kwota)
    return trojki


def trojki_na_slowa(kwota):
    # Sprawdzamy ile jest setek.
    setki_trojliczby = kwota // 100
    # Jeśli są, bierzemy ze słownika z setkami wartość
    # odpowiadającą ilości setek.
    if setki_trojliczby >= 1:
        setki_trojliczby_slownie = SETKI[str(setki_trojliczby)] + ' '
    # Jeśli nie ma, zostawiamy setki puste.
    else:
        setki_trojliczby_slownie = ''
    # Sprawdzamy ile jest dziesiątek, odejmując najpierw
    # uwzględnione już wcześniej setki.
    dziesiatki_trojliczby = (kwota - (setki_trojliczby * 100)) // 10
    # Jeśli są, bierzemy ze słownika z dziesiątkami wartość
    # odpowiadającą ilości dziesiątek.
    # Trzeba wziąć pod uwagę, że dla nastek zapis słowny jest inny
    # niż dla dziesiątek większych niż 1.
    jednosci_trojliczby_slownie = ''
    jednostka_ze_slownika = 'nic'
    if dziesiatki_trojliczby == 1:
        dzies_trojliczby_slownie = NASTKI[
            str((kwota - (setki_trojliczby * 100)) % 10)
        ] + ' '
        # Jeśli są nastki, kwota słownie zawsze końcy się tak samo,
        # więc można użyć stałą wartość.
        jednostka_ze_slownika = 5
    # Teraz zapis dla kwóty dziesiątek innej niż nastki.
    elif 2 <= dziesiatki_trojliczby <= 9:
        dzies_trojliczby_slownie = DZIESIATKI[
            str(dziesiatki_trojliczby)
        ] + ' '
        # Jedności są obsłużone w ramach dziesiątek,
        # ponieważ nie będzie ich przy nastkach.
        # Sprawdzamy ilość jedności.
        jednosci_trojliczby = (
            kwota -
            (setki_trojliczby * 100) -
            (dziesiatki_trojliczby * 10)
        ) // 1
        if jednosci_trojliczby > 0:
            jednosci_trojliczby_slownie = str(
                JEDNOSCI[str(jednosci_trojliczby)]
            ) + ' '
        # Czas na zapis słowny jednostek. Będą one pobierane ze słownika,
        # w zaneżności od tego czy funkcja jest zastosowana dla milionów,
        # tysięcy czy setek zł.
        jednostka_ze_slownika = jednosci_trojliczby
        # Trzeba obsłużyć przypadek, gdy liczba kończy się na 1.
        if jednosci_trojliczby == 1:
            jednostka_ze_slownika = 5
    # I zapis dla kwoty gdy nie ma dziesiątek.
    else:
        dzies_trojliczby_slownie = ''
        jednosci_trojliczby = (
            kwota -
            (setki_trojliczby * 100) -
            (dziesiatki_trojliczby * 10)
        ) // 1
        if jednosci_trojliczby == 0:
            if setki_trojliczby == 0:
                jednosci_trojliczby_slownie = ''
            else:
                jednostka_ze_slownika = 5
        elif jednosci_trojliczby == 1:
            jednosci_trojliczby_slownie = str(
                JEDNOSCI[str(jednosci_trojliczby)]
            ) + ' '
            jednostka_ze_slownika = jednosci_trojliczby
            if setki_trojliczby > 0 or dziesiatki_trojliczby > 0:
                jednostka_ze_slownika = 5
        else:
            jednosci_trojliczby_slownie = str(
                JEDNOSCI[str(jednosci_trojliczby)]
            ) + ' '
            jednostka_ze_slownika = jednosci_trojliczby
    # Funkcja zwraca zapis liczy oraz wartość jednostki ze słownika.
    zapis_liczby = (
        setki_trojliczby_slownie +
        dzies_trojliczby_slownie +
        jednosci_trojliczby_slownie
    )
    return zapis_liczby, jednostka_ze_slownika



def fakturowanie(kwota):
    if not isinstance(kwota, Decimal):
        raise TypeError('Nieprawidłowe dane!')
    if kwota // list(liczby.keys())[0] > 999:
        raise ValueError('Zbyt duża wartość!')
    if kwota < 0:
        raise ValueError('Zbyt mała wartość!')
    kwota.quantize(Decimal('.01'))

    trojki = podzial_na_trojki(kwota)

    setki = trojki.pop()

    liczba_setek = setki // 1
    stowy, liczba_setek_slownie = trojki_na_slowa(liczba_setek)
    trojki.append(stowy)
    liczba_setek_slownie = SETKI_SLOWNIE[liczba_setek_slownie]
    if liczba_setek_slownie != '':
        liczba_setek_slownie = liczba_setek_slownie + ' '
    zlote = all((a == '' for a in trojki[:-1]))
    if liczba_setek_slownie == '':
        liczba_setek_slownie = 'zero złotych ' if zlote else 'złotych '
    if (
        (not zlote or liczba_setek > 1) and
        (liczba_setek - (liczba_setek // 10 * 10)) == 1
    ):
        liczba_setek_slownie = 'złotych '
    trojki.append(liczba_setek_slownie)
    setki = (setki - (liczba_setek * 1)) * 100

    liczba_groszy = setki // 1
    grosze, liczba_groszy_slownie = trojki_na_slowa(liczba_groszy)
    trojki.append(grosze)
    liczba_groszy_slownie = GROSZE_SLOWNIE[liczba_groszy_slownie]
    if liczba_groszy_slownie == '':
        liczba_groszy_slownie = 'zero groszy'
    trojki.append(liczba_groszy_slownie)

    kwota_slownie = ''.join(trojki)

    return kwota_slownie


def main():
    try:
        kwota = Decimal(sys.argv[1])
    except ValueError:
        print('Nieprawidłowe dane!')
    except IndexError:
        print('Brakujący parametr!')
    else:
        print(fakturowanie(kwota))


if __name__ == '__main__':
    main()
