def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!

    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    print("alphabet_occurrence_array is", alphabet_occurrence_array)

    max_occurrence = 0
    max_alphabet_index = 0

    for i in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[i]

        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = i

    return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))