# 주어진 문자열이 올바른지 판단하는 함수
def is_correct(sentence):
    stack = []

    # 문자 하나씩 탐색한다
    for token in sentence:
        stack.append(token)

        # 만약에 스택의 원소가 두 개 이상이라면?
        if len(stack) >= 2:
            first = stack.pop(-1)
            second = stack.pop(-1)

            # 만약에 first와 second가 완벽한 괄호를 이루지 않는다면 다시 넣는다
            if first == ')' and second == '(':
                continue
            else:
                stack.append(second)
                stack.append(first)

    # 만약에 stack에 원소가 없다면 완벽하다
    return True if len(stack) == 0 else False


# 주어진 문자열을 u와 v로 쪼개는 함수
def split_sentence(sentence):
    first = 1 if sentence[0] == '(' else 0
    second = 1 if sentence[0] == ')' else 0
    u = sentence[0]

    for i in range(1, len(sentence)):
        if sentence[i] == '(':
            first += 1
            u += '('
        else:
            second += 1
            u += ')'

        if first == second:
            break

    # u가 완성이 되었다면
    v = sentence[len(u):]

    return u, v


# 주어진 문장의 괄호 방향을 모두 뒤집는 함수
def flip(sentence):
    result = ''
    for i in range(len(sentence)):
        if sentence[i] == '(':
            result += ')'
        else:
            result += '('

    return result


# 재귀함수 구현
def recursive(sentence):
    # 완벽한 문자열이 들어왔다면 바로 리턴한다
    if is_correct(sentence):
        return sentence

    # u와 v를 쪼갠다
    u, v = split_sentence(sentence)

    # u가 올바른 문자열인 경우
    if is_correct(u):
        return u + recursive(v)
    # u가 올바르지 못한 경우
    else:
        return '(' + recursive(v) + ')' + flip(u[1:-1])


def solution(p):
    return recursive(p)