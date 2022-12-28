import sys
input = sys.stdin.readline

# 38분
# 3, 4, 5
# 0 2
def evaluation(number_list, operator_orders, operator_list):
    result = 0
    for i, order in enumerate(operator_orders):
        if i == 0:
            num1 = number_list[0]
            num2 = number_list[1]
        else:
            num1 = result
            num2 = number_list[i + 1]

        operator = operator_list[order] # operator_list에서 인덱스 기반 참조해서 연산자 추출
        result = partial_evaluation(num1, num2, operator)

    return result

def partial_evaluation(num1, num2, operator):
    if operator == 0:
        return num1 + num2
    elif operator == 1:
        return num1 - num2
    elif operator == 2:
        return num1 * num2
    else:
        if num1 < 0:
            tmp = abs(num1) // num2
            return -tmp
        else:
            return num1 // num2

min_answer, max_answer = 1e10, -1e10

N = int(input())

number_list = list(map(int, input().split()))

operator_input = list(map(int, input().split()))
operator_list = []

for i, count in enumerate(operator_input):
    for j in range(count):
        operator_list.append(i)

def solution(k, operator_orders):
    global min_answer, max_answer
    if k == N - 1:
        result = evaluation(number_list, operator_orders, operator_list)
        min_answer = min(min_answer, result)
        max_answer = max(max_answer, result)
        return

    for i in range(N - 1):
        # 만약에 없는 인덱스이면 추가한다
        if i not in operator_orders:
            operator_orders.append(i)
            solution(k + 1, operator_orders)
            operator_orders.pop()

solution(0, [])
print(max_answer)
print(min_answer)