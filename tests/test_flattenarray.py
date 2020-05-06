# third party modules
import pytest

# tool modules
import flattenarray

def test_flatten_to_list_01():
    input_array = [1, [2, 3, [4], []], [], 5, [[], [6]]]
    result = [1, 2, 3, 4, 5, 6]
    assert flattenarray.flatten_to_list(input_array) == result

def test_flatten_to_list_02():
    input_array = [[1, 2, 3], (4, ([5]), 6), [7], [8, 9]]
    result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert flattenarray.flatten_to_list(input_array) == result
