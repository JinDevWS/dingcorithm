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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        # cur = self.get_node(index)
        # next = cur.next

        # node_tail = LinkedList(value)
        # while next is not None:
        #     node_tail.append(next.data)
        #     next = next.next
        
        # self.get_node(index).next = node_tail.head

        # 정답
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        prev_node = self.get_node(index - 1)
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.next = next_node


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(13)
linked_list.append(14)
linked_list.add_node(1, 3)
linked_list.print_all()