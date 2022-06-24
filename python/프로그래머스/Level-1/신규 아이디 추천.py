import re

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9\-\_\.]', '', new_id)
    # ^는 제거하는것이 아닌 남기는 것이다 특수 문자는 \를 붙여야한다
    answer = new_id[0]
    for i in range(1, len(new_id)):
        if answer[-1] == '.' and new_id[i] == '.':
            continue
        else:
            answer += new_id[i]
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) >= 1:
        if answer[-1] == '.':
            answer = answer[:-1]
    if answer == "":
        answer += "a"
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) < 3:
        while len(answer) < 3:
            answer += answer[-1]

    return answer


s = "z-+.^."
print(solution(s))

'''
7가지 조건식을 만족하면 풀린다
'''
