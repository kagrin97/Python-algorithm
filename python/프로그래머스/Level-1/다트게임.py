import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    # 리스트 형태로 돌려줌 
    # [('0', 'D', '#'), ('7', 'S', '*'), ('0', 'T', '')]
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    return sum(dart)

        
n = "0D#7S*0T"	
print(solution(n))

'''
https://blog.naver.com/hands731/221874947799
위 주소가 정규 표현식에대해 설명한다
'''


