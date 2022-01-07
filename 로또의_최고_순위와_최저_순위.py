def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    zeros = lottos.count(0)
    cnt = 0
    for num in lottos:
        if num in win_nums:
            cnt += 1
    return [rank[zeros + cnt], rank[cnt]]


if __name__ == '__main__':
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    print(solution(lottos, win_nums)) 
    # [3, 5]