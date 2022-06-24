def solution(s):
    answer = []

    for i in range(len(s)):
        tmp_str = ''
        tmp_str += s[i]
        for j in range(i+1, len(s)+1):
            if tmp_str == tmp_str[::-1]: # 앞뒤를 바꿔도 똑같은지 확인법
                answer.append(len(tmp_str))
                try:
                    tmp_str += s[j]
                except:
                    pass
            else:
                try:
                    tmp_str += s[j]
                except:
                    pass

    return max(answer)

n = "토마토맛토마토"	
print(solution(n))