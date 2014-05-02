from math import *
from util import *

#######################
# Project Euler #0007 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

# Version 01
@profile
def main01():
  n = 200000
  primes = primesBelow(n)
  # Code here
  printAnswer(primes[10000])

main01()
