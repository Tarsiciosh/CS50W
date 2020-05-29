import math

def is_prime(n):
    """Determines if a non-negative integer is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


""" # other option
import math

def is_prime(n):
  return n > 1 and all(n % i for i in range(2, int(math.sqrt(n)) + 1))
"""
