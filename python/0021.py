from math import *
from util import *

#######################
# Project Euler #0021 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  num = 10000
  dsums = {}
  for n in xrange(1, num+1):
    dsums[n] = sum(properdivisors(n))
  amicable = set()
  for n in xrange(1, num+1):
    if dsums[n] in dsums and n == dsums[dsums[n]] and dsums[n] != n:
      amicable.add(n)
      amicable.add(dsums[n])
  print list(amicable)
  printAnswer(sum(list(amicable)))

main01()
