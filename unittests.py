import unittest
from activities import eat,nap,is_funny,laugh

class ActivityTests(unittest.TestCase):
	
	def test_eat_healthy(self):
		"""eat should havea +ve msg for healthy eating"""
		self.assertEqual(
			eat('broccoli', is_healthy=True),
			"I'm eating broccoli because my body is a temple")
	
	def test_eat_unhealthy(self):
		self.assertEqual(eat('pizza', is_healthy=False), "I'm eating pizza because YOLO!")

	def test_eat_heathy_boolean(self):
		'''is healthiy must be  bool'''
		with self.assertRaises(ValueError):
			eat('pizza', is_healthy='who cares?')

	def test_short_nap(self):
		"""short naps should be refreshing"""
		self.assertEqual(nap(1), "I'm feeling refreshed after my 1 hour nap")
	
	def test_long_nap(self):
		self.assertEqual(nap(7), "UGHHH I overslept:'), should'nt have slept for 7 long hours")

	def test_is_funny_tim(self):
		self.assertEqual(is_funny('tim'), False)

	def test_is_funny_anyone_else(self):
		"""anyone else but tim should be funny"""
		self.assertTrue(is_funny('Blue'), 'blue should be funny')
		self.assertTrue(is_funny('tammy'), 'tammy should be funny')
		self.assertTrue(is_funny('sven'), 'sven should be funny')

	def test_laugh(self):
		self.assertIn(laugh(), ('lol', 'hahaha', 'tehehehe'))

if __name__ == "__main__":
	unittest.main()