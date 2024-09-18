import math

def get_factors(n: int) -> list[int]:
    if (n <= 0) or (n % 1 != 0):
        return []
    list = [1]
    if n == 1:
        return list
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            list = list + [i]
    size = len(list)
    if((math.ceil(math.sqrt(n)))**2 == n):
        list = list + [math.ceil(math.sqrt(n))]
    for i in range(size-1, -1, -1):
        list = list + [int(n/list[i])]
    return list


def is_prime(n: int) -> bool:
    if (n <= 1) or (n % 1 != 0):
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True


def largest_prime_factor(n: int) -> int:
    if (n <= 1) or (n % 1 != 0):
        return 0
    list = get_factors(n)
    for i in range(len(list)-1, 0, -1):
        if is_prime(list[i]):
            return list[i]

if __name__ == "__main__":
    print("get_factors(25): ", get_factors(1))
    print("is_prime(17): ", is_prime(17))
    print("largest_prime_factor(35): ", largest_prime_factor(35))