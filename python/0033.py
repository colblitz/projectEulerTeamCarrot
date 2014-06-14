from math import *
from util import *

#######################
# Project Euler #0033 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():

  def div(a, b, c, d, t):
    if c != d or c == 0 or d == 0:
      return False
    if a == 0 or b == 0:
      return False
    return a/b == t

  d2 = range(10, 100)
  f = []
  for i in d2:
    for j in d2:
      if i >= j:
        continue
      dec = float(i)/float(j)
      idigits = getDigits(i)
      jdigits = getDigits(j)
      i1 = float(idigits[0])
      i2 = float(idigits[1])
      j1 = float(jdigits[0])
      j2 = float(jdigits[1])
      if div(i1, j1, i2, j2, dec) or div(i1, j2, i2, j1, dec) or div(i2, j1, i1, j2, dec) or div(i2, j2, i1, j1, dec):
        f.append((i, j))
  
  n = 1
  d = 1
  for fr in f:
    n *= fr[0]
    d *= fr[1]
  s = (d/gcf(n, d))
  printAnswer(s)

main01()
