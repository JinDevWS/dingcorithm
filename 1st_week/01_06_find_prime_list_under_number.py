input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!

    # 17을 17로 나누면 1이다
    # 3은 소수이다. 3은 2로 나누면 나머지가 1이다. 0으로 떨어지지 않으므로 소수다.
    # 4는 소수가 아니다. 4는 2로 나누었을 때 나머지가 0으로 딱 떨어진다.
    # 5는 소수이다. 2,3,4로 나누었을 때 나머지가 0으로 떨어지지 않는다.
    # 자신보다 더 작은 수로 나누었을 때, 한번이라도 0으로 떨어지면 소수가 아니다.
    is_prime = True
    prime_list = []
    for i in range(2, number + 1):
        is_prime = True
        for j in prime_list:
            if j * j <= i and i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)

    return prime_list


result = find_prime_list_under_number(input)
print(result)