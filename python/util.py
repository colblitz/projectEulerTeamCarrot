import math
import platform
if platform.system()=='Linux':
  from bitarray import bitarray

# Constants
pi = math.pi
e = math.e
sqrt2 = math.sqrt(2)
sqrt5 = math.sqrt(5)
phi = (1.0 + sqrt5) * 0.5
psi = 1.0 - phi

def printAnswer(s):
  print "##########   ANSWER   ##########"
  print ""
  print str(s)
  print ""
  print "################################"

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

def primeFactors(n):
  pass

def fibonacci(n):
  return int((phi**n - psi**n)/sqrt5)

def isPrime(n):
  pass

def lcd(a, b):
  pass

def lcd(*n):
  pass

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

