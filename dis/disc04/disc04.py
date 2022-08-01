# 1.1 Write a function that takes two numbers m and n and returns their product.
# Assume m and n are positive integers. Use recursion, not mul or *!
# Hint: 5*3 = 5 + 5*2 = 5 + 5 + 5*1.

def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)