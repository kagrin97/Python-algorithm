def solution(n):
    answer = 0


    for i in range(1, n + 1):
        if n % i == 0:
            answer +=i
    return answer

n = 5
print(solution(n))

'''
n의 약수를 구하는 방법은
n % i == 0 이 될때만 i가 n의 약수라고 할수가 있다
'''