from collections import deque
import sys
input = sys.stdin.readline

# BFS 기반으로 탐색
def bfs(graph, visited, start):
    queue = deque()
    # 해당 도시 방문 처리
    queue.append((0, start))
    visited[start] = True

    # 큐가 빌 때까지 무한 반복
    while queue:
        # 큐에서 아이템 하나 꺼내기
        v_info = queue.popleft()
        # 인접한 모든 도시들을 queue에 추가 (방문한 적이 없다면)
        for city in graph[v_info[1]]:
            if not visited[city]:
                queue.append((v_info[0] + 1, city))
                visited[city] = True
                # 만약에 경로 2인 곳에 위치한 도시라면 ans에 append 해준다
                if v_info[0] + 1 == K:
                    ans.append(city)

# N: 도시의 개수, M: 도로의 개수, K: 거리 정보, X: 출발 도시의 번호
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)] # 인접 그래프 선언
visited = [False] * (N + 1) # 0부터 N 까지 인덱스를 가지는 방문 정보 리스트
ans = []

# 그래프 초기화
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B) # A 인덱스에 B 도시 추가

# 탐색을 한번 해준다
bfs(graph, visited, X)

if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for city in ans:
        print(city)