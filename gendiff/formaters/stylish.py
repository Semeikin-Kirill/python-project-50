symbols = {
    'added': '+',
    'deleted': '-',
    'unchanged': ' ',
}


def get_indent(depth, spacesCount=4):
    return ' '.ljust(depth * spacesCount - 2, ' ')


def stringify(node, depth):
    if not isinstance(node, dict):
        return node
    indent = get_indent(depth)
    result = []
    for key, value in node.items():
        next_indent = get_indent(depth + 1)
        result.append(f'{next_indent}  {key}: {stringify(value, depth + 1)}')
    return '\n'.join(['{', *result, f'{indent}  }}'])


def node_stringify(tree_diff):
    def iter(tree, depth):
        indent = get_indent(depth)
        result = []
        for node in tree:
            match node['type']:
                case 'nested':
                    children = node['children']
                    result.append(
                        '{0}  {1}: {2}'.format(indent,
                                               node['name'],
                                               '\n'.join([
                                                   '{',
                                                   iter(children, depth + 1),
                                                   f'{indent}  }}'])))
                case 'changed':
                    value1 = stringify(node['value1'], depth)
                    value2 = stringify(node['value2'], depth)
                    node1 = f"{indent}- {node['name']}: {value1}"
                    node2 = f"{indent}+ {node['name']}: {value2}"
                    result.append('\n'.join([node1, node2]))
                case 'added' | 'deleted' | 'unchanged':
                    name = node['name']
                    symbol = symbols[node['type']]
                    value = stringify(node['value'], depth)
                    result.append(
                        '{0}{1} {2}: {3}'.format(indent, symbol, name, value))
        return '\n'.join(result)
    return '\n'.join(['{', iter(tree_diff, 1), '}'])
