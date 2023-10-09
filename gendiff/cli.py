import argparse
from gendiff.generate_diff import generate_diff


def cli():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish')
    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    formater = args.format
    print(generate_diff(first_file, second_file, formater))
