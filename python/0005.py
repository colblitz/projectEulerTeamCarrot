import math
import util

#######################
# Project Euler #0005 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  # Code here
  # 20 = 2^2 * 5
  # 19 = 19
  # 18 = 2 * 3^2
  # 17 = 17
  # 16 = 2^4
  # 15 = 3 * 5
  # 14 = 2 * 7
  # 13 = 13
  # 12 = 2^2 * 3
  # 11 = 11
  # 10 = 2 * 5
  # 9 = 3^2
  # 8 = 2^3
  # 7 = 7
  # 6 = 2 * 3
  # 5 = 5
  # 4 = 2^2
  # 3 = 3
  # 2 = 2
  # 1 = 1
  # answer = 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19
  util.printAnswer(2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19)

main01()
