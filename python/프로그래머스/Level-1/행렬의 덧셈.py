def solution(arr1, arr2):
    
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    
    return arr1

n = [[1,2],[2,3]]
m = [[3,4],[5,6]]	
print(solution(n, m))

'''
answer의 존재를 너무 의식한나머지 arr1에 덮어쓰면 된다는 개념을 깜빡
하고 말았다 ㅠㅠ
'''






