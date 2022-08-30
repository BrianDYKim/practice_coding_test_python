# 해당 문자열에 완성된 괄호가 있는지 판단하여서 q에 완성된 괄호를 빼는 함수
def check(sentence):
    # 만약에 q에 원소가 2개 미만으로 들어가있다면 false를 반환해준다
    if len(sentence) < 2:
        return False

    first = sentence.pop(-1)
    second = sentence.pop(-1)

    # 만약에 완성된 괄호일 경우
    if first == ')' and second == '(':
        return True
    # 완성된 괄호가 아닌 경우 -> 다시 원상복구 시킨다
    else:
        sentence.append(second)
        sentence.append(first)
        return False


def solution(s):
    # 아예 성공하지 못할 경우엔 무조건 false를 반환한다
    if len(s) in [0, 1]:
        return False

    sentence = []
    # 먼저 첫번째, 두번째 원소는 집어넣고 시작한다
    for i in range(2):
        sentence.append(s[i])

    # 완성이 된 괄호인지 우선 체크부터 해준다
    check(sentence)

    if len(s) > 2:
        # 나머지 원소들도 모두 넣어준다
        for i in range(2, len(s)):
            sentence.append(s[i])

            # 올바른 괄호가 있는지 체크를 해준다
            check(sentence)

    # q가 빈 경우 true, 남아있는 경우 false를 반환해준다
    if len(sentence) == 0:
        return True
    else:
        return False