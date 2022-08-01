import sys
input = sys.stdin.readline

N = int(input()) # 학생 수 입력
student_list = []

# 학생 정보 입력받기
for _ in range(N):
    name, korean, eng, math = input().split()
    student_list.append([name, int(korean), int(eng), int(math)])

student_list.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in student_list:
    print(student[0])