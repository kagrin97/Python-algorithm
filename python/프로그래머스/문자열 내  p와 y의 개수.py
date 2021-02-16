def solution(s):
    s = s.lower()
    p_count = 0
    y_count = 0

    for i in range(len(s)):
        if s[i] == 'p':
            p_count += 1
        elif s[i] == 'y':
            y_count += 1
    
    if p_count == y_count:
        return True
    elif p_count == 0 and y_count == 0:
        return True
    elif p_count != y_count:
        return False
    
s = "pPoooyY"
n = 2
print(solution(s))

''' 
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 
False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 
항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
예를 들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.
'''


