import sys

input = sys.stdin.readline

N = int(input())

# 숫자 삼각형을 저장하는 배열
graph = []

# 숫자 삼각형 초기화
for i in range(N):
    if i == 0:
        graph.append([int(input())])
    else:
        graph.append(list(map(int, input().split())))

# 다이내믹 프로그래밍 방식으로 코스트 계산
for i in range(1, N):
    for j in range(i + 1):
        # 왼쪽 구석일 경우
        if j == 0:
            graph[i][j] += graph[i - 1][j]
        # 오른쪽 구석일 경우
        elif j == i:
            graph[i][j] += graph[i - 1][j - 1]
        # 가운데일 경우
        else:
            weight = max(graph[i - 1][j], graph[i - 1][j - 1])
            graph[i][j] += weight

print(max(graph[N - 1]))