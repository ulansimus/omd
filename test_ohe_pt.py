import pytest
from one_hot_encoder import fit_transform


def test_ohe0():
    assert fit_transform([]) == []


def test_ohe1():
    assert fit_transform('Moscow') == [('Moscow', [1])]


def test_ohe2():
    actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected


def test_ohe3():
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
        assert expected_val in actual


def test_ohe4():
    with pytest.raises(
            TypeError,
            match='expected at least 1 arguments, got 0'
    ):
        fit_transform()


if __name__ == '__main__':
    pass
