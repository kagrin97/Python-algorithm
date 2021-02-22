def solution(n):
    answer = ''
    
    while n > 0:
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
    return answer

n = 8	
print(solution(n))

'''
위 문제는 3진법으로 풀었다
'''



