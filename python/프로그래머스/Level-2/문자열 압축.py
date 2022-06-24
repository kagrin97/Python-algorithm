def solution(s):
    length = []
    result = ""

    if len(s) <= 2:
        return len(s)
        # 만약 2이하의 길이라면 return len(s)
    for cut in range(1, len(s) // 2 + 1): # 1씩자르는것부터 반씩 짜르는것 까지
        count = 1
        tempStr = s[:cut] # 초기에 자른 값 (제일 앞의 수)
        for i in range(cut, len(s), cut): # 잘라주기
            if s[i:i + cut] == tempStr: # 그전값(tempStr) 과 그다음 자른 값이 같으면
                count += 1
            else:
                if count == 1: # 전값과 지금값이 다르면 
                    count = "" # 빈 문자열
                result += str(count) + tempStr # aa -> 2a
                tempStr = s[i:i + cut] # 자른값 갱신
                count = 1 # 초기화
        
        if count == 1: # 마지막 문자열을 위한 if문
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        result = ""
    return min(length)
        
s = "aaabbacc"
print(solution(s))

'''
이 문제는 자를수있는 최소 단위가 s의 절반 단위 인것부터 눈치채야 한다
''' 



