import math
import util

#######################
# Project Euler #0003 #
# Joseph Lee          #
# Benjamin Lee        #
#######################


'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

# Version 01
@profile
def main01():
  number = 600851475143
  pfactors = range(2, int(math.sqrt(number)))
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

# Version 02
@profile
def main02():
  number = 600851475143
  pfactors = range(2, int(math.sqrt(number)))
  factors = []
  while pfactors:
    f = pfactors[0]
    if number % f == 0:
      number = number/f
      factors.append(f)
      del pfactors[0]
      #pfactors = pfactors[1:]
      pfactors = [x for x in pfactors if x < int(math.sqrt(number))+1]
    else:
      pfactors = [x for x in pfactors if x % f != 0]
  factors.append(number)
  util.printAnswer(factors[-1])

# Version 03
@profile
def main03():
  number = 600851475143
  pfactors = range(2, int(math.sqrt(number)))
  factors = []
  while pfactors:
    f = pfactors[0]
    if number % f == 0:
      number = number/f
      factors.append(f)
      del pfactors[0]
      #pfactors = pfactors[1:]
      a = int(math.sqrt(number))+1
      pfactors = filter(lambda x: x < a, pfactors)
      #pfactors = [x for x in pfactors if x < int(math.sqrt(number))+1]
    else:
      pfactors = filter(lambda x: x % f != 0, pfactors)
      #pfactors = [x for x in pfactors if x % f != 0]
  factors.append(number)
  util.printAnswer(factors[-1])

#main01() # 23.5 s
#main02() # 23.5 s
main03() # 2.28 s
