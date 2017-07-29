import unittest
import line_intersect

class Line(unittest.TestCase):
	def setUp(self):
		print('Start')
		self.in1 = ([(1.0, 0.0), (1.0, 3.0)], [(0.0, 2.0), (2.0, 2.0)])
		self.in2 = ([(1.0, 0.0), (1.0, 3.0)], [(0.0, 'fail'), (2.0, 2.0)])
		self.in3 = ([(1.0, 0.0), (1.0, 3.0)], [(2.0, 0.0), (2.0, 3.0)])
		self.in4 = ([(-1.0, 0.0), (-1.0, 3.0)], [(0.0, 3.0), (-2.0, 3.0)])
		self.in5 = ([(1.0, 0.0), (1.0, 3.0)], [(1.0, 0.0), (1.0, 3.0)])
	def test1(self):
		expect1 = (1.0, 2.0)
		self.assertEqual(expect1, line_intersect.line_intersect(self.in1))
	def test2(self):
		expect2 = None
		self.assertEqual(expect2, line_intersect.line_intersect(self.in2))
	def test3(self):
		expect3 = '||'
		self.assertEqual(expect3, line_intersect.line_intersect(self.in3))
	def test4(self):
		expect4 = (-1.0, 3.0)
		self.assertEqual(expect4, line_intersect.line_intersect(self.in4))
	def test5(self):
		expect5 = [(1.0, 0.0), (1.0, 3.0)]
		self.assertEqual(expect5, line_intersect.line_intersect(self.in5))
	def test6(self):
		expect6 = None
		self.assertEqual(expect6, line_intersect.line_intersect(([],[])))
	def tearDown(self):
		print('End')
		self.in1 = None
		self.in2 = None
		self.in3 = None
		self.in4 = None
		self.in5 = None

if __name__ == '__main__':
	unittest.main()