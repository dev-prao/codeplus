from math import gcd

N, S = map(int, input().split())  # N : 동생 수, S : 수빈이의 위치
A_list = list(map(int, input().split()))  # A_list : 동생들의 위치
distance = []  # 수빈이와의 거리
for x in A_list:
    distance.append(abs(S - x))

if len(distance) == 1:
    x = distance[0]
else:
    x = gcd(distance[0], distance[1])
    for i in range(2, len(distance)):
        y = gcd(x, distance[i])
        x = y
print(x)
