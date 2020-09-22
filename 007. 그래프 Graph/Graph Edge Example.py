''' 인접행렬을 이용하여 그래프의 엣지 구현 '''

# 모든 요소를 0으로 초기화시킨 크기 6 x 6 인접 행렬
adjacency_matrix = [[0 for i in range(6)] for i in range(6)]

def adj(in_a, in_b):
    adjacency_matrix[in_a][in_b] = 1
    adjacency_matrix[in_b][in_a] = 1
        # 무방향, 무가중치 그래프의 대칭성을 이용하여 노드 a에서 b로의 연결관계를 1로 표시하면,
        # b에서 a로의 연결관계도 1로 표시하도록 했다.

adj(0,1)
adj(0,2)
adj(1,3)
adj(1,5)
adj(2,5)
adj(3,4)
adj(3,5)
adj(4,5)

print(adjacency_matrix)
