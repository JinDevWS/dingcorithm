def find_max_num(array):
    # 이 부분을 채워보세요!

    # max_num = 0
    # for i in range(len(array)):
    #     if array[i] > max_num:
    #         max_num = array[i]
    #
    # return max_num

    max_num = array[0]
    for item in array:
        if item > max_num:
            max_num = item

    return max_num


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))