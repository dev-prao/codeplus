def to_negative_binary(n):
    if n == 0:
        return '0'
    res = ''
    while n != 0:
        remainder = n % (-2)
        n //= -2
        if remainder < 0:
            remainder += 2
            n += 1
        res = str(remainder) + res
    return res

n = int(input())
print(to_negative_binary(n))