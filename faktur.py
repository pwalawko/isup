def fakturowanie():
    amount = input('Podaj liczbę ')
    single = {'1': 'jeden', '2': 'dwa', '3': 'trzy', '4': 'cztery', '5': 'pięć',
            '6': 'sześć', '7': 'siedem', '8': 'osiem', '9': 'dziewięć'}
    teens = {'1': 'jedenaście', '2': 'dwanaście', '3': 'trzynaście',
            '4': 'czternaście', '5': 'piętnaście', '6': 'szesnaście',
            '7': 'siedemnaście', '8': 'osiemnaście', '9': 'dziewiętnaście'}

    # grosze
    jedn_gr = ''
    dzies_gr = ''
    if amount[-2] == '1':
        if amount[-1] == '0':
            dzies_gr = 'dziesięć'
        else:
            dzies_gr = teens[amount[-1]]
    elif amount[-2] == '2':
        dzies_gr = 'dwadzieścia'
    elif amount[-2] == '3' or amount[-2] == '4':
        dzies_gr = single[amount[-2]] + 'dzieści'
        if amount[-2] == '4':
            dzies_gr = 'czterdzieści'
    elif amount[-2] in ('5', '6', '7', '8', '9'):
        dzies_gr = single[amount[-2]] + 'dziesiąt'
    elif amount[-2] == '0':
        if amount[-1] == '0':
            jedn_gr = 'zero'
            dzies_gr = ''
            grosze = ' groszy'
    if amount[-2] in ('0', '2', '3', '4', '5', '6', '7', '8', '9'):
        if amount[-1] in ('1', '2', '3', '4', '5', '6', '7', '8', '9',):
            jedn_gr = ' ' + single[amount[-1]]
            if amount[-1] == '1':
                if amount[-2] == '0':
                    grosze = ' grosz'
                else:
                    grosze = ' groszy'
            if amount[-1] in ('2', '3', '4'):
                grosze = ' grosze'
            if amount[-1] in ('5', '6', '7', '8', '9', '0'):
                grosze = ' groszy'

    # setki
    set_zl = ''
    dzies_zl = ''
    jedn_zl = ''
    if amount[-6] == '1':
        set_zl = 'sto'
    elif amount[-6] == '2':
        set_zl = 'dwieście'
    elif amount[-6] in ('3', '4'):
        set_zl = single[amount[-6]] + 'sta'
    elif amount[-6] in ('5', '6', '7', '8', '9'):
        set_zl = single[amount[-6]] + 'set'
    if amount[-5] == '1':
        if amount[-4] == '0':
            dzies_zl = 'dziesięć'
        else:
            dzies_zl = teens[amount[-4]]
    elif amount[-5] == '2':
        dzies_zl = 'dwadzieścia'
    elif amount[-5] == '3' or amount[-5] == '4':
        dzies_zl = single[amount[-5]] + 'dzieści'
        if amount[-5] == '4':
            dzies_zl = 'czterdzieści'
    elif amount[-5] in ('5', '6', '7', '8', '9'):
        dzies_zl = single[amount[-5]] + 'dziesiąt'
    elif amount[-5] == '0':
        if amount[-4] == '0':
            jedn_zl = 'zero'
            dzies_zl = ''
            zlote = ' złotych'
    if amount[-5] in ('0', '2', '3', '4', '5', '6', '7', '8', '9'):
        if amount[-4] in ('1', '2', '3', '4', '5', '6', '7', '8', '9',):
            jedn_zl = ' ' + single[amount[-4]]
            if amount[-4] == '1':
                if amount[-4] == '0':
                    zlote = ' złoty'
                else:
                    zlote = ' złotych'
            if amount[-4] in ('2', '3', '4'):
                zlote = ' złote'
            if amount[-4] in ('5', '6', '7', '8', '9', '0'):
                zlote = ' złotych'




    print(dzies_gr + jedn_gr + grosze)

fakturowanie()

#   1 .  0    0    0 . 0   0   0 . 0   0   0   ,   0   0
#[-13][-12][-11][-10][-9][-8][-7][-6][-5][-4][-3][-2][-1]
