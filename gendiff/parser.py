def data_parser(first_data, second_data):
    all_keys = set([*first_data.keys(), *second_data.keys()])
    tree = {}
    for key in all_keys:
        if key not in first_data:
            tree[key] = {
                'type': 'added',
                'value': second_data[key]
            }
        elif key not in second_data:
            tree[key] = {
                'type': 'removed',
                'value': first_data[key]
            }
        else:
            value1 = first_data[key]
            value2 = second_data[key]
            tree[key] = {
                'type': 'unchanged' if value1 == value2 else 'changed',
                'value': value1 if value1 == value2 else (value1, value2)
            }
    return tree
