# Question 3 - Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import ceil
from pprint import pprint
from itertools import count

def gen_primes(value):
    # Incremental Sieve of Erastothenes
    D = {} # Dictionary of non-primes and their composites
    for q in range(2, ceil(value/2)):
        if q not in D:
            yield q 
            # Square of q added into dictionary of non-primes, with the prime
            # included as the composite
            D[q * q] = [q] 
        else:
            for p in D[q]:
                # Sum of non-prime and it's composite added to dictionary
                # added to dictionary
                D.setdefault(p + q, []).append(p) 
            
            # Since q is already checked, it's no longer needed
            del D[q]

def main(value):
    dividend = value
    composites = set()
    for prime in gen_primes(value):
        if dividend % prime == 0:
            composites.add(prime)            

            while dividend % prime == 0:
                dividend /= prime

            if dividend == 1:
                break
    return composites

if __name__ == "__main__":
    print(main(12))
    print(main(600851475143))