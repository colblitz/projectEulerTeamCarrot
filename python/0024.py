from math import *
from util import *

#######################
# Project Euler #000x #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

def order3(a, b, c, n):
  if n == 0:
    return [a, b, c]
  elif n == 1:
    return [a, c, b]
  elif n == 2:
    return [b, a, c]
  elif n == 3:
    return [b, c, a]
  elif n == 4:
    return [c, a, b]
  elif n == 5:
    return [c, b, a]

# Version 01
@profile
def main01():
  things = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  l = len(things)
  permut = []
  index = 1000000
  digit = 1
  while index > 0:
    if len(things) == 3:
      permut += order3(things[2], things[1], things[0], index-1)
      things = []
      break
    print "................"
    print "index: ", index
    tick = factorial(l-digit)
    print "tick: ", tick
    which = index/tick
    index = index%tick
    # what
    if index == 0:
      which -= 1
    print "which: ", which
    print "new index: ", index
    permut.append(things[-which-1])
    things.remove(things[-which-1])
    print "permut: ", permut
    print "things: ", things
    digit += 1
    print "digit: ", digit
  # Code here
  while things:
    permut.append(things.pop())
  printAnswer(reduce(lambda x, y: x + y, [str(x) for x in permut]))

main01()
