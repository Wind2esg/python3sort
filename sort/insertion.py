# python3 sort <http://github.com/Wind2esg/python3sort>
# Copyright 2018 Wind2
# Released under the MIT license <http://github.com/Wind2esg/python3sort/LICENSE>

# Build a sorted range from 0 to i - 1, then try to find the position for the i item
# Because it is sorted in the range, when finding, compare the i item with the mid of the range
# insert the i item then update the sorted range from the position to i.

from _comparer import int_comparer

def find_posion(array, start, end, item, compare = int_comparer):
    if compare(item, array[end // 2]) > 0 :
      start = end // 2
    else:
      end = end // 2
    if start == end:
      return start
    else:
      return find_posion(array, start, end)

def insertion(array, compare = int_comparer):
  for i in range(1, len(array)):
    position = find_posion(array, 0, i - 1, array[i])
    tmp = array[i]
    for j in range(i, position, -1):
      array[j] = array[j -1]
    array[position] = tmp
  return arrayy

