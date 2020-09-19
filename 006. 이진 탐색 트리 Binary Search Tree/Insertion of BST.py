''' 이진 탐색 트리의 삽입연산 구현 '''

class Node:
    """이진 탐색 트리 노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right_child = None
        self.left_child = None


def print_inorder(node):
    """주어진 노드를 in-order로 출력해주는 함수"""
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)


class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None


    def insert(self, data):
        new_node = Node(data)  # 삽입할 데이터를 갖는 새 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다
        if self.root is None:
            self.root = new_node
            return

        compare = self.root
            # 비교 대상이 될 compare 변수에 우선 self.root를 저장

        while True:
            # 반복문을 종료시킬 때까지 반복

            if new_node.data > compare.data:
                # 새 노드의 데이터가 비교 대상이 되는 노드의 데이터보다 크다면
                if compare.right_child is None:
                    # 동시에 비교 대상 노드의 오른쪽 자식이 비어있다면,

                    compare.right_child = new_node
                    new_node.parent = compare.right_child
                    return
                        # 새 노드를 오른쪽 자식 노드로 연결하고 반복문을 종료
                else:
                    compare = compare.right_child
                    continue
                        # 자식 노드가 비어있지 않을 경우 다시 현재 자식 노드와 동일한 비교를 수행

            if new_node.data < compare.data:
                if compare.left_child is None:
                    compare.left_child = new_node
                    new_node.parent = compare.left_child
                    return

                else:
                    compare = compare.left_child
                    continue

                    # 오른쪽 자식 노드와 비교하는 과정과 동일

    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root)  # root 노드를 in-order로 출력한다


# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 이진 탐색 트리 출력
bst.print_sorted_tree()
