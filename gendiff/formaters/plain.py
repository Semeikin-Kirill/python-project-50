from itertools import chain


def stringify(value):
    if (isinstance(value, dict)):
        return '[complex value]'
    elif (isinstance(value, str)) and value not in ('true', 'null', 'false'):
        return f"'{value}'"
    return str(value)


def plain(tree_diff):
    def iter(tree, path):
        result = []
        for node in tree:
            current_path = '.'.join([*path, node['name']])
            match(node['type']):
                case 'added':
                    result.append(
                       f'''Property '{current_path
                                      }' was added with value: {stringify(
                          node['value'])}''')
                case 'deleted':
                    result.append(f"Property '{current_path}' was removed")
                case 'changed':
                    result.append(f'''Property '{
                       current_path}' was updated. From {stringify(
                       node['value1'])} to {stringify(
                       node['value2'])}''')
                case 'nested':
                    result.extend(iter(node['children'], [current_path]))
        return list(chain(result))
    return '\n'.join(iter(tree_diff, []))
