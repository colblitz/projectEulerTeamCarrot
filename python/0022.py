from math import *
from util import *

#######################
# Project Euler #0022 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

# Version 01
@profile
def main01():
  f = open('files/0022-names.txt', 'r')
  names = []
  for line in f:
    s = line.replace("\"", "").split(',')
    for name in s:
      names.append(name)
  names = sorted(names)
  f.close()

  totalscore = 0
  for i in xrange(len(names)):
    position = i+1
    score = wordSum(names[i])
    totalscore += position * score

  printAnswer(totalscore)

main01()
