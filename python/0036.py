from math import *
from util import *

#######################
# Project Euler #0036 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  a = []
  for i in xrange(1, 1000001):
    if isPalindrome(str(i)) and isPalindrome(bin(i)[2:]):
      print i, bin(i)
      a.append(i)
  # Code here
  printAnswer(sum(a))

main01()
