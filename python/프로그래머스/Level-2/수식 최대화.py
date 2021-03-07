from itertools import permutations
from copy import deepcopy

def solution(expression):
    answer = 0
    new1 = []
    sub = ''
    for i in expression:
        if i == '+' or i == '-' or i == '*':
            new1.append(int(sub))
            sub = ''
            new1.append(i)
        else:
            sub += i
    new1.append(int(sub)) # 숫자와 연산자를 따로 떼어서 리스트에 넣는다
    for i in permutations(['*', '+', '-']): # 3가지로 할수있는 모든 조합
        order = i
        flag = 0
        new = deepcopy(new1) # deepcopy를 쓰면 new와 new1은 서로 완전히 다르게 존재하게 된다
        for op in order:
            idx = 1 
            while 1:
                if idx >= len(new): # 리스트총 길이와 idx가 같거나 넘으면 종료
                    break
                elif new[idx] == op: # 만약 연산자이면
                    if op == '-': 
                        new[idx] = new[idx - 1] - new[idx + 1] 
                    elif op == '+':
                        new[idx] = new[idx - 1] + new[idx + 1]
                    else:
                        new[idx] = new[idx - 1] * new[idx + 1]
                    new = new[:idx - 1] + [new[idx]] + new[idx + 2:] # 연산후 앞뒤로 잘라서 새로운 new 만듬
                    if len(new) == 1: # 리스트에 남은 수가 1나 이면
                        answer = max(answer, abs(new[0])) # 지금까지 존재하는 값중 max값 갱신
                        flag = 1 # 탈출 계획을 세움
                        break
                else:
                    idx += 1 # op가 연사자가 아닌 숫자라면 인덱스 늘려줌
            if flag: # 탈출계획을 들으면 탈출후 다른 연산자 조합으로 다시 시작
                break
    return answer

b = "100-200*300-500+20"
print(solution(b))