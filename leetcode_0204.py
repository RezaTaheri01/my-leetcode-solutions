# Caching + Exclude even numbers
class Solution0: # Problem: Time Limit Exceeded
    def __init__(self):
        self.cache = {}
        
    def countPrimes(self, n: int) -> int:
        def isPrime(num) -> bool:            
            for div in range(2, int(num ** 0.5) + 1):
                if num % div == 0:
                    self.cache[num] = 0
                    return False
            self.cache[num] = 1
            return True
        
        c = 1 if n > 2 else 0
        for number in range(3, n, 2):  # exclude even numbers
            if number in self.cache:
                c += self.cache[number]
            elif isPrime(number):
                c += 1
                
        return c
    
          
import numpy as np 
        
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: # n is exclusive(not included) 
            return 0

        #  A bool uses the same amount of space as a int8
        prime = np.ones(n, dtype=np.bool_)
        prime[0], prime[1] = 0, 0
        p = 2
        
        # Sieve of Eratosthenes algorithm
        while p * p <= n:
            if prime[p]:      
                # Mark all multiples of p as non-prime
                # for i in range(p * p, n, p):
                #     prime[i] = False
                prime[p * p:n:p] = False # Much faster
            p += 1
            
        return np.count_nonzero(prime)
        # return np.sum(prime)
                        
                           
s = Solution()

print(s.countPrimes(10))
print(s.countPrimes(10**2))
print(s.countPrimes(10**4))
print(s.countPrimes(10**5))
print(s.countPrimes(10**6))
