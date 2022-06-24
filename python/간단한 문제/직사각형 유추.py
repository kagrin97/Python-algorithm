def solution(v):
    x = []
    y = []
    answer = []
    for i in range(3):
        x.append(v[i][0])
        y.append(v[i][1])
     
    if x[0] != x[1] and x[0] != x[2]:
        answer.append(x[0])
    elif x[1] != x[0] and x[1] != x[2]: 
        answer.append(x[1])
    elif x[2] != x[0] and x[2] != x[1]:
        answer.append(x[2])

    if y[0] != y[1] and y[0] != y[2]:
        answer.append(y[0])
    elif y[1] != y[0] and y[1] != y[2]: 
        answer.append(y[1])
    elif y[2] != y[0] and y[2] != y[1]:
        answer.append(y[2])
    return answer
    

v = [[1, 4], [3, 4], [3, 10]]
print(solution(v))

'''
3개의 좌표가 주어지고 나머지 한가지 좌표를 유추하는 문제이다
(3개의 좌표는 직사각형의 각 꼭짓점이다)