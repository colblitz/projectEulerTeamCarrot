from math import *
from util import *

#######################
# Project Euler #000x #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  f = {}
  a = []
  for i in xrange(10):
    f[i] = factorial(i)
  # arbitrary upper limit, was right
  for i in xrange(3, 1000000):
    di = getDigits(i)
    s = 0
    for d in di:
      s += f[d]
    if s == i:
      a.append(i)
  print a
  # Code here
  printAnswer(sum(a))

main01()
