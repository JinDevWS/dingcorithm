finding_target = 2
finding_numbers = [4, 3, 5, 0, 1, 2, 6]

def is_exist_target_number_binary(target, array):
    # 이 부분을 채워보세요!

    cur_min = 0
    cur_max = len(array) - 1
    cur_guess = (cur_min + cur_max) // 2

    temp = 0
    print("\rCurrent array: " + str(array), end="\n")
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            print("array[i]", array[i])
            print("array[j]", array[j])
            if array[i] > array[j]:
                print("체인지")
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
                print("array[i]", array[i])
                print("array[j]", array[j])
            print("-----------")
            print("\rCurrent array: " + str(array), end="")
            print("-----------")
    
    for item in array:
        print(array[item])

    while cur_min <= cur_max:
        if target == array[cur_guess]:
            return True
        elif target > array[cur_guess]:
            cur_min = cur_guess + 1
        elif target < array[cur_guess]:
            cur_max = cur_guess - 1
        cur_guess = (cur_min + cur_max) // 2
    
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)