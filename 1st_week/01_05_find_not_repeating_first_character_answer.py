def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        alphabet_occurrence_array[ord(char) - ord('a')] += 1

    not_repeat_chars = []
    for i in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[i] == 0:
            continue
        if alphabet_occurrence_array[i] == 1:
            not_repeat_chars.append(chr(ord('a') + i))

    for char in string:
        if char in not_repeat_chars:
            return char

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))