import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

# 이진탐색 메소드
def search(start, end, target):
    if start > end:
        return start

    mid = (start + end) // 2

    if res[mid] == target:
        return mid
    elif res[mid] > target:
        return search(start, mid - 1, target)
    else:
        return search(mid + 1, end, target)

# LIS를 저장하는 배열
res = [num_list[0]]

# num_list를 첫번째 인덱스부터 순차적으로 탐색
for i in range(1, len(num_list)):
    # LIS의 마지막 원소와 비교를 수행한다
    length = len(res)
    if res[length - 1] < num_list[i]:
        res.append(num_list[i])
    else:
        res[search(0, length - 1, num_list[i])] = num_list[i]

print(len(res))