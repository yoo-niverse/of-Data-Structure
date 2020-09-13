class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data):
        self.data = data  # 실제 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스
        self.prev = None  # 전 노드에 대한 레퍼런스

class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""

        if self.head is self.tail:
            # 만약 head 노드와 tail 노드가 동일하다면 : CASE 1. 마지막 노드를 삭제할 경우
            self.head = None
            self.tail = None
                # head와 tail 노드를 None으로 갱신하여 연결을 끊음

        elif node_to_delete is self.head:
            # CASE 2. 제거할 노드가 head 노드일 경우
            self.head = node_to_delete.next
            self.head.prev = None
                # 제거할 노드의 다음 노드로 head 노드를 변경, 새 head 노드의 prev 레퍼런스를 None으로 갱신

        elif node_to_delete is self.tail:
            # CASE 3. 제거할 노드가 tail 노드일 경우
            self.tail = node_to_delete.prev
            self.tail.next = None
                # 제거할 노드의 이전 노드를 tail 노드로 변경, 새 tail 노드의 next 레퍼런스를 None으로 갱신

        else:
            # CASE 4. 중간에 있는 노드를 삭제할 경우
            node_to_delete.prev.next = node_to_delete.next
                # 삭제할 노드의 이전 노드 next 값을 삭제할 노드 다음 노드로 변경
            node_to_delete.next.prev = node_to_delete.prev
                # 삭제할 노드의 다음 나도 prev 값을 삭제할 노드 이전 노드로 변경

        return node_to_delete.data

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정한다"""

        iterator = self.head # 링크드 리스트를 돌기 위해 필요한 노드 변수

        # index 번째 있는 노드로 간다
        for _ in range(index):
            iterator = iterator.next

        return iterator

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)  # 새로운 노드 생성

        # 빈 링크드 리스트라면 head와 tail을 새로 만든 노드로 지정
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 이미 노드가 있으면
        else:
            self.tail.next = new_node  # 마지막 노드의 다음 노드로 추가
            new_node.prev = self.tail
            self.tail = new_node  # 마지막 노드 업데이

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

# 새로운 노드 4개 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)

# 두 노드 사이에 있는 노드 삭제
node_at_index_2 = my_list.find_node_at(2)
my_list.delete(node_at_index_2)
print(my_list)

# 가장 앞 노드 삭제
head_node = my_list.head
print(my_list.delete(head_node))
print(my_list)

# 가장 뒤 노드 삭제
tail_node = my_list.tail
my_list.delete(tail_node)
print(my_list)

# 마지막 노드 삭제
last_node  = my_list.head
my_list.delete(last_node)
print(my_list)
