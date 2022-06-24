def solution(s):
    answer = ''
    s = s.split(' ')
    
    for i in s:
        answer += i.capitalize() + " "

    answer =  answer[:-1] # 맨 마지막이 공백이기 때문에 공백을 제거
    return  answer

a = "3people unFollowed me"

print(solution(a))

'''
문자열 첫문자만 대문자로 바꿔준다
숫자가 첫문자이면 대문자로 바꾸지 않는다
'''

