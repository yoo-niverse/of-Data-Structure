''' 힙으로 구현한 우선순위 큐에서 우선순위에 따라 데이터를 추출하는 코드 구현 '''

from Heapify import *
from Insertion_of_Heap import reverse_heapify

class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""
    def __init__(self):
        self.heap = [None]  # 파이썬 리스트로 구현한 힙

    def insert(self, data):
        """삽입 메소드"""
        self.heap.append(data)  # 힙의 마지막에 데이터 추가
        reverse_heapify(self.heap, len(self.heap)-1) # 삽입된 노드(추가된 데이터)의 위치를 재배치

    def extract_max(self):
        """최우선순위 데이터 추출 메소드"""
        swap(self.heap, 1, len(self.heap)-1)
            # root노드와 마지막 leaf 노드의 자리 교체
        return_value = self.heap.pop()
            # 원래 root에 있던, 새로운 leaf 노드의 값을 return_value에 저장

        heapify(self.heap, 1, len(self.heap))
            # 새로운 root 노드가 힙 속성을 만족할 수 있도록 heapify 실행
       return return_value
            # 저장해뒀던 마지막 노드의 값 return

    def __str__(self):
        return str(self.heap)

# 출력 코드
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
