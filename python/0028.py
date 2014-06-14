from math import *
from util import *

#######################
# Project Euler #0028 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  sum = 1
  for i in xrange(3, 1003, 2):
    p = i - 2
    p2 = p*p
    i2 = i*i
    h = (p2+i2) / 2
    sum += i2 + 3*h
  printAnswer(sum)

main01()
