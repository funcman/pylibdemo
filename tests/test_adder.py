import unittest
from pylibdemo import add_numbers, accumulate_n_times

class TestAdder(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
        
    def test_accumulate_n_times(self):
        self.assertEqual(accumulate_n_times(2, 3), 6)
        self.assertEqual(accumulate_n_times(1, 5), 5)
        self.assertEqual(accumulate_n_times(0, 10), 0)
        self.assertEqual(accumulate_n_times(3, 0), 0)

if __name__ == '__main__':
    unittest.main() 