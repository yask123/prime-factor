import math
primes=[]

def isPrime(num):
  global primes
  for i in range(2,int(math.sqrt(num))+1):
      if num % i ==0:
          return False
  primes.append(num)
  return True  

for num in range(2,1000000):
  isPrime(num)
l=0
start=0
s=0
maxx=0
term=0



for p in range(len(primes)):

  start=0
  s_p=0
  s=0
  l=0
  while primes[s_p] < primes[p]:# Could be made better


      if s == primes[p]:
          #Success
          if maxx < l:
              term=primes[p]
              maxx=l
          break
      elif s > primes[p]:
          #Failed
          #Restart with next term

          start=start+1
          s_p = start
          l=0
          s=0
      else :
          s=s+primes[s_p]
          s_p=s_p+1
          l=l+1
print (maxx)          
print (term)