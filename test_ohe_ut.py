import unittest
from one_hot_encoder import fit_transform


class TestOneHotEncoder(unittest.TestCase):
    def test_ohe0(self):
        actual = fit_transform([])
        expected = []
        self.assertEqual(actual, expected)

    def test_ohe1(self):
        actual = fit_transform('Moscow')
        expected = [('Moscow', [1])]
        self.assertEqual(actual, expected)

    def test_ohe2(self):
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_ohe3(self):
        actual = fit_transform(['London', 'is', 'the',
                                'capital', 'of', 'Great', 'Britain'])
        expected = [
            ('London',
             [0, 0, 0, 0, 0, 0, 1]),
            ('is',
             [0, 0, 0, 0, 0, 1, 0]),
            ('the',
             [0, 0, 0, 0, 1, 0, 0]),
            ('capital',
             [0, 0, 0, 1, 0, 0, 0]),
            ('of',
             [0, 0, 1, 0, 0, 0, 0]),
            ('Great',
             [0, 1, 0, 0, 0, 0, 0]),
            ('Britain',
             [1, 0, 0, 0, 0, 0, 0])
        ]
        for expected_val in expected:
            self.assertIn(expected_val, actual)

    def test_ohe4(self):
        with self.assertRaises(
                TypeError,
                msg='expected at least 1 arguments, got 0'
        ):
            fit_transform()


if __name__ == '__main__':
    pass
