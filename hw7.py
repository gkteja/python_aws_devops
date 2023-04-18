# import unittest
# import calc

# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#     	self.assertTrue('FOO'.isupper())
#     	self.assertFalse('Foo'.isupper())

#     def test_add(self):
#     	result = calc.add(10,15)
#     	self.assertEqual(result,25)

# if __name__ == '__main__':
#     unittest.main()

import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
    	self.assertEqual(calc.add(10,5),15)

if __name__ == '__main__':
    unittest.main()