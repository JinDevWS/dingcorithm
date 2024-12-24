class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 우선, push 라는 함수 먼저 볼게요.
# 만약 현재 스택이 아래와 같다고 해봅시다.
# stack = [4] 
# 스택에 3을 push 하면 어떻게 되어야 할까요?
# 빨래통이니까 제일 위에 있는 데이터가 3이 되어야 합니다.
# 즉, [3] → [4] 가 되어야 합니다!
# 링크드 리스트에서 새로운 head를 지정하려면,
# 새로운 값을 담은 새로운 노드를 만들고,
# 그 노드의 다음 노드를 현재의 head 로 지정하고,
# 그 노드를 head 로 정하면 됩니다! 다음과 같이요!
def push(self, value):                 # 현재 [4] 밖에 없다면
    new_head = Node(value)             # [3] 을 만들고!
    new_head.next = self.head          # [3] -> [4] 로 만든다음에
    self.head = new_head               # 현재 head의 값을 [3] 으로 바꿔준다.

# 이제 pop 이라는 함수를 구현해보겠습니다.
# 만약 현재 스택이 아래와 같다고 해봅시다.
# stack = [3] → [4]
# 스택에 pop을 하면 어떻게 되어야 할까요?
# 제일 위에 있는 데이터인 3이 빠져야 합니다.
# 즉, [4] 가 되어야 합니다!
# 링크드 리스트에서 head 를 제거하려면,
# 현재 head 의 값을 다른 변수에 저장해 둔 다음,
# head 가 지칭하는 노드를 현재 head 의 다음값으로 지정합니다.
# 그리고 아까 저장해둔 head 를 반환해주면 됩니다!
def pop(self):
    if self.is_empty():                  # 만약 비어있다면 에러!
        return "Stack is empty!"
    delete_head = self.head              # 제거할 node 를 변수에 잡습니다.
    self.head = self.head.next           # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.
    return delete_head                   # 그리고 제거할 node 반환

# 이제 peek 이라는 함수를 구현해보겠습니다.
# 되게 쉽습니다!
# 만약 현재 스택이 아래와 같다고 해봅시다.
# stack = [3] → [4]
# 제일 위에 있는 노드를 주세요!
# 그러면 head 를 반환해주기만 하면 됩니다 ㅎㅎ
def peek(self):
    if self.is_empty():
        return "Stack is empty!"

    return self.head.data

# 이제 is_empty 이라는 함수를 구현해보겠습니다.
# 비어있는지 아닌지는 
# head 가 None 인지 아닌지 여부를 반환하면 됩니다!
def is_empty(self):
    return self.head is None


# 여기서 잠깐! Tip
# 스택 실전 사용법
# 위에서 스택을 구현해봤지만, 실제 코드에서는 파이썬의 list 를 이용해서 스택으로 사용합니다!
stack = []            # 빈 스택 초기화
stack.append(4)       # 스택 push(4)
stack.append(3)       # 스택 push(3)
top = stack.pop()     # 스택 pop
print(top)            # 3