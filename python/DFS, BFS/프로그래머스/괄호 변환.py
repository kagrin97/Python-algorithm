def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
            # 검사해서 균형 잡힌게 끝날 경우 끝난 index 값 반환 

def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True
    # 문자열u를 검사해서 올바를경우 true, 아니면 false 반환

def solution(p):
    answer = '' # 빈 문자열 생성
    if p == '': # 빈 문자열 일경우 빈 문자열 반환
        return answer
    index = balanced_index(p) # 문자열을 검사해서 균형잡힌게 끝날때 값을 가져옴
    u = p[:index + 1] # 균형 잡힌 문자열
    v = p[index + 1:] # 그 뒤의 문자열 v
    if check_proper(u): 
        answer = u + solution(v) # u가 올바른 문자열이면 v도 솔루션후 합침
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = "("
        answer += "".join(u)
        # u가 올바르지 않으면 "("+v+")"와 u 앞뒤를 자르고 괄호를 반전 시킨
        # 값을 둘이 더 해줌 

    return answer

p = "()))((()"
print(solution(p))