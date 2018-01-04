import sys
from decimal import Decimal


BILLIARDS = ('biliard ', 'biliardy ', 'biliardów ')
TRILLIONS = ('bilion ', 'biliony ', 'bilionów ')
BILLIONS = ('miliard ', 'miliardy ', 'miliardów ')
MILLIONS = ('milion ', 'miliony ', 'milionów ')
THOUSANDS = ('tysiąc ', 'tysiące ', 'tysięcy ')
HUNDREDS_WORDS = ('złoty ', 'złote ', 'złotych ')
GROSZE_WORDS = ('grosz', 'grosze', 'groszy')

UNITIES = {
    1: 'jeden ',
    2: 'dwa ',
    3: 'trzy ',
    4: 'cztery ',
    5: 'pięć ',
    6: 'sześć ',
    7: 'siedem ',
    8: 'osiem ',
    9: 'dziewięć '
}
TEENS = {
    0: 'dziesięć ',
    1: 'jedenaście ',
    2: 'dwanaście ',
    3: 'trzynaście ',
    4: 'czternaście ',
    5: 'piętnaście ',
    6: 'szesnaście ',
    7: 'siedemnaście ',
    8: 'osiemnaście ',
    9: 'dziewiętnaście '
}
TENS = {
    2: 'dwadzieścia ',
    3: 'trzydzieści ',
    4: 'czterdzieści ',
    5: 'pięćdziesiąt ',
    6: 'sześćdziesiąt ',
    7: 'siedemdziesiąt ',
    8: 'osiemdziesiąt ',
    9: 'dziewięćdziesiąt '
}
HUNDREDS = {
    1: 'sto ',
    2: 'dwieście ',
    3: 'trzysta ',
    4: 'czterysta ',
    5: 'pięćset ',
    6: 'sześćset ',
    7: 'siedemset ',
    8: 'osiemset ',
    9: 'dziewięćset '
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
    if n == 1:
        plural = 0
    else:
        if n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            plural = 1
        else:
            plural = 2

    return plural


def form_part(amount):
    setki_trojliczby = amount // 100
    dziesiatki_trojliczby = (amount % 100) // 10
    jednosci_trojliczby = (
        amount -
        (setki_trojliczby * 100) -
        (dziesiatki_trojliczby * 10)
    ) // 1

    setki_trojliczby_slownie = ''
    jednosci_trojliczby_slownie = ''
    dzies_trojliczby_slownie = ''

    if setki_trojliczby >= 1:
        setki_trojliczby_slownie = HUNDREDS[setki_trojliczby]

    if dziesiatki_trojliczby == 1:
        dzies_trojliczby_slownie = TEENS[
            ((amount - (setki_trojliczby * 100)) % 10)
        ]
    elif 2 <= dziesiatki_trojliczby <= 9:
        dzies_trojliczby_slownie = TENS[(dziesiatki_trojliczby)]
        if jednosci_trojliczby > 0:
            jednosci_trojliczby_slownie = (UNITIES[jednosci_trojliczby])
    else:
        if jednosci_trojliczby != 0:
            jednosci_trojliczby_slownie = (
                UNITIES[jednosci_trojliczby]
            )

    zapis_liczby = (
        setki_trojliczby_slownie +
        dzies_trojliczby_slownie +
        jednosci_trojliczby_slownie
    )

    plural_amount = plural_form(amount)

    return zapis_liczby, plural_amount


def zlote(threes, setki):
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

    are_zlote = all((a == '' for a in formed_amount[:-1]))
    if liczba_setek == 0:
        liczba_setek_slownie = 'zero złotych ' if are_zlote else 'złotych '
    if (
        (not are_zlote or liczba_setek > 1) and
        (liczba_setek - (liczba_setek // 100)) == 1
    ):
        liczba_setek_slownie = 'złotych '
    formed_amount.append(liczba_setek_slownie)
    kwota_slownie = ''.join(formed_amount)
    setki = (setki - (liczba_setek * 1)) * 100

    return kwota_slownie, setki


def grosze(setki):
    liczba_groszy = setki // 1
    grosze, liczba_groszy_slownie = form_part(liczba_groszy)
    liczba_groszy_slownie = GROSZE_WORDS[liczba_groszy_slownie]

    if liczba_groszy == 0:
        liczba_groszy_slownie = 'zero groszy'

    formed_amount = grosze + liczba_groszy_slownie

    return formed_amount


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

    formed_amount_zlote, liczba_setek = zlote(threes, setki)
    formed_amount_grosze = grosze(liczba_setek)
    kwota_slownie = formed_amount_zlote + formed_amount_grosze

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
