import sys
from decimal import Decimal


JEDNOSCI = {'1': 'jeden',
            '2': 'dwa',
            '3': 'trzy',
            '4': 'cztery',
            '5': 'pięć',
            '6': 'sześć',
            '7': 'siedem',
            '8': 'osiem',
            '9': 'dziewięć'}
NASTKI = {'0': 'dziesięć',
          '1': 'jedenaście',
          '2': 'dwanaście',
          '3': 'trzynaście',
          '4': 'czternaście',
          '5': 'piętnaście',
          '6': 'szesnaście',
          '7': 'siedemnaście',
          '8': 'osiemnaście',
          '9': 'dziewiętnaście'}
DZIESIATKI = {'2': 'dwadzieścia',
              '3': 'trzydzieści',
              '4': 'czterdzieści',
              '5': 'pięćdziesiąt',
              '6': 'sześćdziesiąt',
              '7': 'siedemdziesiąt',
              '8': 'osiemdziesiąt',
              '9': 'dziewięćdziesiąt'}
SETKI = {'1': 'sto',
        '2': 'dwieście',
        '3': 'trzysta',
        '4': 'czterysta',
        '5': 'pięćset',
        '6': 'sześćset',
        '7': 'siedemset',
        '8': 'osiemset',
        '9': 'dziewięćset'}

MILIONY_SLOWNIE = {1: 'milion',
                   2: 'miliony',
                   3: 'miliony',
                   4: 'miliony',
                   5: 'milionów',
                   6: 'milionów',
                   7: 'milionów',
                   8: 'milionów',
                   9: 'milionów',
                   0: 'milionów',
                   'nic': ''}
TYSIACE_SLOWNIE = {1: 'tysiąc',
                   2: 'tysiące',
                   3: 'tysiące',
                   4: 'tysiące',
                   5: 'tysięcy',
                   6: 'tysięcy',
                   7: 'tysięcy',
                   8: 'tysięcy',
                   9: 'tysięcy',
                   0: 'tysięcy',
                   'nic': ''}
SETKI_SLOWNIE = {1: 'złoty',
                 2: 'złote',
                 3: 'złote',
                 4: 'złote',
                 5: 'złotych',
                 6: 'złotych',
                 7: 'złotych',
                 8: 'złotych',
                 9: 'złotych',
                 0: 'złotych',
                 'nic': ''}
GROSZE_SLOWNIE = {1: 'grosz',
                  2: 'grosze',
                  3: 'grosze',
                  4: 'grosze',
                  5: 'groszy',
                  6: 'groszy',
                  7: 'groszy',
                  8: 'groszy',
                  9: 'groszy',
                  0: 'groszy',
                  'nic': ''}


def main():
    try:
        amount = Decimal(sys.argv[1])
    except ValueError:
        print('Nieprawidłowe dane!')
    except IndexError:
        print('Brakujący parametr!')
    else:
        print(fakturowanie(amount))


