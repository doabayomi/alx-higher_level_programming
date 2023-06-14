#!/usr/bin/python3
def best_score(a_dictionary):
    try:
        dict_keys = list(a_dictionary.keys())
    except AttributeError:
        return None

    if (len(dict_keys) < 1):
        return None
    else:
        max_val = a_dictionary.get(dict_keys[0])
        max_val_key = dict_keys[0]
        for key in dict_keys:
            val = a_dictionary.get(key)
            if val > max_val:
                max_val = val
                max_val_key = key
            else:
                continue
        return max_val_key
