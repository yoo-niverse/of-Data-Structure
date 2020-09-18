''' 힙의 삽입 연산을 구현하기 '''

def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def reverse_heapify(tree, index):
    """삽입된 노드를 힙 속성을 지키는 위치로 이동시키는 함수"""
    parent_index = index // 2  # 삽입된 노드의 부모 노드의 인덱스 계산

    if parent_index == 0:
        return None
        # 파라미터로 받은 index를 2로 나누어 부모 인덱스를 계산했을 때, 0이 나오면 더 이상 부모가 없는 것이므로 수행 중단

    if tree[parent_index] < tree[index]:
       swap(tree, parent_index, index)
        # 부모 노드의 값 보다 새로 추가된 노드의 값이 크다면 둘의 자리 변경
       reverse_heapify(tree, parent_index)
        # 자리를 변경을 완료한 경우 재귀 호출을 통해 새로운 부모노드를 계산하고 자리 변경여부 재 파악




class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""
    def __init__(self):
        self.heap = [None]  # 파이썬 리스트로 구현한 힙


    def insert(self, data):
        """삽입 메소드"""
        self.heap.append(data)
        reverse_heapify(self.heap, len(self.heap)-1)


    def __str__(self):
        return str(self.heap)


'''# 실행 코드
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue)
'''
