array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    # 이 부분을 채워보세요!

    cur_index_1 = 0
    cur_index_2 = 0
    len1 = len(array1)
    len2 = len(array2)
    merge_arr = []

    while cur_index_1 < len1 and cur_index_2 < len2:
        print(cur_index_1)
        print(cur_index_2)
        if array1[cur_index_1] < array2[cur_index_2]:
            merge_arr.append(array1[cur_index_1])
            cur_index_1 += 1
        else:
            merge_arr.append(array2[cur_index_2])
            cur_index_2 += 1
        print(cur_index_1)
        print(cur_index_2)
        print("-------------")
        print(merge_arr)
        print("-------------")

    
    if cur_index_1 < len(array1):
        for i in range(cur_index_1, len1):
            merge_arr.append(array1[i])
    
    if cur_index_2 < len(array2):
        for i in range(cur_index_2, len2):
            merge_arr.append(array2[i])

    return merge_arr


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))