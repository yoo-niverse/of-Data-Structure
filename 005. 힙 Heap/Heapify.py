''' 힙 속성을 만족시키기 위해 동작하는 Heapify 함수 구현 '''

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

    if not 0 < left_child_index + right_child_index < tree_size * 2:
        return None
            # 재귀호출로 처리되는 왼쪽 자식노드와 오른쪽 자식노드 인덱스의 합이 범위를 벗어나면 실행 중단

    max_node = max(tree[index], tree[left_child_index], tree[right_child_index])
        # 파라미터로 받은 노드와 해당 노드의 자식 노드들 중 최대값을 저장

    if max_node != tree[index]:
        # 파라미터로 받은 노드의 값이 최대값이 아닐 경우

        if tree[left_child_index] > tree[right_child_index]:
            # 왼쪽 자식 노드의 값이 오른쪽보다 크다면
            swap(tree, index, left_child_index)
            heapify(tree, left_child_index, tree_size)
                # 파라미터로 받은 노드(부모)와 왼쪽 노드의 data를 swap하고, 재배치 후 힙 속성을 만족하는지 재귀함수로 확인

        else:
            swap(tree, index, right_child_index)
            heapify(tree, right_child_index, tree_size)


# 인덱스 넘치는 문제 어떻게 해결할래?



# 실행 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree)
