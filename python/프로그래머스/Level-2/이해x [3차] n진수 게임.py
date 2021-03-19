def solution(n, t, m, p):
    answer = '0'
    mapper = '0123456789ABCEDF'
    target = 1

    while len(answer) < t * m:
        temp_number = target
        temp_answer = ""
        while temp_number:
            temp_answer = mapper[temp_number % n] + temp_answer
            temp_number //= n
        answer += temp_answer
        target += 1
    return answer[p - 1: t * m: m]


n = 16
t = 16
m = 2
p = 2
print(solution(n, t, m, p))