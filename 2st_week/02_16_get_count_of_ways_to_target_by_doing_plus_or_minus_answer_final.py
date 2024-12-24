# 엇!! 그런데 result_count 가 0으로 찍힙니다!! 

# 왜일까요?
# 그 이유는 바로 파이썬의 Call by Object Reference  라는 개념 때문에 그렇습니다.

# 함수에서 파라미터로 배열을 넘기면 그 내부에 원소를 추가하거나 할 수 있는데
# 파라미터로 int, str 타입의 변수를 넘기면 그 값이 복제되어 새로운 값을 생성합니다.

# 따라서 함수 내부의 all_ways_count 만 변경이 되고,
# 함수 외부의 result_count 는 변하지 않아서 문제가 생깁니다!

# 이런 경우에는, 함수 외부의 변수를 사용하기 위해 
# 파이썬의 글로벌 변수라는 걸 사용하시면 됩니다!

# 외부에 정의되어 있는 변수를 내부에서 사용하기 위해서
# global 변수이름 이라고 쓰기만 하면 됩니다! 

# all_ways_count 파라미터는 안 쓰니까 지워주면 되겠죠~!


numbers = [2, 3, 1]
target_number = 0
result_count = 0  # target 을 달성할 수 있는 모든 방법의 수를 담기 위한 변수


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(array):  # 탈출조건!
        if current_sum == target:
            global result_count
            result_count += 1  # 마지막 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, 
                                                       target, 
                                                       current_index + 1,
                                                       current_sum + array[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, 
                                                       target, 
                                                       current_index + 1,
                                                       current_sum - array[current_index])


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)
# current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!
print(result_count)  # 2가 반환됩니다!