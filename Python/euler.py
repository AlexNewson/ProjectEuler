import pandas as pd
from math import sqrt


def print_problem(problem_id):
    basic = pd.read_csv('https://projecteuler.net/minimal=problems',
                        sep='##',
                        engine='python')

    print("Promblem: ", problem_id)
    print("Title:    ", basic.loc[problem_id - 1]["Description"])
    print("URL:      ", "https://projecteuler.net/problem=" + str(problem_id))
    print("")


def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i//2]:
            sieve[i * i//2::i] = [False] * ((n - i * i - 1)//(2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n//2) if sieve[i]]


def is_prime(x):
    if x % 2 == 0:
        return False

    p = 3
    while p < sqrt(x)+1:
        if x % p == 0: return False
        p += 2
    return True


def nth_prime(n):
    prime = 2
    primes = 1
    number = 3
    while primes < n:
        if is_prime(number):
            prime = number
            primes += 1
        number += 1
    return prime


def is_pandigital(y):
    if len(y) == 9:
        x = []
        for i in y:
            if i == "0":
                return False
            elif i in x:
                return False
            x.append(i)
        return True
    else:
        return False


def generate_pentagonal(n):
    return int((n * (3 * n - 1)) / 2)


def is_pentagonal(x):
    return ((1+sqrt(1+24*x))/6).is_integer()


def generate_hexagonal(n):
    return int(n * (2 * n - 1))


def prime_factor_count(x):
    i = 2
    primes = set()
    while i < x ** 0.5 or x == 1:
        if x % i == 0:
            x = x / i
            primes.add(i)
            i -= 1
        i += 1
    return len(primes) + 1