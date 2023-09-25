import json
from gendiff.parser import data_parser


def dec_bool(param):
    for key, value in param.items():
        if isinstance(value, bool):
            param[key] = 'true' if value else 'false'
    return param


def get_data(file_path):
    with open(file_path) as data:
        return json.load(data, object_hook=dec_bool)


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
    tree = data_parser(data1, data2)
    items = sorted(tree.items(), key=lambda items: items[0])
    result = ['{', *list(map(string_generation, items)), '}']
    return '\n'.join(result)
