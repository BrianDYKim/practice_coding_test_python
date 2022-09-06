import math

answer = 0
dp_table = [False] * 3001


def dp():
    for i in range(2, 3001):
        if dp_table[i] == False:
            dp_table[i] = is_prime(i)


def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True

    length = math.sqrt(num)
    length = math.floor(length)

    for i in range(2, length + 1):
        if num % i == 0:
            return False
    return True


def recursive(count, buffer, number_list):
    global answer
    global dp_table

    if count == 3:
        if dp_table[sum(buffer)]:
            answer += 1
        return

    for number in number_list:
        if number not in buffer:
            buffer.append(number)
            recursive(count + 1, buffer, number_list)
            buffer.remove(number)


def solution(nums):
    global answer

    # 미리 소수들을 계산해둔다
    dp()

    # 재귀함수를 이용해서 탐색한다
    recursive(0, [], nums)

    # 중복의 경우의 수 제거
    answer //= 6

    return answer