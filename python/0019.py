from math import *
from util import *
import datetime

#######################
# Project Euler #000x #
# Team Carrot:        #
# Joseph Lee          #
# Benjamin Lee        #
# Stephanie Yu        #
#######################

'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

# Version 01
@profile
def main01():
  date = datetime.datetime(1901, 1, 1)
  end = datetime.datetime(2000, 12, 31)
  total = 0
  while date <= end:
    if date.weekday() == 6 and date.day == 1:
      total += 1
    date += datetime.timedelta(days=1)
  printAnswer(total)

main01()
