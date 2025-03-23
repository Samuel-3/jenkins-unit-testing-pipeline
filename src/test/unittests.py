import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main.main import Functions

functions = Functions

class TestFunctions(unittest.TestCase):

    def test_multiple_by_two(self):
        self.assertEqual(functions.multiple_by_two(5), 10)

    def test_half(self):
        self.assertEqual(functions.half(20), 10)

    
def main():
    unittest.main()

if __name__ == "__main__":
    main()
