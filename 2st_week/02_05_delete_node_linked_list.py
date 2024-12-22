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
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        prev_node = self.get_node(index - 1)
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        # delete_node = self.get_node(index)
        # if index == 0:
        #     self.head = delete_node.next
        #     return
        
        # prev_node = self.get_node(index - 1)
        # next_node = delete_node.next
        # prev_node.next = next_node

        # 정답
        if index == 0:
            self.head = self.head.next
        
        prev_node = self.get_node(index - 1)
        index_node = self.get_node(index)
        prev_node.next = index_node.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(13)
linked_list.append(14)
linked_list.add_node(1, 3)
linked_list.print_all()
linked_list.delete_node(3)
linked_list.print_all()