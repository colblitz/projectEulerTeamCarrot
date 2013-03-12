import math
import util

#######################
# Project Euler #0002 #
# Joseph Lee          #
# Benjamin Lee        #
#######################

# Version 01
@profile
def main01():
  sqrt5 = math.sqrt(5)
  phi = (1.0 + sqrt5) * 0.5
  psi = 1.0 - phi
  def f(n):
    # They start with 1, 2, so need to add two
    m = n + 2
    return int((phi**m - psi**m)/sqrt5)
  sum = 0

  # 34th fibonacci is 5702887, so with their index only go to 31
  for i in xrange(1,32,3):
    fib = f(i)
    if fib % 2 == 0:
      sum += fib
  util.printAnswer(sum)

main01()
