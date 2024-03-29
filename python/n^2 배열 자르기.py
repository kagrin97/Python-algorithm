def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        a = i // n  # 몫
        b = i % n  # 나머지

        if a < b:
            answer.append(b + 1)
        else:
            answer.append(a + 1)

    return answer

n = 4
left = 7
right = 14

print(solution(n, left, right))