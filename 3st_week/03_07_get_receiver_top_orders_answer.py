# 레이저를 왼쪽으로 쏘고 있습니다.
# 자신의 위치보다 왼쪽에 있는 탑들을 하나 하나 보면서, 
# 자기보다 크다면 그 위치를 설정해주면 됩니다!

# 즉, 탑의 높이가 담긴 배열들을 stack 이라고 한다면, 
# 맨위의 값부터 하나하나 pop 하면서 원소들과 비교하는 방법입니다.

top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    
    answer = [0] * len(heights)

    while heights:
        height = heights.pop()
        
        print("탑높이", height)

        # len(heights)-1 부터, 0까지, -1씩 하는 for 문이다.
        for i in range(len(heights) - 1, -1, -1):
            print("i", i)
            print("heights[i]", heights[i])
            if height <= heights[i]:
                answer[len(heights)] = i + 1
                print("---------- 레이저 수신!! ---------")
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))


# Q. 여기서 퀴즈, 이 함수의 시간 복잡도는 얼마나 걸릴까요?

# 바로 $O(N^2)$ 만큼 걸립니다. 
# heights 의 길이만큼 while 문을 쓰는데, 내부에 for 문이 len(heights) 만큼 도니까,
# $O(N^2)$ 겠구나 생각해주시면 됩니다. 다른 계수는 다 버려버리자구요~!