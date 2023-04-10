import unittest
from adder import even_adder

class TestEvenAdder(unittest.TestCase):

    def test_empty_list(self):
        expectedSum = None
        sum = even_adder.EvenAdder([]).add()
        self.assertEqual(sum, expectedSum)