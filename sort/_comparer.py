# python3 sort <http://github.com/Wind2esg/python3sort>
# Copyright 2018 Wind2
# Released under the MIT license <http://github.com/Wind2esg/python3sort/LICENSE>

# this is compare function, might be better delivery lambda in real

def _comparer(a,b):
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0