
import math

def prime_test(n):
    is_prime = True
    for i in range(2, int(math.floor(math.sqrt(n))) + 1):
        if n % i == 0:
            is_prime = False
    return is_prime

primes_found = 1
i = 0

while primes_found < 10001:
    i += 1
    if prime_test(2 * i + 1) == True:
        primes_found += 1
        print str(primes_found) + ":  " + str(2 * i + 1)

print ""
print 2 * i + 1
