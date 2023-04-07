import sys

def main():
    input = sys.stdin.readline
    test_case = int(input())
    for _ in range(test_case):
        repetition, string = input().split()
        repetition = int(repetition)
        result = ''
        for word in string:
            result += word * repetition
        print(result)

if __name__ == "__main__":
    main()