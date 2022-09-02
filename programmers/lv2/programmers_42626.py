import heapq


def solution(foods, K):
    q = []
    count = 0

    for food in foods:
        heapq.heappush(q, food)

    # 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복한다
    while q[0] < K:
        try:
            first = heapq.heappop(q)
            second = heapq.heappop(q)
            result = first + (2 * second)
            heapq.heappush(q, result)
        # 인덱스 에러가 걸리면 second를 못 가져온다는 것이기 때문에 모두 조합해도 결과가 안 나온다는 것임
        except IndexError:
            return -1
        count += 1

    return count