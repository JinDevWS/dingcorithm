def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!

    # 0, 1을 만나면 +를 한다
    # 나머지는 곱한다
    is_plus = True
    total = 0
    for item in array:
        if item <= 1 or total <= 1:
            total += item
        else:
            total *= item

    return total


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))