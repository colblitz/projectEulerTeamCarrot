from math import *
from util import *

#######################
# Project Euler #0016 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  a = reduce(lambda x, y: int(x) + int(y), str(2**1000))
  printAnswer(a)

main01()
