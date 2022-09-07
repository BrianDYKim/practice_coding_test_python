import math

answer = 0
checked_list = []


# 18:54 ~
# 해당 숫자가 소수인지 판별하는 함수
def is_prime(value):
    if value <= 1:
        return False
    elif value == 2:
        return True

    upper_bound = math.floor(value ** 0.5)  # 루트 value의 소숫점을 버린다

    for i in range(2, upper_bound + 1):
        if value % i == 0:
            return False

    return True


# 주어진 숫자 배열로 만들어지는 숫자가 소수인지 판별해주는 함수
def check(number_list):
    global checked_list
    # 첫번째 원소가 0인 경우 숫자 형성 자체가 안된다
    if number_list[0] == '0':
        return False

    result = ''
    for number in number_list:
        result += number

    target = int(result)

    if target in checked_list:
        return False

    print(target)

    checked_list.append(target)

    return is_prime(int(result))


# 재귀함수를 기반으로 탐색하는 함수
def recursive(current, numbers, length):
    global answer
    # 탈출 조건 -> 모든 숫자를 탐색했을 때는 체크하고 빠져나간다
    if len(current) == length:
        return

    # numbers를 순차적으로 탐색한다
    for i, number in enumerate(numbers):
        # 숫자의 중복이 허용되므로 그냥 넣고본다
        current.append(number)
        # 숫자를 넣었기 때문에 numbers로부터 삭제해둔다
        numbers.remove(numbers[i])
        # 체크한다
        if check(current):
            answer += 1
        # depth를 1 늘려서 탐색한다
        recursive(current, numbers, length)
        # 숫자 복구
        numbers.insert(i, number)
        current.pop(-1)


def solution(numbers):
    global answer

    numbers = [token for token in numbers]
    recursive([], numbers, len(numbers))

    return answer