from django.test import TestCase

from app.calc import add,sub

class ClacTests(TestCase):
	def test_add_numbers(self):
		self.assertEqual(add(3, 8), 11)
		self.assertEqual(add(4, 4), 8)
		
	def test_subtract(self):
		self.assertEqual(sub(8, 5), 3)