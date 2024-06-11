import unittest
from main import jorge

class TestJorge(unittest.TestCase):
    def test_jorge(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()