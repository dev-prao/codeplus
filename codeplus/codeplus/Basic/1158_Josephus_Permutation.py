from collections import deque

n, k = map(int, input().split())  # N은 총 사람 수, K번째 사람 제거
q = deque()
for i in range(1, n + 1):
    q.append(i)
ans = []
for i in range(n - 1):
    for j in range(k - 1):
        q.append(q.popleft())
    ans += [q.popleft()]

ans += [q[0]]
print('<' + ', '.join(map(str, ans)) + '>')