''' 파이썬 리스트로 구현된 Heap을 활용하여 힙 정렬 수행 '''

def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index

    if largest != index: # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를 대상으로 또 heapify 함수를 호출한다



def heapsort(tree):
    """힙 정렬 함수"""
    tree_size = len(tree)

    for i in range(tree_size-1, 0, -1):
        heapify(tree, i, tree_size)
        # 힙 속성(부모 노드 > 자식 노드)을 만족시키게 하기 위하여 우선 leaf node부터 heapify를 해준다.

    for i in range(tree_size-1, 1, -1):
        swap(tree, 1, i)
        heapify(tree, 1, i)
        # heapify를 통해 heap이 완성되었으면, 1번과 마지막 인덱스 노드를 변경하고,
        # 다시 heapify를 활용하여 힙 정렬을 수행한다.

        ''' 분명히 문제에 "먼저 리스트를 힙으로 만듭니다."라고 명시 되어있었기에, 1번 반복문을 수행해야했다.
         그러나 반복문 하나로 swap과 그 후 heapify만 수행하려고 하니 뜻하는 결과가 출력되지 않았다. '''



# 실행 코드
data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]
heapsort(data_to_sort)
print(data_to_sort)
