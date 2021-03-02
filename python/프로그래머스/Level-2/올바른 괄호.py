def solution(s):
    bracket = []

    if s[0] == ')' or s[-1] == "(":
        return False

    for i in s:
        if i == '(':
            bracket.append(i)
        elif "(" in bracket:
            bracket.pop()
        else:
            return False
    
    if not bracket:
        return True
    
    return False

s = "(()("
print(solution(s))

'''
이 문제는 리스트에 ( 를 모두 넣고 )가 나온다면 
리스트에서 (을 뺴누는 방법으로 풀었다
마지막 return false는 만약 입력 받은 값에 아무것도 
안들어 있을 경우를 대비한 것이다
'''

