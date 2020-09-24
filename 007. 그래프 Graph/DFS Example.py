''' DFS을 이용하여 인접 역 탐색을 구현하는 코드 '''

from collections import deque
from subway_graph import *

def dfs(graph, start_node):
    """최단 경로용 bfs 함수"""
    stack = deque()  # 빈 큐 생성

    # 모든 노드를 처음 보는 노드(visited = 0)로 초기화
    for station_node in graph.values():
        station_node.visited = 0

    start_node.visited = 1
    stack.append(start_node)
        # DFS 탐색 순서 1 : 파라미터로 전달받은 시작 노드에 스택 추가 표시를 하고, 스택에 push한다.

    while stack:
        distin = stack.pop()
        distin.visited = 2
        # DFS 탐색 순서 2 : 스택에 요소가 있는 동안 반복하며, 요소들을 하나씩 꺼내고 pop된 요소는 방문한 것으로 표시(visited = 2)한다.

        for i in distin.adjacent_stations:
            # DFS 탐색 순서 3 : 꺼낸 노드들의 인접 리스트에 저장된 내용을 반복적으로 받아온다.
            tmp = i

            if tmp.visited == 0:
                tmp.visited = 1
                stack.append(tmp)
                # DFS 탐색 순서 4 : 가져온 인접 노드를 방문한 적이 없다면, 스택 추가 표시(visited = 0)하고, 스택에 추가한다.


stations = create_station_graph("./new_stations.txt")  # stations.txt 파일로 그래프를 만든다

gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
dfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)

