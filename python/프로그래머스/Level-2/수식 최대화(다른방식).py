def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)

b = "100-200*300-500+20"
print(solution(b))

'''
eval함수는 eval('100'+'200") = 300이 나오도록
문자열이 있어도 자동으로 int로 계산을 해준다 하지만 오히려 
그때문에 권한이 너무 쎄서 해킹에 매우 취약한 함수이다
'''