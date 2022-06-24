def solution(p, l):
    answer = 0
    cnt = 0
    p_index = [0] * len(p)
    p_index[l] = 1 
    while True:
        if p[0] == max(p):
            cnt += 1
            if p_index[0] == 1:
                return cnt
            else:
                del p[0]
                del p_index[0]
        else:
            p.append(p[0])
            del p[0]
            p_index.append(p_index[0])
            del p_index[0]


    return answer

p = [1, 1, 9, 1, 1, 1]	
l = 0
print(solution(p,l))

'''
백준사이트 프린터 큐와 95프로 흡사한 문제이다
'''

