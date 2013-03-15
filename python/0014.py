from math import *
from util import *

#######################
# Project Euler #0014 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  lengths = {}
  lengths[1] = 0
  def collatz(n):
    a = n
    steps = 0
    while a != 1:
      if a in lengths:
        steps += lengths[a]
        a = 1
      else:
        if a % 2 == 0:
          a = a/2
        else:
          a = 3*a + 1
        steps += 1
    lengths[n] = steps

  for i in xrange(2, 1000000):
    collatz(i)
  longest = max(lengths, key=lambda x: lengths[x])

  # Code here
  printAnswer(longest)

main01()
