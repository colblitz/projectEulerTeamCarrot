from math import *
from util import *

#######################
# Project Euler #0031 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  coins = [1, 2, 5, 10, 20, 50, 100, 200]
  # much better, 0.01 s
  memoize = {}
  def ways(n, k):
    if (n, k) in memoize:
      return memoize[(n, k)]
    if n < 0 or k < 1:
      return 0
    elif n == 0:
      return 1
    w = ways(n, k-1) + ways(n-coins[k-1], k)
    memoize[(n, k)] = w
    return w


  # This is 5 minutes, still not the best
  # coinr = {}
  # for i in xrange(8):
  #   coinr[coins[i]] = str(i)
  # ways = {}
  # ways[1] = set()
  # ways[1].add("0")
  # for i in xrange(2, 201):
  #   w = set()
  #   for c in coins:
  #     if i > c:
  #       for x in ways[i-c]:
  #         w.add(reduce(lambda x, y: x + y, sorted(x + coinr[c])))
  #     if i == c:
  #       w.add(coinr[c])
  #   ways[i] = w
 

  # This took 20 minutes, horrible
  # ways = {}
  # ways[1] = set()
  # ways[1].add((1, 0))
  # for i in xrange(2, 201):
  #   w = set()
  #   for c in coins:
  #     if i > c:
  #       old = set()
  #       old.update([sortTuple(listToTuples(list(x) + [c])) for x in ways[i-c]])
  #       w = w.union(old)
  #    if i == c:
  #      w.add((c, 0))
  #  ways[i] = w
  printAnswer(ways(200, 8))

main01()
