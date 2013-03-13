import math
import util

#######################
# Project Euler #0006 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  hundred = range(1, 101)
  squares = map(lambda x: x*x, hundred)
  sumhundred = sum(hundred)
  sumsquares = sum(squares)
  # Code here
  util.printAnswer(sumhundred*sumhundred - sumsquares)

main01()
