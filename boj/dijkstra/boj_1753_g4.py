import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
V, E = map(int, input().split())
# 시작 노드
start = int(input())
# 거리 정보를 저장하는 배열
distance = [INF] * (V + 1)
# 연결 정보를 저장하는 배열
graph = [[] for i in range(V + 1)]

# 간선 정보 입력
for i in range(E):
    # a->b의 코스트가 c이다
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라 구현
def dijkstra(start):
    q = []
    # 시작 지점에 대해서 초기화
    distance[start] = 0
    heapq.heappush(q, (0, start))

    # 큐가 빌 때까지 반복
    while q:
        dist, now = heapq.heappop(q)
        # 만일 방문했던 노드였다면?
        if distance[now] < dist:
            continue
        # 방문한 적이 없다면 연결 노드를 모두 탐색해서 업데이트를 진행한다
        for info in graph[now]:
            # 새롭게 코스트를 계산
            cost = distance[now] + info[1]
            if cost < distance[info[0]]:
                heapq.heappush(q, (cost, info[0]))
                distance[info[0]] = cost

# 다익스트라 알고리즘 호출
dijkstra(start)

# 출력
for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])