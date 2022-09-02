import copy

answer = 0


# 숫자 리스트, 연산자 리스트를 뽑아오는 함수
def extract_expression_info(expression, number_list, operator_list):
    first = 0
    for i in range(len(expression)):
        # 연산자를 현재 참조하는 경우
        if expression[i] in ['+', '-', '*']:
            tmp1 = int(expression[first:i])
            tmp2 = expression[i]
            number_list.append(tmp1)
            operator_list.append(tmp2)
            first = i + 1
        elif i == len(expression) - 1:
            tmp1 = int(expression[first:])
            number_list.append(tmp1)


# 두 숫자를 operator에 따라서 연산한 결과를 반환해주는 함수
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


# number_list, operator_list, 우선순위 리스트를 받아서 계산 결과를 반환해주는 함수
def total_calculate(number_list, operator_list, priority_list):
    # 우선순위에 맞는 연산을 먼저 찾아서 수행한다
    for priority in priority_list:
        count = 0  # 중복 연산을 할 경우 보정하기 위한 값

        # 우선순위에 맞는 연산이 존재하지 않는 경우 건너뛴다
        if priority not in operator_list:
            continue

        # operator_list를 선형으로 읽어서 연산을 수행한다
        for i, operator in enumerate(operator_list):
            # 일치하는 연산인 경우
            if operator == priority:
                first = number_list.pop(i - count)
                second = number_list.pop(i - count)
                result = calculate(first, second, operator)
                number_list.insert(i - count, result)
                count += 1

        # 연산자를 날려버린다
        while priority in operator_list:
            operator_list.remove(priority)

    return abs(number_list[0])


# 재귀적인 접근을 이용해서 계산 결과를 갱신해주는 함수
def recursive(count, number_list, operator_list, priority_list):
    global answer

    ops = ['+', '-', '*']

    if count == 3:
        # 모든걸 깊은 복사를 이용해서 전달해줘야한다
        nums_param = copy.deepcopy(number_list)
        operators_param = copy.deepcopy(operator_list)
        result = total_calculate(nums_param, operators_param, priority_list)
        answer = max(answer, result)
        return

    # ops를 돌면서 없는 op를 더해준다
    for op in ops:
        if op not in priority_list:
            priority_list.append(op)
            recursive(count + 1, number_list, operator_list, priority_list)
            priority_list.remove(op)


def solution(expression):
    global answer
    number_list = []  # 숫자의 리스트
    operator_list = []  # 연산자의 리스트

    extract_expression_info(expression, number_list, operator_list)
    recursive(0, number_list, operator_list, [])

    return answer
