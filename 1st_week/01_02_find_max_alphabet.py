def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!

    max_count = 0
    max_char = string[0]
    for char in string:
        if char.isalpha():
            if string.count(char) > max_count:
                max_count = string.count(char)
                max_char = char

    return max_char


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))