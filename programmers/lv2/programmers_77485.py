# 행렬 테두리를 직렬화 해서 리턴해주는 함수
def serialize_matrix(graph, x1, y1, x2, y2):
    result = []

    # 맨 위의 가로를 직렬화한다 (끝은 미포함)
    for i in range(y1, y2):
        result.append([x1, i, graph[x1][i]])

    # 맨 오른쪽 세로 라인을 직렬화한다 (끝은 미포함)
    for i in range(x1, x2):
        result.append([i, y2, graph[i][y2]])

    # 맨 아래 라인을 직렬화한다 (끝은 미포함)
    for i in range(y2, y1, -1):
        result.append([x2, i, graph[x2][i]])

    # 맨 왼쪽 라인을 직렬화한다 (끝은 미포함)
    for i in range(x2, x1, -1):
        result.append([i, y1, graph[i][y1]])

    return result


# 주어진 직렬화 결과를 회전시킨 배열을 리턴하는 함수
def spin(serialized):
    # 첫번째 위치를 임시로 저장한다
    first_x, first_y = serialized[0][0], serialized[0][1]
    # 한칸씩 좌표를 밀어버린다
    for i in range(len(serialized) - 1):
        serialized[i][0] = serialized[i + 1][0]
        serialized[i][1] = serialized[i + 1][1]

    # 맨 마지막 원소의 좌표는 첫번째로 지정한다
    serialized[-1][0] = first_x
    serialized[-1][1] = first_y


def solution(rows, columns, queries):
    answer = []

    # 지도
    graph = [[(1 + i) + columns * j for i in range(columns)] for j in range(rows)]

    # 주어진 모든 queries의 좌표를 컴퓨터에 맞게 수정한다
    for query in queries:
        for i in range(len(query)):
            query[i] -= 1

    # 주어진 query를 모두 읽으면서
    for query in queries:
        # 직렬화된 결과를 가져온다
        serialized = serialize_matrix(graph, query[0], query[1], query[2], query[3])
        # 최솟값을 우선 저장한다
        values = [i[2] for i in serialized]
        answer.append(min(values))
        # serialized를 회전시킨다
        spin(serialized)
        # serialized를 읽으면서 graph에 반영시켜버린다
        for x, y, value in serialized:
            graph[x][y] = value

    return answer