from math import *
from util import *

#######################
# Project Euler #0032 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  d1 = [2, 3, 4, 6, 7, 8, 9]
  d2 = []
  d3 = []
  d4 = []
  for i in xrange(10, 100):
    dd1 = i%10
    dd2 = (i/10)%10
    if dd1 in d1 and dd2 != dd1:
      d2.append(i)
  for i in xrange(100, 1000):
    dd1 = i%10
    dd2 = (i/10)%10
    dd3 = (i/100)%10
    if dd1 in d1 and dd2 != dd1 and dd3 != dd1 and dd3 != dd2 and dd2 != 0:
      d3.append(i)
  for i in xrange(1000, 5000):
    dd1 = i%10
    dd2 = (i/10)%10
    dd3 = (i/100)%10
    dd4 = (i/1000)%10
    if dd1 in d1 and dd2 != dd1 and dd3 != dd1 and dd3 != dd2 and dd4 != dd1 and dd4 != dd2 and dd4 != dd3 and dd2 != 0 and dd3 != 0:
      d4.append(i)

  def isPandigital(a, b, c):
    alls = str(a) + str(b) + str(c)
    digits = set()
    for d in list(str(a) + str(b) + str(c)):
      digits.add(d)
    return len(digits) == 9 and not "0" in digits and len(alls) == 9

  s = set()
  for i in d1:
    for j in d4:
      if isPandigital(i, j, i*j):
        print i, j, i*j
        s.add(i*j)
  for i in d2:
    for j in d3:
      if isPandigital(i, j, i*j):
        print i, j, i*j
        s.add(i*j)

  # Code here
  printAnswer(sum(list(s)))

main01()
