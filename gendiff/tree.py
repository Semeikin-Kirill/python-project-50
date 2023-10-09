def change_bool(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    return value


def create_tree(first_data, second_data):
    uniq_keys = set([*first_data.keys(), *second_data.keys()])
    sorted_keys = sorted(list(uniq_keys))
    tree = []
    for key in sorted_keys:
        value1 = change_bool(first_data.get(key))
        value2 = change_bool(second_data.get(key))
        if key not in first_data:
            tree.append({
                'name': key,
                'type': 'added',
                'value': value2
            })
        elif key not in second_data:
            tree.append({
                'name': key,
                'type': 'deleted',
                'value': value1
            })
        elif isinstance(value1, dict) and isinstance(value2, dict):
            tree.append({
                'name': key,
                'type': 'nested',
                'children': create_tree(value1, value2)
            })
        elif value1 != value2:
            tree.append({
                'name': key,
                'type': 'changed',
                'value1': value1,
                'value2': value2
            })
        else:
            tree.append({
                'name': key,
                'type': 'unchanged',
                'value': value1
            })
    return tree
