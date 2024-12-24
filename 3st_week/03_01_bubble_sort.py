# 두 변수의 값을 교체 하려면 어떻게 할 수 있을까요?

# 다른 언어에서는 임시로 값을 저장해두는 변수를 따로 둬야 하지만, (예: temp 변수)
# 파이썬에서 되게 쉽게 할 수 있습니다!

# a, b = b, a 라고 작성하시면 됩니다!


input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

bubble_sort(input)
print(input)

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))


# 이것도 바로 $O(N^2)$ 만큼 걸립니다. 
# 함수 구문 하나하나를 보지 않더라도, 
# 2차 반복문이 나왔고, array 의 길이 만큼 반복한다? 
# 그러면 $O(N^2)$ 이겠구나! 생각해주시면 됩니다. 다른 계수는 다 버려버리자구요~!