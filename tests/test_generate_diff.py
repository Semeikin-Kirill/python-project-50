import pytest
from gendiff.generate_diff import generate_diff

FILE1 = 'tests/fixtures/file1.json'
FILE2 = 'tests/fixtures/file2.json'


@pytest.fixture
def get_expected():
    with open('tests/fixtures/expected.txt') as expected_data:
        print(expected_data)
        return expected_data.read().strip()


def test_generate_diff(get_expected):
    assert generate_diff(FILE1, FILE2) == get_expected
