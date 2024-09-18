import math
def contains_the_same(a: int, b: int):
    list_of_digits1 = []
    list_of_digits2 = []
    while (a > 0):
        list_of_digits1.append(a % 10)
        a = a//10
    while (b > 0):
        list_of_digits2.append(b % 10)
        b = b//10
    return sorted(list_of_digits1) == sorted(list_of_digits2) 
def PermutedMultiples():
    i = 1
    while True:
        if contains_the_same(i, 2*i) and contains_the_same(i, 3*i) and contains_the_same(i, 4*i) and contains_the_same(i, 5*i) and contains_the_same(i, 6*i):
            print(i)
            return 
        i += 1

def is_prime(n: int) -> bool:
    if (n <= 1) or (n % 1 != 0):
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

def prime_permutations():
    list_of_all_primes = []
    for i in range(1000, 10000):
        if is_prime(i):
            list_of_all_primes.append(i)
    for i in list_of_all_primes:
        for j in range(1, 5000):
            if ((i + j) in list_of_all_primes) and ((i + 2*j) in list_of_all_primes) and (contains_the_same(i, i+j)) and  (contains_the_same(i, i+2*j)):
                print(i, i+j, i+2*j)

prime_permutations()


                   