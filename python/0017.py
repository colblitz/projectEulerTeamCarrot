from math import *
from util import *

#######################
# Project Euler #000x #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  # Code here
  total = 0
  for i in xrange(1, 1001):
    print i, ": ", numberWord(i), "-", lettersForNumberWord(i)
    total += lettersForNumberWord(i)
    # x million, y thousand, z
    # 1-10 hundred and 1-19 | (20, 30, 40, etc) 1-10 
  printAnswer(total)

main01()
