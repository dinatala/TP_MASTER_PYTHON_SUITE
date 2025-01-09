import unittest
from unittest import result


def save_division(a, b):
    if b == 0:
      raise ZeroDivisionError("Division par zéro.")
      result = int(a / b)
    return result


class TestDivision(unittest.TestCase):
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            print(save_division(10,0))

unittest.main()


 
