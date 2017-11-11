import sys
from decimal import Decimal


BILLIARDS = {
    0: 'biliard ',
    1: 'biliardy ',
    2: 'biliardów ',
}

TRILLIONS = {
    0: 'bilion ',
    1: 'biliony ',
    2: 'bilionów ',
}

BILLIONS = {
    0: 'miliard ',
    1: 'miliardy ',
    2: 'miliardów ',
}


MILLIONS = {
    0: 'milion ',
    1: 'miliony ',
    2: 'milionów ',
}

THOUSANDS = {
    0: 'tysiąc ',
    1: 'tysiące ',
    2: 'tysięcy ',
}

UNITIES = {
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
TEENS = {
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
DOZENS = {
    '2': 'dwadzieścia',
    '3': 'trzydzieści',
    '4': 'czterdzieści',
    '5': 'pięćdziesiąt',
    '6': 'sześćdziesiąt',
    '7': 'siedemdziesiąt',
    '8': 'osiemdziesiąt',
    '9': 'dziewięćdziesiąt'
}
HUNDREDS = {
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

HUNDREDS_WORDS = {
    0: 'złoty',
    1: 'złote',
    2: 'złotych'
}
GROSZE_WORDS = {
    0: 'grosz',
    1: 'grosze',
    2: 'groszy'
}

ORDERS = [THOUSANDS, MILLIONS, BILLIONS, TRILLIONS, BILLIARDS]


def split_amount(amount):
    threes = []
    while amount // 1000 > 0:
        three = amount % 1000
        threes.append(three)
        amount = amount // 1000
    threes.append(amount)
    return threes


def plural_form(n):
    plural = 0
    if n == 1:
        plural = 0
    else:
        if n%10 >= 2 and n%10 <= 4 and (n%100 < 10 or n%100 >= 20):
            plural = 1
        else:
            plural = 2

    return plural


def form_part(amount):
    # Sprawdzamy ile jest setek.
    setki_trojliczby = amount // 100
    # Jeśli są, bierzemy ze słownika z setkami wartość
    # odpowiadającą ilości setek.
    if setki_trojliczby >= 1:
        setki_trojliczby_slownie = HUNDREDS[str(setki_trojliczby)] + ' '
    # Jeśli nie ma, zostawiamy setki puste.
    else:
        setki_trojliczby_slownie = ''
    # Sprawdzamy ile jest dziesiątek, odejmując najpierw
    # uwzględnione już wcześniej setki.
    dziesiatki_trojliczby = (amount - (setki_trojliczby * 100)) // 10
    # Jeśli są, bierzemy ze słownika z dziesiątkami wartość
    # odpowiadającą ilości dziesiątek.
    # Trzeba wziąć pod uwagę, że dla nastek zapis słowny jest inny
    # niż dla dziesiątek większych niż 1.
    jednosci_trojliczby_slownie = ''
    if dziesiatki_trojliczby == 1:
        dzies_trojliczby_slownie = TEENS[
            str((amount - (setki_trojliczby * 100)) % 10)
        ] + ' '
    # Teraz zapis dla kwóty dziesiątek innej niż nastki.
    elif 2 <= dziesiatki_trojliczby <= 9:
        dzies_trojliczby_slownie = DOZENS[
            str(dziesiatki_trojliczby)
        ] + ' '
        # Jedności są obsłużone w ramach dziesiątek,
        # ponieważ nie będzie ich przy nastkach.
        # Sprawdzamy ilość jedności.
        jednosci_trojliczby = (
            amount -
            (setki_trojliczby * 100) -
            (dziesiatki_trojliczby * 10)
        ) // 1
        if jednosci_trojliczby > 0:
            jednosci_trojliczby_slownie = str(
                UNITIES[str(jednosci_trojliczby)]
            ) + ' '
    # I zapis dla kwoty gdy nie ma dziesiątek.
    else:
        dzies_trojliczby_slownie = ''
        jednosci_trojliczby = (
            amount -
            (setki_trojliczby * 100) -
            (dziesiatki_trojliczby * 10)
        ) // 1
        if jednosci_trojliczby == 0:
            if setki_trojliczby == 0:
                jednosci_trojliczby_slownie = ''
        elif jednosci_trojliczby == 1:
            jednosci_trojliczby_slownie = str(
                UNITIES[str(jednosci_trojliczby)]
            ) + ' '
        else:
            jednosci_trojliczby_slownie = str(
                UNITIES[str(jednosci_trojliczby)]
            ) + ' '
    # Funkcja zwraca zapis liczy oraz wartość jednostki ze słownika.
    zapis_liczby = (
        setki_trojliczby_slownie +
        dzies_trojliczby_slownie +
        jednosci_trojliczby_slownie
    )

    plural_amount = plural_form(amount)

    return zapis_liczby, plural_amount


def fakturowanie(amount):
    if not isinstance(amount, Decimal):
        raise TypeError('Nieprawidłowe dane!')
    if amount // 1000**len(ORDERS) > 999:
        raise ValueError('Zbyt duża wartość!')
    if amount < 0:
        raise ValueError('Zbyt mała wartość!')
    amount.quantize(Decimal('.01'))

    threes = split_amount(amount)

    setki = threes.pop(0)

    formed_amount = []
    zipped_amount = list(zip(threes, ORDERS))[::-1]
    for part, order in zipped_amount:
        if part == 0:
            continue
        formed_part, unit = form_part(part)
        unit = order[unit]
        formed_amount.append(formed_part)
        formed_amount.append(unit)

    liczba_setek = setki // 1
    stowy, liczba_setek_slownie = form_part(liczba_setek)
    formed_amount.append(stowy)
    liczba_setek_slownie = HUNDREDS_WORDS[liczba_setek_slownie]
    if liczba_setek_slownie != '':
        liczba_setek_slownie = liczba_setek_slownie + ' '
    zlote = all((a == '' for a in formed_amount[:-1]))
    if liczba_setek == 0:
        liczba_setek_slownie = 'zero złotych ' if zlote else 'złotych '
    if (
        (not zlote or liczba_setek > 1) and
        (liczba_setek - (liczba_setek // 10 * 10)) == 1
    ):
        liczba_setek_slownie = 'złotych '
    formed_amount.append(liczba_setek_slownie)
    setki = (setki - (liczba_setek * 1)) * 100

    liczba_groszy = setki // 1
    grosze, liczba_groszy_slownie = form_part(liczba_groszy)
    formed_amount.append(grosze)
    liczba_groszy_slownie = GROSZE_WORDS[liczba_groszy_slownie]
    if liczba_groszy == 0:
        liczba_groszy_slownie = 'zero groszy'
    formed_amount.append(liczba_groszy_slownie)

    kwota_slownie = ''.join(formed_amount)

    return kwota_slownie


def main():
    try:
        amount = Decimal(sys.argv[1])
    except ValueError:
        print('Nieprawidłowe dane!')
    except IndexError:
        print('Brakujący parametr!')
    else:
        print(fakturowanie(amount))


if __name__ == '__main__':
    main()
