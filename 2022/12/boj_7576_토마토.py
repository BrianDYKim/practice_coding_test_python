from collections import deque
import sys

input = sys.stdin.readline

answer = 0
# M: 상자의 가로 크기, N: 상자의 세로 크기
M, N = map(int, input().split())
is_already_all = True

# 해당 좌표가 가능한지 여부를 알려주는 함수
def possible(coordinate, tomato_map):
    i, j = coordinate

    if i >= N or j >= M or i < 0 or j < 0:
        return False

    if tomato_map[i][j] == 0:
        return True

# 좌표 후보군을 뽑아오는 함수
def get_candidates(coordinate):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result = []
    i, j = coordinate

    for diff_x, diff_y in zip(dx, dy):
        result.append((i + diff_x, j + diff_y))
    return result

def bfs(q, tomato_map):
    global answer
    while q:
        current_age, coordinate = q.popleft()
        candidates = get_candidates(coordinate)

        for candidate in candidates:
            if possible(candidate, tomato_map):
                # 우선 토마토를 익힌다
                new_x, new_y = candidate
                tomato_map[new_x][new_y] = current_age + 1
                # answer를 갱신한다
                answer = max(current_age + 1, answer)
                # 토마토 위치 정보를 queue에 추가한다
                q.append([current_age + 1, (new_x, new_y)])

# 익지 않은 영역이 있는지 검사하는 함수
def check(tomato_map):
    for i in range(N):
        for j in range(M):
            if tomato_map[i][j] == 0:
                return False

    return True

tomato_map = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    tomato_map.append(tmp)

q = deque()

# 토마토 위치를 queue에 저장
for i in range(N):
    for j in range(M):
        if tomato_map[i][j] == 1:
            q.append([1, (i, j)]) # age, 좌표 순으로 저장
        elif tomato_map[i][j] == 0:
            is_already_all = False

# bfs 탐색 시작
bfs(q, tomato_map)

# 다 익었는가
is_completed = check(tomato_map)

if is_already_all:
    print(0)
elif is_completed:
    print(answer - 1)
else:
    print(-1)