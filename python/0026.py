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
  l = 0
  lp = 0
  for i in xrange(1, 1001):
    p = periodOfReciprocal(i)
    if p > lp:
      lp = p
      l = i

  # if p is prime, period is order of 10 modulo p - if 10 is primitive root modulo p, period is p-1
  # if p is composite and coprime to 10
  # 1/p^k*q^l, etc has period lcm(p^k, q^l, etc) - 1/p^k usually p^(k-1)T_p, except 3, 487, 56598313, which = 1/p
  # composite not co prime to 10 - remove 2 and 5, then continue
  # Code here
  printAnswer(l)

main01()
