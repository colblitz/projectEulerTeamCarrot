import math
import util

#######################
# Project Euler #0004 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
#@profile
def main01():
  def isPalindrome(n):
    s = str(n)
    rs = s[::-1]
    if s == rs:
      return True
    return False
  
  largest = 0
  for i in xrange(100, 1000):
    for j in xrange(100, 1000):
      p = i*j
      if isPalindrome(p):
        largest = max(largest, p)

  # Code here
  util.printAnswer(largest)

# Version 02
#@profile
def main02():
  number = 600851475143
  palindromes = xrange(997,99,-1) # possible palindromes leftmost digits
  candidates = (n*1000+int(str(n)[::-1]) for n in palindromes)
  while candidates:
    #print candidates
    f = next(candidates)
    for i in xrange(999,99,-1):
      for j in xrange(999,99,-1):
        if i*j<=f:
          break
      if i*j==f:
        candidates=False
        break
  util.printAnswer(f)

main01()
main02()
