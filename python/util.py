import math
#import platform
#if platform.system()=='Linux':
from bitarray import bitarray
from string import *

# Constants
pi = math.pi
e = math.e
sqrt2 = math.sqrt(2)
sqrt5 = math.sqrt(5)
phi = (1.0 + sqrt5) * 0.5
psi = 1.0 - phi

letterToNumbers = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26}

numberToLetters = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z'}

def wordSum(s):
  return reduce(lambda x, y: x + y, [letterToNumbers[lower(c)] for c in s])

def printAnswer(s):
  print "##########   ANSWER   ##########"
  print ""
  print str(s)
  print ""
  print "################################"

def factorial(n):
  if n > 1:
    return n * factorial(n-1)
  return 1


def sumdigits(n):
  return reduce(lambda x, y: int(x) + int(y), str(n))

def primesBelow(n):
  # About 10s for n = 10000000
  ssize = int((n+1)/2.0)
  sieve = bitarray(ssize) # represents [1, 3, 5... ]
  sieve.setall(True)
  upper = int(math.sqrt(ssize) + 1)
  for i in xrange(1, upper):
    if sieve[i]:
      for j in xrange(i*2*(i+1), ssize, 2*i+1):
        sieve[j] = False
  primes = [2]
  for i in xrange(1, ssize):
    if sieve[i]:
      primes.append(2*i+1)
  return primes

'''
800x slower for n = 200000
def primesBelow(n):
  pprimes = range(2, n)
  primes = []
  while pprimes:
    p = pprimes.pop(0)
    pprimes = filter(lambda x: x % p != 0, pprimes)
    primes.append(p)
  return primes
'''

def properdivisors(n):
  candidates = range(1, int(math.sqrt(n)) + 1)
  lowdivisors = (d for d in candidates if n%d==0)
  divisors = []
  for d in lowdivisors:
    divisors.append(d)
    divisors.append(n/d)
  return sorted(filter(lambda x: x != n, list(set(divisors))))

def primeFactors(n):
  primes=primesBelow(n/2)
  factors = (f for f in primes if n%f==0)
  factorization = [(f, factorInto(n,f)) for f in factors]
  if factorization:
    return factorization
  return [(n,1)]

def factorInto(n,f):
  if n%f!=0:
    return 0
  return 1+factorInto(n/f,f)

def fibonacci(n):
  return int((phi**n - psi**n)/sqrt5)

def isPrime(n):
  primes=primesBelow(int(math.sqrt(n))+1)
  factors = (f for f in primes if n%f==0)
  try:
    next(factors)
  except StopIteration:
    return True
  return False

def lcd2(a, b):
  return a*b/gcf2(a,b)

def lcd(*n):
  return reduce(lambda x, y: lcd2(x, y), n)

def gcf2(m, n):
  a = m
  b = n
  while b != 0:
    t = b
    b = a % t
    a = t
  return a

def gcf(*n):
  return reduce(lambda x, y: gcf2(x, y), n)

