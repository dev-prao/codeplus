prime = [True] * 1000001
primes = []
for i in range(2, 1000001):
    if prime[i]:
        primes.append(i)
        j = i + i
        while j <= 1000000:
            prime[j] = False
            j += i

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for p in primes:
        if n - p >= 2 and n - p >= p:
            if prime[n-p] == True:
                ans += 1
        else:
            break
