def get_prime_number(M, N):
    lst = []
    for i in range(M, N + 1):
        if i < 2:
            continue
        is_prime = True
        j = 2
        while j * j <= i:
            if i % j == 0:
                is_prime = False
                break
            j += 1
        if is_prime:
            lst.append(i)
    print('\n'.join(map(str, lst)))


M, N = map(int, input().split())
get_prime_number(M, N)
