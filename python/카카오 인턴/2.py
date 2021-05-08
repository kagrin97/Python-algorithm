def kan(t1, t2, places):
    for i in range(t1[0], t2[0]+1):
        if t1[1] <= t2[1]:
            for j in range(t1[1], t2[1]+1):
                
                if places[i][j] == 'X':
                    return False
        else:
            for j in range(t2[1], t1[1]+1):
                
                if places[i][j] == 'X':
                    return False
    return True
        
def check(p_info, places):
    for i in range(len(p_info)):
        for j in range(i+1, len(p_info)):
            if abs(p_info[i][0] - p_info[j][0]) + abs(p_info[i][1] - p_info[j][1]) <= 2:
                if kan(p_info[i], p_info[j], places):
                    
                    return True
    return False

def solution(places):
    answer = []
    for k in range(5):
        p_info = []
        for i in range(5):
            for j in range(5):
                if places[k][i][j] == 'P':
                    p_info.append([i, j])

        if check(p_info, places[k]):
            answer.append(0)
        else:
            answer.append(1)
    
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], 
["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))