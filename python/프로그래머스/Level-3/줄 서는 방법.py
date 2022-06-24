from math import factorial 
def solution(n, k): 
    answer = [] 
    num = list(range(1,n+1)) 
    while n!=0 :
        fact = factorial(n-1)
        answer.append(num.pop((k-1)//fact))
        n -= 1
        k %= fact 
    return answer

n = 3
k = 5
print(solution(n, k))

'''
이문제를 permutations를 사용해 풀면 시간초과가 나온다
수학적 계산으로 풀수가 있는데 
구하고자하는 순서인 k를 (n-1)!를 나눈 몫이 구하고자하는
순서의 맨앞 숫자가 된다 그리고 n을 줄여서 팩토리얼 값을 
줄이고 k번째순서를 fact로 나눈 나머지를 개신하면
순서대로 값이 나온다
'''