def fakturowanie(amount):
    if not isinstance(amount, Decimal):
        raise Exception('Nieprawidłowe dane!')
    if amount > 1000000000:
        raise Exception('Zbyt duża wartość!')
    if amount < 0:
        raise Exception('Zbyt mała wartość!')
    amount.quantize(Decimal('.01'))

    # miliard może być tylko jeden, więc definiujemy taki prosty przypadek
    liczba_miliardow = amount // 1000000000
    if liczba_miliardow == 1:
        miliard = JEDNOSCI['1'] + ' ' + 'miliard' + ' '
        amount1 = amount - 1000000000
    else:
        amount1 = amount
        miliard = ''

    # Dla setek, tysięcy i milionów część setkowa będzie taka sama,
    # tak więc możemy zrobić jedną funkcję i wykorzystać ją w tych trzech przypadkach.
    # Kwotą może być liczba milionów, tysięcy i jedności.
    def trojliczby(kwota):
        #import ipdb; ipdb.set_trace()
        # Sprawdzamy ile jest setek.
        setki_trojliczby = kwota // 100
        # Jeśli są, bierzemy ze słownika z setkami wartość odpowiadającą ilości setek.
        if setki_trojliczby >= 1:
            setki_trojliczby_slownie = SETKI[str(setki_trojliczby)] + ' '
        # Jeśli nie ma, zostawiamy setki puste.
        else:
            setki_trojliczby_slownie = ''
        # Sprawdzamy ile jest dziesiątek, odejmując najpierw uwzględnione już wcześniej setki.
        dziesiatki_trojliczby = (kwota - (setki_trojliczby * 100)) // 10
        # Jeśli są, bierzemy ze słownika z dziesiątkami wartość odpowiadającą ilości dziesiątek.
        # Trzeba wziąć pod uwagę, że dla nastek zapis słowny jest inny niż dla dziesiątek większych niż 1.
        jednosci_trojliczby_slownie = ''
        jednostka_ze_slownika = 'nic'
        if dziesiatki_trojliczby == 1:
            dzies_trojliczby_slownie = NASTKI[str((kwota - (setki_trojliczby * 100)) % 10)] + ' '
            # Jeśli są nastki, kwota słownie zawsze końcy się tak samo,
            # więc można użyć stałą wartość.
            jednostka_ze_slownika = 5
        # Teraz zapis dla kwóty dziesiątek innej niż nastki.
        elif 2 <= dziesiatki_trojliczby <= 9:
            dzies_trojliczby_slownie = DZIESIATKI[str(dziesiatki_trojliczby)] + ' '
            # Jedności są obsłużone w ramach dziesiątek, ponieważ nie będzie ich przy nastkach.
            # Sprawdzamy ilość jedności.
            jednosci_trojliczby = (kwota - (setki_trojliczby * 100) - (dziesiatki_trojliczby * 10)) // 1
            if jednosci_trojliczby > 0:
                jednosci_trojliczby_slownie = str(JEDNOSCI[str(jednosci_trojliczby)]) + ' '
            # Czas na zapis słowny jednostek. Będą one pobierane ze słownika,
            # w zaneżności od tego czy funkcja jest zastosowana dla milionów, tysięcy czy setek zł.
            jednostka_ze_slownika = jednosci_trojliczby
            # Trzeba obsłużyć przypadek, gdy liczba kończy się na 1.
            if jednosci_trojliczby == 1:
                jednostka_ze_slownika = 5
        # I zapis dla kwoty gdy nie ma dziesiątek.
        else:
            dzies_trojliczby_slownie = ''
            jednosci_trojliczby = (kwota - (setki_trojliczby * 100) - (dziesiatki_trojliczby * 10)) // 1
            if jednosci_trojliczby == 0:
                jednosci_trojliczby_slownie = ''
                if setki_trojliczby > 0:
                    jednostka_ze_slownika = 5
            else:
                jednosci_trojliczby_slownie = str(JEDNOSCI[str(jednosci_trojliczby)]) + ' '
                jednostka_ze_slownika = jednosci_trojliczby
                if setki_trojliczby == 0:
                    jednostka_ze_slownika = jednosci_trojliczby
                else:
                    jednostka_ze_slownika = 5
        # Trzeba jeszcze obsłużyć przypadki, gdy
        # Funkcja zwraca zapis liczy oraz wartość jednostki ze słownika.
        return (setki_trojliczby_slownie + dzies_trojliczby_slownie + jednosci_trojliczby_slownie), (jednostka_ze_slownika)

    liczba_milionow = amount1 // 1000000
    miliony, liczba_milionow_slownie = trojliczby(liczba_milionow)
    liczba_milionow_slownie = MILIONY_SLOWNIE[liczba_milionow_slownie] + ' '
    amount2 = (amount1 - (liczba_milionow * 1000000))

    liczba_tysiecy = amount2 // 1000
    tysiace, liczba_tysiecy_slownie = trojliczby(liczba_tysiecy)
    liczba_tysiecy_slownie = TYSIACE_SLOWNIE[liczba_tysiecy_slownie] + ' '
    amount3 = (amount2 - (liczba_tysiecy * 1000))

    liczba_setek = amount3 // 1
    stowy, liczba_setek_slownie = trojliczby(liczba_setek)
    liczba_setek_slownie = SETKI_SLOWNIE[liczba_setek_slownie] + ' '
    amount4 = (amount3 - (liczba_setek * 1)) * 100

    liczba_groszy = amount4 // 1
    grosze, liczba_groszy_slownie = trojliczby(liczba_groszy)
    liczba_groszy_slownie = GROSZE_SLOWNIE[liczba_groszy_slownie]

    if grosze == '':
        liczba_groszy_slownie = 'zero groszy'
    if liczba_milionow + liczba_tysiecy + liczba_setek == 0:
        liczba_setek_slownie = 'zero złotych '

    kwota_slownie = str(miliard +
        miliony + liczba_milionow_slownie +
        tysiace + liczba_tysiecy_slownie +
        stowy + liczba_setek_slownie +
        grosze + liczba_groszy_slownie)

    kwota_slownie = kwota_slownie.replace('   ', ' ')
    kwota_slownie = kwota_slownie.replace('  ', ' ')
    kwota_slownie = kwota_slownie.strip()

    return kwota_slownie


if __name__ == '__main__':
    main()
