# python3 sort <http://github.com/Wind2esg/python3sort>
# Copyright 2018 Wind2esg
# Released under the MIT license <http://github.com/Wind2esg/python3sort/LICENSE>

from _comparer import int_comparer


def quick(array, compare=int_comparer):
    return find_position(array, 0, len(array) - 1)


def find_position(array, left, right, compare=int_comparer):
    i = left
    j = right
    if i >= j:
        return array
    key = array[i]
    while i < j:
        while i < j and array[j] >= key:
            j = j - 1
        array[i] = array[j]
        while i < j and array[i] <= key:
            i = i + 1
        array[j] = array[i]
    find_position(array, left, i - 1)
    find_position(array, j - 1, right)
    return array
