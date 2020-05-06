#!/usr/bin/env python3


def flatten_to_list(input_array):
    result = list()
    for item in input_array:
        if isinstance(item, (list, tuple)):
            sub_array = flatten_to_list(item)
            result.extend(sub_array)
        else:
            result.append(item)
    return result
