finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    # 구현해보세요!

    arr_len = len(array)
    flag = arr_len // 2

    for number in range(arr_len):
        if target == number:
            return True
        
        # 이진 탐색
        # 1~ 16
        # 타겟이 16 // 2 보다 크면
        # 16 // 2 ~ 16
        # flag = 8~16 사이에서 1/2, 8 + ((16 - 8) // 2) 한 수

        # 타겟이 16 // 2 보다 작으면
        # 1 ~ 16 // 2
        # flag = 1 ~ 8 사이에서 1/2, 8 - ((16 - 8) // 2) 한 수

        if target > flag:
            number = flag
            flag = flag + ((arr_len - flag) // 2)
        elif target < flag:
            arr_len = flag 
            flag = flag - ((arr_len - flag) // 2)

        print("flag", flag)
        print("target", target)
        print("number", number)
        print("arr_len", arr_len)
        print("------------")

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)