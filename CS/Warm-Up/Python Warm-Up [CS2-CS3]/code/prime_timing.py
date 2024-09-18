import math
from TimingProfiler import TimingProfiler

def is_prime_exhaustive(n: int) -> bool:
    if n <= 1:
        return False
    t = 0
    for i in range(2, n):
        if n%i == 0:
            t = t + 1
    if t > 0:
        return False
    else:
        return True

def is_prime_exhaustive_escape(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True 

def is_prime_skip_evens(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 ==  0:
        return False
    
    for i in range(3, n, 2):
        if n%i == 0:
            return False
    return True 

def is_prime_factor_fold(n: int) -> bool:
    if (n <= 1):
        return False
    if n == 2:
        return True
    if n % 2 ==  0:
        return False
    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    algorithms = [is_prime_exhaustive, is_prime_exhaustive_escape, is_prime_skip_evens, is_prime_factor_fold]
    test_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    # Verifying Correctness- is_prime
    for algorithm in algorithms:
        actual_primes = []
        for n in range(101):
            if algorithm(n):
                actual_primes.append(n)
        
        if test_primes == actual_primes:
            print(f"{algorithm.__name__} correctly finds primes < 100")
        else:
            print(f"{algorithm.__name__} has a mistake!!")
            print(f"  - Expected: {test_primes}")
            print(f"  - Actual: {actual_primes}")

    
    # Speed comparisons- is_prime
    inputs = [11, 101, 1009, 10007, 100003, 1000003, 10000019]
    trials = 10

    experiment = TimingProfiler(algorithms, inputs, trials)
    experiment.run_experiments()
    print(experiment.results)
    experiment.graph(title="is_prime Timings", scale="log")
    
