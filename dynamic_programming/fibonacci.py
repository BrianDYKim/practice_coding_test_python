dp_table = [0] * 100

def fibo(x):
    # 만약에 1, 2인 경우 바로 리턴을 해준다
    if x == 1 or x == 2:
        dp_table[x] = 1
        return 1

    # 만약에 이미 계산된 경우 dp_table에서 return해준다
    if dp_table[x] != 0:
        return dp_table[x]

    # 이전에 계산된 적이 없다면 새로 계산해준다
    dp_table[x] = fibo(x - 1) + fibo(x - 2)
    return dp_table[x]

print(fibo(9))