# 큐라는 자료 구조에서 제공하는 기능은 다음과 같습니다!

# enqueue(data) : 맨 뒤에 데이터 추가하기 
# dequeue() : 맨 앞의 데이터 뽑기
# peek() : 맨 앞의 데이터 보기
# isEmpty(): 큐가 비었는지 안 비었는지 여부 반환해주기

# 한 번, 직접 구현해볼까요?

# 그 전에! 과연 큐는 뭘로 구현하면 좋을까요?
# 데이터 넣고 뽑는 걸 자주하는 자료 구조입니다!

# 그렇습니다. 스택과 마찬가지로 링크드 리스트와 유사하게 구현할 수 있습니다!
# 아래 코드를 기반으로 한 번 같이 구현해보겠습니다!

# 이 때, 스택과 다르게 큐는 끝과 시작의 노드를 전부 가지고 있어야 하므로,
# self.head 와 self.tail 을 가지고 시작합니다!

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # 어떻게 하면 될까요?

        # 우선, enqueue 라는 함수 먼저 볼게요.
        # 만약 현재 큐가 아래와 같다고 해봅시다.
        # queue = [4] → [2]
        # 큐에 3을 enqueue 하면 어떻게 되어야 할까요?
        # 놀이기구니까 제일 뒤에 있는 데이터가 3이 되어야 합니다.
        # 즉, [4] → [2] → [3] 가 되어야 합니다!
        # 그런데 이 때, head 와 tail 의 관점으로 봐야 합니다!
        # 어떻게 화살표를 이어줘야 할까요?
        # tail이 가리키는 Node의 next에 새롭게 추가되는 new_node를 연결해줘야 합니다!
        # 즉, tail.next = new_node 로 해줘야 합니다!
        # 그리고, tail을 새롭게 추가된 new_node로 옮겨줍니다! 
        
        # # 현재 [4] -> [2] 인 상태에서
        # new_node = Node(value)             # [3] 을 만들고
        # self.tail.next = new_node          # 현재 tail 인 [2] 의 다음을 [3] 으로 지정합니다.
        # self.tail = new_node		       # 그리고 tail을 [3] 으로 지정합니다.

        # 그러나, 이렇게 하면 에러가 발생합니다.
        # 바로, 초기 상태를 신경쓰지 않아서 그렇습니다!
        # 아무것도 큐에 들어가 있지 않은 상태라면,
        # head 와 tail 모두 None 입니다!
        # 그 상태에서 위의 코드로 queue.enqueue(3) 을 실행하면,
        # new_node = node(value) # [3] 을 만들고, 
        # self.tail.next = new_node # 여기서 문제가 생깁니다! self.tail 은 None 인데 next 를 하니까요!
        # 그래서, 빈 경우에는 예외적으로 처리를 해줘야 합니다.
        # [3] 은 head 이자 tail 이 되도록 설정해줘야 합니다.
        # 즉, 아래처럼 변경해주시면 됩니다.          
        new_node = Node(value)             
        if self.is_empty():                # 만약 비어있다면,
            self.head = new_node           # head 에 new_node를
            self.tail = new_node           # tail 에 new_node를 넣어준다.
            return

        self.tail.next = new_node          
        self.tail = new_node		           

        return

    def dequeue(self):
        # 어떻게 하면 될까요?

        # 이제 dequeue 이라는 함수를 구현해보겠습니다.
        # 만약 현재 큐가 아래와 같다고 해봅시다.
        # head             tail
        # [3] → [4] → [5]
        # 큐에 dequeue을 하면 어떻게 되어야 할까요?
        # 제일 앞에 있는 데이터인 [3]이 빠져야 합니다.
        # 즉, 다음과 같이 되어야 합니다.
        # head           tail
        # [4]       →    [5]
        # 즉, [4] 가 되어야 합니다!
        # 그러기 위해서는 head 에 [4] 를 지정하고, [3] 을 반환해주면 됩니다.
        # 즉, 현재 head 의 값을 다른 변수에 저장해 둔 다음,
        # head 가 지칭하는 노드를 현재 head 의 다음값으로 지정합니다.
        # 그리고 아까 저장해둔 head 를 반환해주면 됩니다!
        if self.is_empty():
            return "Queue is empty!"        # 만약 비어있다면 에러!

        delete_head = self.head             # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next          # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.

        return delete_head.data             # 그리고 제거할 node 반환

    def peek(self):
        # 어떻게 하면 될까요?
        # 만약 현재 큐가 아래와 같다고 해봅시다.
        # queue = [3] → [4]
        # 제일 위에 있는 노드를 주세요!
        # 그러면 head 를 반환해주기만 하면 됩니다 ㅎㅎ
        if self.is_empty():
            return "Queue is empty!"
    
        return self.head.data

    def is_empty(self):
        # 어떻게 하면 될까요?
        # 비어있는지 아닌지는 
        # linked_list 의
        # 제일 위에 있는 노드를 주세요!
        # 그러면 linked_list 의 head 를 반환해주기만 하면 됩니다 ㅎㅎ
        return self.head is None
    


# 여기서 잠깐! Tip
# Queue 를 실전에서 사용하려면?
# 여러분, 제가 큐를 파이썬에서 사용하기 위해서는 파이썬의 기본 자료형인 list() 를 사용하면 된다고 했었는데, 코딩테스트에서 큐를 사용할 때는 
# collections.deque 를 사용하셔야 합니다.
# 성능 차이가 많이 나거든요..! 스택은 그대로 list 사용하셔도 됩니다.

# 따라서 앞으로는 큐가 필요할 때 다음과 같이 사용하겠습니다!
# >>> from collections import deque
# >>> queue = deque()
# >>> queue.append(3) # enqueue [3]
# >>> queue.append(4) # enqueue [3] -> [4]
# >>> print(queue.popleft()) # dequeue [4]
# 3