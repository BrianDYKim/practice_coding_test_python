import sys
input = sys.stdin.readline

N = int(input())
number_list = []

for _ in range(N):
    number_list.append(int(input()))

number_list.sort() # 정렬
sum = 0

for i in range(N):
    if i in (0, 1):
        sum += number_list[i]
    else:
        sum = sum * 2 + number_list[i]

print(int(sum))