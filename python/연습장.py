def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            print(temp,1)
            temp_list.append(f'({b.join(temp)})')
            print(temp_list,2)
        answer.append(abs(eval(a.join(temp_list))))
        print(temp_list,3)
    return max(answer)

b = "100-200*300-500+20"
print(solution(b))