def solution(x, n):
    answer = []

    if x < 0:
        for i in range(x, x * n-1, x):
            answer.append(i)
    elif x > 0:
        for i in range(x, x * n+1, x):
            answer.append(i)
    else:
        return [0]*n
    return answer


n = 0
m = 5
print(solution(n, m))

"""
함수 solution은 정수 x와 자연수 n을 입력 받아, 
x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 
다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

x가 0일경우 n번만큼 반복한다 위의예 : [0, 0, 0, 0, 0]
"""





