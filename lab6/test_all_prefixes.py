import unittest
import all_prefixes

class Pref(unittest.TestCase):
	def setUp(self):
		print('Start')
		self.in1 = 'lead'
		self.in2 = 'avangard'
		self.in3 = 'fai123l'
		self.in4 = 123
	def test1(self):
		expect1 = [{'le', 'lead', 'lea', 'l'}]
		self.assertEqual(expect1, all_prefixes.all_prefixes(self.in1))
	def test2(self):
		expect2 = [{'avangar', 'avang', 'avangard', 'avanga', 'a', 'av', 'ava', 'avan'}, {'ang', 'anga', 'a', 'angard', 'an', 'angar'}, {'a', 'ard', 'ar'}]
		self.assertEqual(expect2, all_prefixes.all_prefixes(self.in2))
	def test3(self):
		expect3 = None
		self.assertEqual(expect3, all_prefixes.all_prefixes(self.in3))
	def test4(self):
		expect4 = None
		self.assertEqual(expect4, all_prefixes.all_prefixes(self.in4))
	def tearDown(self):
		print('End')
		self.in1 = None
		self.in2 = None
		self.in3 = None
		self.in4 = None

if __name__ == '__main__':
	unittest.main()