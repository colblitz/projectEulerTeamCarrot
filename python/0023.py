from math import *
from util import *

#######################
# Project Euler #000x #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

# Version 01
@profile
def main01():
  # Code here
  total = 0
  abundant = []
  for i in xrange(28125):
    if sum(properdivisors(i)) > i:
      abundant.append(i)
  sum_abundant = set()
  l = len(abundant)
  print l
  for i in xrange(l):
    for j in xrange(i, l):
      if abundant[i] + abundant[j] > 28125:
        break
      sum_abundant.add(abundant[i] + abundant[j])
  print len(sum_abundant)
  for i in xrange(28124):
    if i not in sum_abundant:
      total += i

  printAnswer(total)

main01()
