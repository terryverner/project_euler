# Multiples of 3 and 5
## Problem 1

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from functools import reduce

def multiples(threshold):
    seq = (i for i in range(threshold) \
            if i % 3 == 0 or i % 5 == 0)
    return sum(seq)

ceiling = int(input('Enter ceiling number >>> '))

print(f"Multiples of 3 and 5 below {ceiling}: {multiples(ceiling)}")
