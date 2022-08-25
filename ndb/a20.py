import sys

input = sys.stdin.readline

N = int(input())
# 지도 정보
graph = []
# 지도 정보 입력
for _ in range(N):
    graph.append(list(input().split()))

ans = False


# 선생님한테 걸리는지 여부를 체크해주는 함수
def check(graph):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'T' and check_teacher(graph, (i, j)) == False:
                return False
    return True


# 주어진 좌표를 기준으로 상하좌우로 학생이 있는지 검사
def check_teacher(graph, coordinate):
    x, y = coordinate
    # 왼쪽부터 다 채운다
    for i in range(y, -1, -1):
        if graph[x][i] == 'O':
            break
        elif graph[x][i] == 'S':
            return False
    # 오른쪽을 채운다
    for i in range(y, N):
        if graph[x][i] == 'O':
            break
        elif graph[x][i] == 'S':
            return False
    # 아래를 채운다
    for i in range(x, -1, -1):
        if graph[i][y] == 'O':
            break
        elif graph[i][y] == 'S':
            return False
    # 위를 채운다
    for i in range(x, N):
        if graph[i][y] == 'O':
            break
        elif graph[i][y] == 'S':
            return False
    return True


# 장애물을 세우다가, 3개가 되면 만족 여부를 체크해주는 함수
def func(count):
    global ans
    # 3개를 다 세운 경우
    if count == 3:
        if check(graph) == True:
            ans = True
        return

    # 3개가 아니기 때문에 벽을 계속 세운다
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                func(count + 1)
                graph[i][j] = 'X'


# 탐색
func(0)

# 정답 출력
if ans:
    print('YES')
else:
    print('NO')
