def solution(sizes):
    wallet_width = 0
    wallet_height_list = []  # height가 될 수 있는 후보를 저장하는 list

    # 1. sizes 배열 안에서 최댓값을 뽑아낸다
    for width, height in sizes:
        tmp = max(width, height)  # width, height 중에서 max 값을 뽑는다
        wallet_width = max(tmp, wallet_width)  # wallet_width를 갱신한다

    # 2. sizes를 탐색하면서 height가 될 수 있는 값들을 저장한다
    for width, height in sizes:
        wallet_height_list.append(min(width, height))

    # height를 선정한다
    wallet_height = max(wallet_height_list)

    return wallet_width * wallet_height