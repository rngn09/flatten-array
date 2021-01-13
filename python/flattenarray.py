# function to flatten given array of arbitrarily nested arrays of integers


def flatten_to_list(input_array):
    result = list()
    for item in input_array:
        if isinstance(item, (list, tuple)):
            sub_array = flatten_to_list(item)
            result.extend(sub_array)
        else:
            result.append(item)
    return result

# here
