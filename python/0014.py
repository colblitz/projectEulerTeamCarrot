from math import *
from util import *

#######################
# Project Euler #0014 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

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
