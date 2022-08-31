ans = 0


def func(count, numbers, sequence, target):
    global ans
    # 만약에 sequence의 원소를 모두 채우게된다면
    if count == len(numbers):
        # 만일 sequence의 모든 합이 target과 일치한다면 ans를 더한다
        if sum(sequence) == target:
            ans += 1

        return

    # 점화관계
    sequence.append(numbers[count])
    func(count + 1, numbers, sequence, target)
    sequence[-1] = -sequence[-1]  # 마지막 숫자 부호 뒤집기
    func(count + 1, numbers, sequence, target)
    sequence.pop(-1)  # 마지막 원소 제거


def solution(numbers, target):
    global ans
    func(0, numbers, [], target)
    return ans