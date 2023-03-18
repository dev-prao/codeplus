import sys

t = int(sys.stdin.readline())
for _ in range(t):
    s = sys.stdin.readline()
    stack = []
    for w in s:
        if w == ' ' or w == '\n':
            print(''.join(stack[::-1]), end='')
            stack.clear()
            print(w, end='')
        else:
            stack.append(w)