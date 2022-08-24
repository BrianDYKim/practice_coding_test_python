import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수, 스타트 지점
n, m, c = map(int, input().split())
# 연결 정보
graph = [[] for _ in range(n + 1)]
# 거리 정보
distance = [INF] * (n + 1)
# 간선 정보 입력
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))  # x->y 의 비용이 z 라는 뜻


# 다익스트라 알고리즘 구현
def dijkstra(start):
    q = []
    # 시작점 정보 초기화
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # 큐가 빌 때까지 반복
    while q:
        dist, now = heapq.heappop(q)
        # 만약 들렀던 경우 패스
        if distance[now] < dist:
            continue

        # 연결된 노드들을 모두 조회
        for i in graph[now]:
            cost = dist + i[1]  # 새롭게 코스트를 계산
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘 호출
dijkstra(c)

# 전보를 받는 도시 목록을 모두 리스트로 받아옴
result = list(filter(lambda x: x != INF, distance))
print(len(result) - 1, max(result))  # 자기 자신의 노드는 제외한다
