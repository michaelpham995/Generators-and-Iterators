import math

def factorial_recursive(n):
    if n < 2:
        return 1
    return n * factorial_recursive(n - 1)


for i in range(1, 11):
    print(factorial_recursive(i))


def factorial_range_reduce(n):
    assert n >= 0
    return reduce(mul, range(1, n + 1), 1)

    #1 at the end is the seed

    #Reduce - Highe rorder function
    # 1 mul 1 = 1
    # 1 mul 2 = 2
    # 2 mul 3 = 6


#Prime:     p > 1 and can only be divided by 1 and p 


def is_prime(n):
    if n < 2:
        return False
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
   

for i in range(1, 11):
    print(is_prime(i))

def is_prime_2(n):
    assert n > 0
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

for i in range(1, 11):
    print(is_prime_2(i))
