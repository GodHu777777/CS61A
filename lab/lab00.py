def twenty_twenty():
    """Come up with the most creative expression that evaluates to 2020,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty()
    2020
    """
    return 2000 + 20

def fib(n):
    k = 0
    pred,curr = 1,0
    while k < n:
        k += 1
        pred,curr = curr,pred+curr
    return curr

def end(n,d):
    while n % 10 != d:
        print(n % 10)
        n //= 10
    print(d)
