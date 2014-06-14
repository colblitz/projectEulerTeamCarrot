from math import *
from util import *

#######################
# Project Euler #0035 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  def rotate(n):
    s = str(n)
    return int(s[1:] + s[0])

  s = []
  primes = set(primesBelow(1000000)) 
  for p in primes:
    b = p
    keep = True
    for i in xrange(len(str(p))-1):
      b = rotate(b)
      if len(str(b)) < len(str(p)):
        keep = False
      if b not in primes:
        keep = False
    if keep:
      s.append(p)
  print s
  printAnswer(len(s))

main01()
