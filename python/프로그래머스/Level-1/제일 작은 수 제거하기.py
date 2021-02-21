def solution(arr):
    if not arr or len(arr) == 1:
        return [-1]
    
    arr.remove(min(arr))
    # 특정값을 지우고 싶으면 remove를 사용
    return arr 

              
n = [4,3,2,1]
print(solution(n))

'''
정수를 저장한 배열, arr 에서 가장 작은 수를 
제거한 배열을 리턴하는 함수, solution을 완성해주세요. 
단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 
예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, 
[10]면 [-1]을 리턴 합니다.
'''
