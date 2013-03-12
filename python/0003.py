import math
import util

#######################
# Project Euler #0003 #
# Joseph Lee          #
# Benjamin Lee        #
#######################

# Version 01
@profile
def main01():
  number = 600851475143
  pfactors = xrange(2, int(math.sqrt(number)))
  factors = []
  while pfactors:
    f = pfactors[0]
    if number % f == 0:
      number = number/f
      factors.append(f)
      pfactors = pfactors[1:]
      pfactors = [x for x in pfactors if x < int(math.sqrt(number))+1]
    else:
      pfactors = [x for x in pfactors if x % f != 0]
  factors.append(number)
  util.printAnswer(factors[-1])

main01()
