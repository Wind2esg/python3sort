# python3 sort <http://github.com/Wind2esg/python3sort>
# Copyright 2018 Wind2esg
# Released under the MIT license <http://github.com/Wind2esg/python3sort/LICENSE>

# As if there is a gnome holding and moving the item in the array?
# gno is the the position of the gnome, cur is index of the target being sorted, and item is the taregt.
# The gnome starts from cur, holding the target, comparing with the one ahead of its current position.
# If the item is smaller, the gnome moves ahead, and we move the value of gno -1 to gno.
# If the item is bigger or equal, that means it finds the item's final position. Then put the item there. 
# The gnome return to the next target.

# Actually, I am in goblin side.

from _comparer import int_comparer

def gnome(array, compare = int_comparer):
  gno = 1
  cur = gno
  item = array[cur]
  while gno < len(array):
    if compare(item, array[gno - 1]) < 0:
      array[gno] = array[gno - 1]
      if gno > 1:
        gno -= 1
    else:
        array[gno] = item
        gno += cur + 1
        cur = gno
        item = array[cur]
  return array        
    
