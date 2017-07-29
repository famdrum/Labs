import unittest
import is_sorted

class Sort(unittest.TestCase):
	def setUp(self):
		self.in1 = [1,2,3,4]
		self.in2 = [1,2,3,3,4]
		self.in3 = [1,2,3,5,4]
		self.in4 = [1,2,3,'hello',4]
		self.in5 = 'fail'
	def test1(self):
		expect1 = True
		self.assertEqual(expect1, is_sorted.is_sorted(self.in1))
	def test2(self):
		expect2 = True
		self.assertEqual(expect2, is_sorted.is_sorted(self.in2))
	def test3(self):
		expect3 = False
		self.assertEqual(expect3, is_sorted.is_sorted(self.in3))
	def test4(self):
		expect4 = None
		self.assertEqual(expect4, is_sorted.is_sorted(self.in4))
	def test5(self):
		expect5 = None
		self.assertEqual(expect5, is_sorted.is_sorted(self.in5))

if __name__ == '__main__':
	unittest.main()