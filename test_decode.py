import pytest
from morse import decode


@pytest.mark.parametrize(
    'msg, text',
    [
        ('... --- ...', 'SOS'),
        ('.--. -.-- - .... --- -.', 'PYTHON'),
        ('..--- ----- ..--- ...--', '2023'),
    ]
)
def test_decode(msg, text):
    assert decode(msg) == text


if __name__ == '__main__':
    pass
