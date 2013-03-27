from math import *
from util import *

#######################
# Project Euler #0015 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  size = 21
  grid = [[0]*size for i in xrange(size)]
  grid[0][0] = 1
  # For each diagonal
  for d in xrange(1, size*2 - 1):
    width = d + 1
    if d >= size:
      width = 2*size - d - 1
    for j in xrange(width):
      if d < size:
        x = j
      else:
        x = d + j + 1 - size
      y = d - x
      value = 0
      if ( x > 0 ):
        value += grid[x - 1][y]
      if ( y > 0 ):
        value += grid[x][y - 1]
      grid[x][y] = value

  # Code here
  printAnswer(grid[size-1][size-1])

main01()
