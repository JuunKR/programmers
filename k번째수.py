def solution(array, commands):
    return [sorted(array[a-1:b])[c-1] for a,b,c in commands]

if __name__ == '__main__':
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    
    print(solution(array, commands))
    # [5, 6, 3]
    
