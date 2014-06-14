from math import *
from util import *

#######################
# Project Euler #0030 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  digits = {}
  for i in xrange(10):
    digits[i] = i*i*i*i*i
  yay = []
  # arbitrary 1000000 upper limit, was correct
  for i in xrange(30, 1000000):
    d = getDigits(i)
    s = sum([digits[x] for x in d])
    if i == s:
      print i
      yay.append(i)      
  printAnswer(sum(yay))

main01()
