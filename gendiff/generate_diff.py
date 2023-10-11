from pathlib import Path
from gendiff.tree import create_tree
from gendiff.parser import parser
from .formaters import node_stringify, plain, json_formatter


def get_data(file_path):
    suffix = Path(file_path).suffix[1:]
    with open(file_path) as data:
        return parser(data, suffix)


formatters = {
    'stylish': node_stringify,
    'plain': plain,
    'json': json_formatter
}


def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    tree = create_tree(data1, data2, formatter)
    result = formatters[formatter](tree)
    return result
