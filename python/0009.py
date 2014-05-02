from math import *
from util import *

#######################
# Project Euler #0009 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

# Version 01
@profile
def main01():
  # a = m^2 - n^2
  # b = 2mn
  # c = m^2 + n^2
  # with m > n
  # sum = 2m^2 + 2mn = 1000 ->
  # m^2 + mn = 500 
  for i in xrange(1, 25):
    if (500 - i*i) % i == 0 and i > (500 - i*i)/i:
      m = i
      n = (500 - m*m)/m
      a = m*m - n*n
      b = 2*m*n
      c = m*m + n*n
      print a, b, c
      printAnswer(a*b*c)
      break

main01()
