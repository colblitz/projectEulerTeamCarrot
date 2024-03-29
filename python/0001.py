import math
import util

#######################
# Project Euler #0001 #
# Joseph Lee          #
# Benjamin Lee        #
#######################

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

# Version 01
@profile
def main01():
  sum = 0
  for i in xrange(1000):
    if i % 3 == 0 or i % 5 == 0:
      sum += i
  util.printAnswer(sum)

main01()

# Addendum:
# Multiples of 3 range from 3 to 999
# (3+999)+(6+996)+...+(498+504)+(501)=(498/3*2+1)*501=166833
# Multiples of 5 range from 5 to 995
# (5+995)+(10+990)+...+(495+505)+(500)=(495/5*2+1)*500=99500
# Multiples of 15 range from 15 to 990
# (15+990)+(30+975)+...+(495+510)=(495/15)*1005=33165
# Answer = 166833+99500-33165 = 233168


