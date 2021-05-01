bar_razor = list(input())
answer = 0
stack = []

for i in range(len(bar_razor)):
    if bar_razor[i] == '(':
        stack.append('(')
    else:
        if bar_razor[i-1] == '(':
            stack.pop()
            answer += len(stack) # 짤라진 막대의 개수
        else:
            stack.pop()
            answer += 1 #꼬다리 더해줌
print(answer)

'''
붙어있는 괄호 '()' : 현재 위치에서 존재하는 쇠막대기를 절단한다.
떨어진 괄호   '('    : 쇠막대기를 새로 생성한다.
떨어진 괄호   ')'    : 쇠막대기가 끝난다.

이문제는 위의 조건만 알면 쉬운문제이지만 그 조건을 알기 어렵다
붙어있는괄호가 나오면 (를 개수가 잘려진 막대의 개수가 되고 
)가 나왔는데그전이 (가 아니라면 막대의 꼬다리 부분이기 때문에 막대를 += 1를
해준다
'''