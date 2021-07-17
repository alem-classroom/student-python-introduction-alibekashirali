dict = {'first': 'первый', 'second': 'второй'}

def reverse_dict(dict):
    # swap keys and values within dict and return dict
    inv_map = {v: k for k, v in dict.items()}
    return inv_map

print(reverse_dict(dict))