def solution(s):
    answer = ''
    mid = len(s) // 2 
    if len(s) % 2 == 0: # 짝수라면
        answer += s[mid-1] # 가운데 두글자를 넣어줌
        answer += s[mid]
    else:
        answer += s[mid]
    return answer

s = "qwer"	
print(solution(s))
