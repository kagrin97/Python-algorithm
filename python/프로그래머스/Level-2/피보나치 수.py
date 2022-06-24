def solution(n):
    pibo = [0] * (n+1)
    pibo[0] = 0
    pibo[1] = 1

    for i in range(2, len(pibo)):
        pibo[i] = (pibo[i-1] + pibo[i-2])
        
    return pibo[-1] % 1234567

a = 5
print(solution(a))

