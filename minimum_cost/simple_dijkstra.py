import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력
n, m = map(int, input().split())
# 시작 노드를 입력받기
start = int(input())
# 연결 정보
graph = [[] for i in range(n + 1)]
# 방문 정보
visited = [False] * (n + 1)
# 최단거리 정보를 저장하는 리스트
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a에서 b로 가는 거리가 c라는 뜻


# distance에서 방문하지 않은 노드들 중에서 가장 최단거리의 노드를 가져오는 함수
def get_smallest_node():
    index = 0
    min_value = INF

    for i in range(n + 1):
        if distance[i] < min_value and not visited[i]:
            index = i
            min_value = distance[i]

    return index


# 다익스트라 알고리즘
def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 모든 노드를 탐색
    for i in range(n - 1):
        # 최단 거리를 가지는 노드를 가져오기
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            # 새롭게 코스트를 계산
            cost = distance[now] + j[1]
            # 새롭게 갱신
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드를 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print('inf')
    else:
        print(distance[i])