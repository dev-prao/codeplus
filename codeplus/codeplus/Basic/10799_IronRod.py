def main():  # 메인 함수를 정의합니다.
    a = input().strip()  # 사용자로부터 입력을 받아 공백을 제거합니다.
    n = len(a)  # 입력받은 문자열의 길이를 구합니다.
    s = []  # 괄호의 stack를 저장할 stack을 초기화합니다.
    ans = 0  # 정답을 저장할 변수를 초기화합니다.

    for i in range(n):  # 문자열의 길이만큼 반복합니다.
        c = a[i]  # i번째 문자를 가져옵니다.

        if c == '(':  # 여는 괄호인 경우
            s.append(i)  # stack에 index를 추가합니다.
        else:  # 닫는 괄호인 경우
            if s[-1] + 1 == i:  # 직전 문자가 여는 괄호인 경우
                s.pop()  # stack에서 꺼냅니다.
                ans += len(s)  # 현재 stack의 길이를 정답에 더합니다.
            else:  # 직전 문자가 닫는 괄호인 경우
                s.pop()  # stack에서 꺼냅니다.
                ans += 1  # 정답에 1을 더합니다.

    print(ans)  # 최종 정답을 출력합니다.

if __name__ == "__main__":
    main()  # 메인 함수를 실행합니다.