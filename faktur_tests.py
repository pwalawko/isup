from decimal import Decimal
import unittest

import faktur


PRZYKLADY_KWOT = {
    '0.0': "zero złotych zero groszy",
    '0.0001': "zero złotych zero groszy",
    '0.009': "zero złotych zero groszy",
    '0.01': "zero złotych jeden grosz",
    '0.02': "zero złotych dwa grosze",
    '0.21': "zero złotych dwadzieścia jeden groszy",
    '1': "jeden złoty zero groszy",
    '2': "dwa złote zero groszy",
    '5': "pięć złotych zero groszy",
    '12.99': "dwanaście złotych dziewięćdziesiąt dziewięć groszy",
    '21': "dwadzieścia jeden złotych zero groszy",
    '100': "sto złotych zero groszy",
    '101': "sto jeden złotych zero groszy",
    '222': "dwieście dwadzieścia dwa złote zero groszy",
    '1100': "jeden tysiąc sto złotych zero groszy",
    '45678.90': "czterdzieści pięć tysięcy sześćset siedemdziesiąt osiem "
    "złotych dziewięćdziesiąt groszy",
    '987654.18': "dziewięćset osiemdziesiąt siedem tysięcy sześćset "
    "pięćdziesiąt cztery złote osiemnaście groszy",
    '1000000': "jeden milion złotych zero groszy",
    '1000001': "jeden milion jeden złotych zero groszy",
    '10000000': "dziesięć milionów złotych zero groszy",
    '100000000': "sto milionów złotych zero groszy",
    '100100100.10': "sto milionów sto tysięcy sto złotych dziesięć groszy",
    '16012015.13': "szesnaście milionów dwanaście tysięcy piętnaście złotych "
    "trzynaście groszy",
    '102102102': "sto dwa miliony sto dwa tysiące sto dwa złote zero groszy",
    '999999999': "dziewięćset dziewięćdziesiąt dziewięć milionów "
    "dziewięćset dziewięćdziesiąt dziewięć tysięcy "
    "dziewięćset dziewięćdziesiąt dziewięć złotych "
    "zero groszy"
}


class TestFaktur(unittest.TestCase):

    def test_1_zl(self):
        for kwota, slownie in PRZYKLADY_KWOT.items():
            self.assertEqual(faktur.fakturowanie(Decimal(kwota)), slownie)

    def test_raise_value_error(self):
        self.assertRaises(TypeError, faktur.fakturowanie, 'a')
        self.assertRaises(TypeError, faktur.fakturowanie, 2)


if __name__ == '__main__':
    unittest.main()
