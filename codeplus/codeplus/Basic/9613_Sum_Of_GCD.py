def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


t = int(input())

for _ in range(t):
    lst = []
    cmd = list(map(int, input().split()))
    for i in range(1, cmd[0]):
        for j in range(i + 1, cmd[0] + 1):
            lst.append(gcd(cmd[i], cmd[j]))
    print(sum(lst))