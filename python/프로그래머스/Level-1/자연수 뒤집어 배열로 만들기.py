def solution(n):
    answer = []
    n = str(n)

    for i in range(len(n)):
        answer.append(int(n[i]))

    answer.reverse()
    return answer

n = 12349087
print(solution(n))

"""
위 문제는 내림차순으로 정렬하는줄 착각을 했었다
내림차순이 아닌 n값을 거꾸로 뒤집는 것이다
12349087 -> 78094321
"""
