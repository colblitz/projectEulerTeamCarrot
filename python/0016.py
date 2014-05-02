from math import *
from util import *

#######################
# Project Euler #0016 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

# Version 01
@profile
def main01():
  a = reduce(lambda x, y: int(x) + int(y), str(2**1000))
  printAnswer(a)

main01()
