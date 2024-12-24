# 그런데 저희는 모든 경우의 수를 구하는 것이 아니라,
# 모든 경우의 수가 target 과 일치하는지! 를 알고 싶은 거죠?
# 그래서 다음과 같이 코드를 변경합니다.

# target 을 파라미터에 추가적으로 받아주고, all_ways 가 아니라 all_ways_count 를 알아야 하기 때문에 이렇게 변경합니다! 

numbers = [2, 3, 1]
target_number = 0
result_count = 0  # target 을 달성할 수 있는 모든 방법의 수를 담기 위한 변수


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum, all_ways_count):
    if current_index == len(array):  # 탈출조건!
        if current_sum == target:
            all_ways_count += 1  # 마지막 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, 
                                                       target, 
                                                       current_index + 1,
                                                       current_sum + array[current_index],
                                                       all_ways_count)
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, 
                                                       target, 
                                                       current_index + 1,
                                                       current_sum - array[current_index],
                                                       all_ways_count)


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0, result_count)
# current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!
print(result_count)