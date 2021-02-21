import math

def solution(n):
    answer = 0
    sqrt = math.sqrt(n)

    if sqrt % 1 == 0:
        answer += int((sqrt + 1) ** 2)
        # % 1을 했을때 0이 나오면 딱 떨어지는 제곱근이다
    else:
        return -1

    return answer 
       
n = 121
print(solution(n))


'''
위 문제는 제곱근을 구하는 방법인데 2가지 방법이 있다
1. math.sqrt 함수를 사용하는 방법
2. n ** (0.5) 를 사용하면 제곱근을 구할수있다
'''
