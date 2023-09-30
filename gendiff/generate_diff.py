import json
import yaml
from pathlib import Path
from gendiff.tree import create_tree


def parser_yaml(data):
    return yaml.load(data, Loader=yaml.CLoader)


parsers = {
    'json': lambda data: json.load(data),
    'yml': parser_yaml,
    'yaml': parser_yaml
}


def get_data(file_path):
    suffix = Path(file_path).suffix[1:]
    with open(file_path) as data:
        return parsers[suffix](data)


def changed(key, values):
    return f'''{state['removed'](key, values[0])}
{state['added'](key, values[1])}'''


state = {
    'added': lambda key, value: f'  + {key}: {value}',
    'removed': lambda key, value: f'  - {key}: {value}',
    'changed': changed,
    'unchanged': lambda key, value: f'    {key}: {value}',
}


def string_generation(items):
    key, values = items
    type = values['type']
    value = values['value']
    return state[type](key, value)


def generate_diff(file_path1, file_path2):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    tree = create_tree(data1, data2)
    items = sorted(tree.items(), key=lambda items: items[0])
    result = ['{', *list(map(string_generation, items)), '}']
    return '\n'.join(result)
