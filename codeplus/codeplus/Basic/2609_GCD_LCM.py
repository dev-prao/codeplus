def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b):
    ans = a * b // gcd(a, b)
    return ans


a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b))
