import json
import yaml


def parser_yaml(data):
    return yaml.load(data, Loader=yaml.CLoader)


parsers = {
    'json': lambda data: json.load(data),
    'yml': parser_yaml,
    'yaml': parser_yaml
}


def parser(data, suffix):
    return parsers[suffix](data)
