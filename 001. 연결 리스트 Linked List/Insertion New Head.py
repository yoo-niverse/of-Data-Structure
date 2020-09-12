class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data):
        self.data = data  # 실제 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        new_node = Node(data)
            # 새로운 노드를 노드 클래스의 객체로 생성

        if self.head is None:
            # head 노드가 비어있다면(비어있는 리스트라면)
            self.head = new_node
            # 새로운 노드를 head 노드로 지정
        else:
            new_node.next = self.head
            # 그외의 경우 새 노드의 next가 기존 head 노드를 가르키게 함
            self.head = new_node
            # 새로운 노드를 head 노드로 지정

        i = self.head
        while i.next is not None:
            i = i.next
        self.tail = i


    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str



# 새로운 링크드 리스트 생성
linked_list = LinkedList()

# 여러 데이터를 링크드 리스트 앞에 추가
linked_list.prepend(11)
linked_list.prepend(7)
linked_list.prepend(5)
linked_list.prepend(3)
linked_list.prepend(2)

print(linked_list)  # 링크드 리스트 출력

# head, tail 노드가 제대로 설정됐는지 확인
print(linked_list.head.data)
print(linked_list.tail.data)

