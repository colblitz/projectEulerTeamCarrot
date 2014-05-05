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
  answer = (999 + log10(sqrt(5))) / log10(phi)
  '''
  overflows lol

  def d(n):
    return floor(log(fibonacci(n)))

  i = 2
  j = 1
  # going up
  while True:
    if d(i) >= 1000:
      break
    j = i
    i *= 2
  # find
  while True:
    if i == j + 1:
      break
    m = (i+j)/2
    if d(m) >= 1000:
      i = m
    else:
      j = m

  # Code here
  '''
  printAnswer(answer)

main01()
