def solution(n):
    answer = 0

    for s in range(1, n):
        tmp = 0
        for i in range(s, n):
            if tmp > n:
                break
            elif tmp < n:
                tmp += i
        if tmp == n: # 다 검사후 목표 n과 일치하면 + 1
            answer += 1

    return answer + 1

n = 15
print(solution(n))