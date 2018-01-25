# python3 sort <http://github.com/Wind2esg/python3sort>
# Copyright 2018 Wind2esg
# Released under the MIT license <http://github.com/Wind2esg/python3sort/LICENSE>

# Whenever mentioned sort, always bubble first!

from _comparer import int_comparer


def bubble(array, compare=int_comparer):
    for i in range(0, len(array) - 1):
      for j in range(1, len(array) - i):
        if compare(array[j - 1], array[j]) > 0:
          array[j], array[j - 1] = array[j - 1], array[j]
  return array
