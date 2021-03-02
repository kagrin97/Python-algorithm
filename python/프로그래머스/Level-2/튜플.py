def solution(s):
    answer = []
    s = s[2:-2] # 앞뒤 {}를 지워준다
    s = s.split('},{') # }{를 기준으로 나눠줌
    s.sort(key = len) # 길이로 정렬
    for i in s:
        li = i.split(',') # ,를 기준으로 나눔
        for j in li:
            if int(j) not in answer:
                answer.append(int(j))
                # 하나씩 검사후 answer안에 없을시 삽입

    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))

