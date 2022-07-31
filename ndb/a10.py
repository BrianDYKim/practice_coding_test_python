# 주어진 배열을 90도 돌리는 함수
def rotate_matrix_by_90_degree(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])  # 열 길이 계산
    result = [[0] * n for _ in range(m)]  # 결과 리스트

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]

    return result


# 자물쇠의 중간 부분이 모두 1인지 체크하는 함수
def check(new_lock):
    lock_length = len(new_lock) // 3

    # 중간 부분을 체크한다
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False

    return True


# 솔루션 함수
def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 자물쇠의 크기를 기존의 3배로 패딩
    new_lock = [[0] * (3 * n) for _ in range(3 * n)]

    # 새로운 자물쇠의 중간 부분에 기존의 자물쇠 정보를 부여하기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인하기
    for rotation in range(4):
        key = rotate_matrix_by_90_degree(key)  # 90도 회전

        for x in range(2 * n):
            for y in range(2 * n):
                # 자물쇠에 열쇠를 끼운다
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                # 새로운 자물쇠가 맞는지 검사
                if check(new_lock) == True:
                    return True

                # 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False