class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        # [6] [7] [8] ==> k=3, 끝에서 3번째 반환 = 3 - 3 = 0, 0 번째를 반환
        # [6] [7] [8] ==> k=2, 끝에서 2번째 반환 = 3 - 2 = 1, 0 1 번째를 반환
        # [6] [7] [8] ==> k=1, 끝에서 1번째 반환 = 3 - 1 = 2, 0 1 2 번째를 반환

        # node = Node(0)

        # count = 0
        # cur = self.head
        # while cur is not None:
        #     count += 1
        #     cur = cur.next
        
        # if count == k:
        #     return self.head
        # elif count > k:
        #     node = self.head
        #     for i in range(count - k):
        #         node = node.next
        # else:
        #     return False        

        # return node

        # 정답 (더 효율적인 방법)
        # 그런데, 길이를 전부 알아야만 할까요?

        # 2개의 포인터를 사용하면, 쉽게 해결할 수 있습니다!

        # k 만큼의 길이가 떨어진 포인터 두개를 두고, 한 칸씩 이동하면 어떨까요?
        # 언젠가 앞에 나선 포인터가 끝에 도달하게 됩니다.
        # 그 때 k 만큼 뒤떨어져있던 포인터는, 바로 끝에서부터 k 만큼 뒤떨어진 포인터가 됩니다!

        #              1   2  3 ....  k+1        끝
        # 시작   : ㅁ← k 만큼의 길이 → ㅁ  
        # 1단계 :      ㅁ← k 만큼의 길이 → ㅁ  
        # ....
        # 끝나면:                 ㅁ← k 만큼의 길이 → ㅁ 

        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow



linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(1).data)  # 7이 나와야 합니다!