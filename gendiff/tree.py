def change_bool(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return value


def create_tree(first_data, second_data):
    all_keys = set([*first_data.keys(), *second_data.keys()])
    tree = {}
    for key in all_keys:
        if key not in first_data:
            tree[key] = {
                'type': 'added',
                'value': change_bool(second_data[key])
            }
        elif key not in second_data:
            tree[key] = {
                'type': 'removed',
                'value': change_bool(first_data[key])
            }
        else:
            value1 = change_bool(first_data[key])
            value2 = change_bool(second_data[key])
            tree[key] = {
                'type': 'unchanged' if value1 == value2 else 'changed',
                'value': value1 if value1 == value2 else (value1, value2)
            }
    return tree
