from math import *
from util import *

#######################
# Project Euler #0037 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  a = []
  # arbitrary upper limit, correct
  primes = set(primesBelow(1000000))
  for p in primes:
    if p in [2, 3, 5, 7]:
      continue
    keep = True
    s = str(p)
    for i in xrange(1, len(s)):
      tl = int(s[i:])
      tr = int(s[:i])
      if tl not in primes or tr not in primes:
        keep = False
        break
    if keep:
      print p
      a.append(p)
  # Code here
  printAnswer(sum(a))

main01()
