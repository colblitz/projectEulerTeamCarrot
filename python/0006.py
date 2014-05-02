import math
import util

#######################
# Project Euler #0006 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

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
