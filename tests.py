import unittest
import arithmetic


class TestArithmetic(unittest.TestCase):

	def test_count_2_3(self):
		data = {1: 2, 2: 5, 3: 8, 4: 11, 5: 14, 6: 17, 33: 98, 67: 200, 100: 299}
		for n, result in data.items():
			self.assertEqual(arithmetic.counting(2, 3, n), result)

	def test_count_4_5(self):
		data = {1: 4, 2: 9, 3: 14, 4: 19, 5: 24, 6: 29, 33: 164, 67: 334, 100: 499}
		for n, result in data.items():
			self.assertEqual(arithmetic.counting(4, 5, n), result)

	def test_count_m1_m6(self):
		data = {-1: 11, -2: 17, -3: 23, -4: 29, 5: -25, 6: -31, 33: -193, -33: 203}
		for n, result in data.items():
			self.assertEqual(arithmetic.counting(-1, -6, n), result)

	def test_count_2_0(self):
		n = [1, 2, 3, 4, 5, 6, 33, 67, 100]
		for element in n:
			self.assertEqual(arithmetic.counting(2, 0, element), 2)

if __name__ == '__main__':
    unittest.main()
