def solution(absolutes, signs):
    return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))


if __name__ == '__main__':
    absolutes = [4,7,12]
    signs = [True, False, True]
    
    print(solution(absolutes, signs))
    # 9
