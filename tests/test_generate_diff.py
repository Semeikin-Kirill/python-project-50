import pytest
from gendiff.generate_diff import generate_diff

FILE1 = 'tests/fixtures/file1.json'
FILE2 = 'tests/fixtures/file2.json'
FILE3 = 'tests/fixtures/file3.yml'
FILE4 = 'tests/fixtures/file4.yaml'


@pytest.fixture
def get_expected():
    with open('tests/fixtures/expected.txt') as expected_data:
        return expected_data.read().strip()


def test_generate_diff_json_file(get_expected):
    assert generate_diff(FILE1, FILE2) == get_expected


def test_generate_diff_yaml_file(get_expected):
    assert generate_diff(FILE3, FILE4) == get_expected

