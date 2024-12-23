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


def get_linked_list_sum(linked_list_1, linked_list_2):
    # 구현해보세요!

    zero_count1 = 0
    zero_count2 = 0
    linked_list_new1 = LinkedList(0)
    linked_list_new2 = LinkedList(0)
    sum = 0
    node1 = None
    node2 = None

    cur1 = linked_list_1.head
    while cur1 is not None:
        cur1 = cur1.next
        zero_count1 += 1

    cur2 = linked_list_2.head
    while cur2 is not None:
        cur2 = cur2.next
        zero_count2 += 1

    print("zero_count1", zero_count1)
    print("zero_count2", zero_count2)
    
    zero_count = 0
    if zero_count1 == zero_count2:
        zero_count = zero_count1
        node1 = linked_list_1.head
        node2 = linked_list_2.head

    elif zero_count1 > zero_count2:
        zero_count = zero_count1

        while (zero_count1 - 1) > zero_count2:
            linked_list_new2.append(0)
            zero_count1 -= 1

        node1 = linked_list_1.head

        cur = linked_list_new2.head
        last_node = None
        while cur is not None:
            last_node = cur
            cur = cur.next

        last_node.next = linked_list_2.head
        node2 = linked_list_new2.head

    elif zero_count1 < zero_count2:
        zero_count = zero_count2

        while (zero_count2 - 1) > zero_count1:
            linked_list_new1.append(0)
            zero_count2 -= 1

        cur = linked_list_new1.head
        last_node = None
        while cur is not None:
            last_node = cur
            cur = cur.next

        last_node.next = linked_list_1.head
        node1 = linked_list_new1.head

        node2 = linked_list_2.head
    
    digit = zero_count - 1
    while digit >= 0:
        print("digit", digit)
        print("node1.data", node1.data)
        print("node2.data", node2.data)
        sum = sum + ((node1.data + node2.data) * (10 ** digit))
        print((node1.data + node2.data))
        print((10 ** digit))
        print(((node1.data + node2.data) * (10 ** digit)))
        node1 = node1.next
        node2 = node2.next
        digit -= 1
        print(sum)

    return sum


linked_list_1 = LinkedList(6)
linked_list_1.append(0)
linked_list_1.append(8)
# linked_list_1.append(6)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)
linked_list_2.append(1)
linked_list_2.append(0)
linked_list_2.append(2)

print(get_linked_list_sum(linked_list_1, linked_list_2))
# print(6786 + 354)
print(608 + 354102)