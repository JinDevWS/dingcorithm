finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    # 정답

    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2
    print(current_min)
    print(current_max)
    print(current_guess)
    print("---------------")

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            print("업")
            current_min = current_guess + 1
        else:
            print("다운")
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

        print(current_min)
        print(current_max)
        print(current_guess)
        print("================")

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)