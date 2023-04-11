# 입력 받기
binary_num = input()

# 앞에서부터 3자리씩 끊어서 8진수로 변환
binary_num = binary_num.zfill(len(binary_num) + (3 - len(binary_num) % 3) % 3)
octal_num = ""

for i in range(0, len(binary_num), 3):
    octal_digit = int(binary_num[i:i+3], 2)
    octal_num += str(octal_digit)

# 결과 출력
print(octal_num)