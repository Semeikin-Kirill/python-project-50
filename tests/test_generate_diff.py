import pytest
from gendiff.generate_diff import generate_diff

FILE1 = 'tests/fixtures/file1.json'
FILE2 = 'tests/fixtures/file2.json'
FILE3 = 'tests/fixtures/file3.yml'
FILE4 = 'tests/fixtures/file4.yaml'


@pytest.fixture
def get_expected_stylish():
    with open('tests/fixtures/expected_stylish.txt') as expected_data:
        return expected_data.read().strip()


@pytest.fixture
def get_expected_plain():
    with open('tests/fixtures/expected_plain.txt') as expected_data:
        return expected_data.read().strip()


def test_generate_diff_json_file(get_expected_stylish):
    assert generate_diff(FILE1, FILE2) == get_expected_stylish


def test_generate_diff_yaml_file(get_expected_stylish):
    assert generate_diff(FILE3, FILE4) == get_expected_stylish


def test_generate_diff_json_file_plain(get_expected_plain):
    assert generate_diff(FILE1, FILE2, 'plain') == get_expected_plain


def test_generate_diff_yaml_file_plain(get_expected_plain):
    assert generate_diff(FILE3, FILE4, 'plain') == get_expected_plain
