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
@profile
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

main01()
