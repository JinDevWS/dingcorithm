input = "abcdcba"

def is_palindrome(string):
    # n = len(string)
    # for i in range(n):
    #     if string[i] != string[n - i - 1]:
    #         return False
    # return True

    if len(string) <= 1:
        return True
    # [-1]'은 뒤에서 첫 번째 데이터, '[-2]'는 뒤에서 두 번째를 의미합니다
    if string[0] != string[-1]:
        return False
    # string[1:-1]: 문자열을 자르겠다, 1부터 -1까지
    return is_palindrome(string[1:-1])

print(is_palindrome(input))