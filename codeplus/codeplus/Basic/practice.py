import sys


def eratosthenes_sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime = False
    return is_prime


def goldbach_conjecture(n, primes, prime_list):
    for a in prime_list:
        if a > n // 2:
            break
        if primes[n - a]:
            return a, n - a


if __name__ == "__main__":
    max_n = 1000000
    primes = eratosthenes_sieve(max_n)
    prime_list = [i for i in range(3, max_n + 1, 2) if primes[i]]

    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break

        a, b = goldbach_conjecture(n, primes, prime_list)
        if a and b:
            print(f"{n} = {a} + {b}")
        else:
            print("Goldbach's conjecture is wrong.")
