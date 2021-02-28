from itertools import permutations

def solution(numbers):
    answer = 0
    ss = []
    vv = []
    qq = []
    pp = []
    zz = []
    plag = True
    if int(numbers) <= 1:
        return 0

    for i in range(len(numbers)):
        ss.append(int(numbers[i]))
    
    for i in range(len(numbers)):
        vv.append(list(permutations(ss, i+1)))
    
    for i in range(len(vv)):
        for j in range(len(vv[i])):
            qq.append(''.join(map(str, vv[i][j])))

    for i in range(len(qq)):
        if qq[i] == '1' or qq[i] == '0' or qq[i][0] == '0':
            continue
        else:
            pp.append(qq[i])
    
    for v in pp:
        if int(v) not in zz:
            zz.append(int(v))
    
    for i in zz:
        for j in range(2, i):
            if i % j == 0:
                plag = False
                break
        if plag:
            answer += 1
        else:
            plag = True
        

    return answer

orders = "17"
print(solution(orders))
