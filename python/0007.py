from math import *
from util import *

#######################
# Project Euler #0007 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  n = 200000
  primes = primesBelow(n)
  # Code here
  printAnswer(primes[10000])

main01()
