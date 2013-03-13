from math import *
from util import *
from numpy import prod

#######################
# Project Euler #0012 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  for n in xrange(100,100000): # no need to start small
    triangle=(n+1)*(n+2)/2
    factors1=primeFactors(n+1)
    factors2=primeFactors(n+2)
    divisors1=[j+1 for (i,j) in factors1 if i!=2]
    divisors2=[j+1 for (i,j) in factors2 if i!=2]
    divisors3=factorInto(triangle,2)+1
    numDivisors=prod(divisors1+divisors2+[divisors3])
    #print triangle,numDivisors
    if numDivisors>500:
      print n
      break
  printAnswer(triangle)
    
main01()
