def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    zeros = lottos.count(0)
    cnt = 0
    for num in lottos:
        if num in win_nums:
            cnt += 1
    return [rank[zeros + cnt], rank[cnt]]



