import sys

n = int(sys.stdin.readline())
s = []
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        num = int(cmd[1])
        s.append(num)
    elif cmd[0] == 'top':
        if s:
            print(s[-1])
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(s))
    elif cmd[0] == 'empty':
        print(0 if s else 1)
    elif cmd == 'pop':
        if s:
            print(s.pop())
        else:
            print(-1)
