# python3 sort <http://github.com/Wind2esg/python3sort>
# Copyright 2018 Wind2esg
# Released under the MIT license <http://github.com/Wind2esg/python3sort/LICENSE>

from _comparer import int_comparer


def cocktail(array, compare=int_comparer):
    left = 0
    right = len(array) - 1
    step = 1
    while left != right:
        for i in range(left, right, step):
            if compare(array[i], array[i + 1]) > 0:
                array[i], array[i + 1] = array[i + 1], array[i]
        left, right = right - 1, left
        step *= -1
    return array
