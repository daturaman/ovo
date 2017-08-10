import unittest
from ovo import Tariff

class TestOvo(unittest.TestCase):

    def test_usage(self):
        t = Tariff()
        result = t.usage('better-energy', 'power', 100)
        self.assertEqual(result, 635.76)
    

if __name__ == '__main__':
    unittest.main()
