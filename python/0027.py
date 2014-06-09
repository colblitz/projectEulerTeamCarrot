from math import *
from util import *

#######################
# Project Euler #0027 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  # n^2 + an + b where |a| and |b| < 1000, find ab for ab with most consecutive primes starting with n = 0
  # b has to be prime, a + b + 1 has to be prime
  b = primesBelow(1000)
  primes = primesBelow(2000)
  b.extend([-x for x in b])
  pairs = []
  for i in xrange(-1000, 1000):
    for j in b:
      if (i + j + 1) in primes:
        pairs.append((i, j))
  allprimes = set(primesBelow(100000))
  n = 2
  while len(pairs) > 1:
    newpairs = []
    n2 = n**2
    for p in pairs:
      a = p[0]
      b = p[1]
      pp = n2 + a*n + b
      if pp in primes:
        newpairs.append(p)
    pairs = newpairs
    n += 1
  printAnswer(pairs[0])

main01()
