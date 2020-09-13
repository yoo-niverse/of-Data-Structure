''' 더블리 링크드 리스트의 head 노드 앞에 새로운 노드를 추가하는 prepend 메소드 구현 '''

class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data):
        self.data = data  # 실제 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스
        self.prev = None  # 전 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
            self.head = None  # 링크드 리스트 가장 앞 노드
            self.tail = None  # 링크드 리스 가장 뒤 노드

    def prepend(self, data):
        """링크드 리스트 가장 앞에 데이터를 추가시켜주는 메소드"""
        new_node = Node(data)

        if self.head is None:
            # head 노드가 비어있다면 = 연결 리스트가 비어있는 상태
            self.head = new_node
            self.tail = new_node
                # head와 tail 노드를 새 노드로 지정
        else:
            # 연결 리스트가 비어있지 않은 경우
            new_node.next = self.head
                # 새 노드의 next 레퍼런스를 기존 head 노드로 지정
            self.head.prev = new_node
                # 기존 head 노드의 prev 레퍼런스(이전 노드)를 새 노드로 지정
            self.head = new_node
                # 새 노드를 head 노드로 갱신

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str


# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 여러 데이터를 링크드 리스트 앞에 추가
my_list.prepend(11)
my_list.prepend(7)
my_list.prepend(5)
my_list.prepend(3)
my_list.prepend(2)

print(my_list) # 링크드 리스트 출력

# head, tail 노드가 제대로 설정됐는지 확인
print(my_list.head.data)
print(my_list.tail.data)
