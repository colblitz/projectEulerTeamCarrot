from math import *
from util import *

#######################
# Project Euler #0022 #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

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
