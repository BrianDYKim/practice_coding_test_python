def solution(n, times):
    first, second = 1, max(times) * n  # 이분 탐색을 위해서 하한, 상한을 정해둠
    ans = 0

    while first <= second:
        count = 0
        mid = (first + second) // 2

        for time in times:
            count += (mid // time)

            if count >= n:
                break

        if count >= n:
            second = mid - 1
            ans = mid
        else:
            first = mid + 1

    return ans