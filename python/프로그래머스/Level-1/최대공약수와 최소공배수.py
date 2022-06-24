from math import gcd

def solution(n, m):
    answer = []
    answer.append(gcd(n,m)) # 최대공약수 구하는법
    answer.append(n * m // gcd(n, m)) # 최소공배수 구하는법
    return answer


n = 3
m = 12
print(solution(n,m))


