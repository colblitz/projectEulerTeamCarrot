from math import *
from util import *

#######################
# Project Euler #000x #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

# Version 01
@profile
def main01():
  primes = primesBelow(2000000)
  # Code here
  printAnswer(sum(primes))

main01()
