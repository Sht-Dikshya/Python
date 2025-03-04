import math 

def nth_root(value, n):
    if value < 0 and n% 2 ==0:
        raise ValueError("Cannot compute the even root of a negative")
    return value ** (1 / n)