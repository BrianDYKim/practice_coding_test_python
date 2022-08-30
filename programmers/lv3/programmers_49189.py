import heapq


# 다익스트라 알고리즘으로 해결한다 (0:44 ~ 0:58)
def solution(n, vertex_list):
    INF = int(1e9)  # max값
    # 최단거리를 저장하는 리스트
    distance = [INF] * (n + 1)  # 1 ~ n 번까지의 최단거리를 저장하는 배열
    # 연결 노드 정보를 저장하는 리스트
    graph = [[] for _ in range(n + 1)]  # 1 ~ n 번까지 연결 간선 리스트를 저장하는 배열
    for vertex in vertex_list:
        a, b = vertex
        # 양방향 그래프이므로 양방향으로 간선 연결
        graph[a].append((1, b))
        graph[b].append((1, a))

    # 다익스트라 함수 호출
    dijkstra(1, graph, distance)

    # 맨 앞의 distance 정보는 제거한다
    distance.pop(0)

    # 최댓값을 뽑아온다
    max_distance = max(distance)

    # count를 뽑아온다
    answer = distance.count(max_distance)

    return answer


# 다익스트라 함수
def dijkstra(start, graph, distance):
    q = []
    # 시작 지점에 대한 초기화
    distance[start] = 0
    heapq.heappush(q, (0, start))

    # 큐가 빌 때까지 반복한다
    while q:
        # 우선순위 큐에서 아이템을 하나 꺼낸다 (cost, node)
        cost, now = heapq.heappop(q)
        # 만약에 이미 들른적이 있는 노드였을 경우 -> 패스한다
        if distance[now] < cost:
            continue
        # 연결된 간선을 모두 조회한다
        for info in graph[now]:
            # 새로운 비용을 계산한다
            new_cost = distance[now] + info[0]
            # 만약에 더 짧은 경우
            if new_cost < distance[info[1]]:
                distance[info[1]] = new_cost
                heapq.heappush(q, (new_cost, info[1]))