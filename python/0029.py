from math import *
from util import *

#######################
# Project Euler #0029 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  factorizations = set()
  for a in xrange(2, 101):
    f = primeFactors(a)
    for b in xrange(2, 101):
      nf = [[x[0], b*x[1]] for x in f]
      factorizations.add(listToTuples(nf))
  printAnswer(len(factorizations))

main01()
