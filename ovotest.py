import unittest
from ovo import Tariff

#This is the same as a 'Parameterized' test in Junit.
class TestOvo(unittest.TestCase):

    usage_params = [
        [('better-energy', 'power', 100), 635.76],
        [('2yr-fixed', 'gas', 250), 7748.15],
        [('greener-energy', 'power', 80), 439.51],
        [('simpler-energy', 'power', 120), 755.99]
    ]

    cost_params = [
        [(100, 50), {('better-energy', 120.82), ('greener-energy', 121.17), ('2yr-fixed', 126.47), ('simpler-energy', 126.63)}],
        [(400, 120), {('simpler-energy', 173.01), ('better-energy', 166.0), ('greener-energy', 169.81), ('2yr-fixed', 172.65)}],
        [(950, 310), {('greener-energy', 258.97), ('2yr-fixed', 259.24), ('simpler-energy', 260.18), ('better-energy', 250.69)}]
    ]

    def test_usage(self):
        for i in self.usage_params:
            with self.subTest():
                args = i[0]
                expected = i[1]
                self.assertEqual(Tariff.usage(*args), expected)

    def test_cost(self):
        for i in self.cost_params:
            with self.subTest():
                args = i[0]
                expected = i[1]
                self.assertTrue(Tariff.cost(*args) >= expected)


if __name__ == '__main__':
    unittest.main()
