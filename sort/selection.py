# python3 sort <http://github.com/Wind2esg/python3sort>
# Copyright 2018 Wind2esg
# Released under the MIT license <http://github.com/Wind2esg/python3sort/LICENSE>

# Selection sort, everytime pick the smallest value 

from _comparer import int_comparer

def selection(array, compare = int_comparer):
    for i in range(0, len(array)):
        min_index = i
        for j in range(0, len(array)):
            if compare(array[j], array[min_index]) < 0:
                min_index = j
        if min_index != 1:
            array[i], array[min_index] = array[min_index], array[i]
    return array