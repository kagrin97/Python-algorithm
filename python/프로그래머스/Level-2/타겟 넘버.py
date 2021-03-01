def solution(numbers, target):
    tree = [0]

    for i in numbers:
        sub = []
        for j in tree:
            sub.append(j+i) # 더하거나
            sub.append(j-i) # 뺴거나
        tree = sub # 계속 갱신

    return tree.count(target)
    
numbers = [1, 2, 3, 4, 5]
target = 3
print(solution(numbers, target))

'''
이 문제는 0부터 시작해서 number안의 값들을 더하거나 뺴는
방식을 점차 늘려서 트리구조로 만든다
''' 
