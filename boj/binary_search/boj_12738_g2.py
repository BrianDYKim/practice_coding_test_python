import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_set = set(num_list)
print(len(num_set))