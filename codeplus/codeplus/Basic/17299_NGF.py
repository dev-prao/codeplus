import sys
from collections import Counter


def print_NGF(sequence):
    N = len(sequence)
    stack = []
    result = [-1] * N
    counter = Counter(sequence)  # 빈도수를 미리 계산하여 저장합니다.

    for i in range(N):
        while stack and counter[sequence[stack[-1]]] < counter[sequence[i]]:
            index = stack.pop()
            result[index] = sequence[i]
        stack.append(i)

    return result


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    sequence = list(map(int, input().split()))
    result = print_NGF(sequence)
    print(' '.join(map(str, result)))
