def solution(land):
 
    answer = 0
 
    for i in range(len(land)-1):
 
        land[i+1][0] += max(land[i][1],land[i][2],land[i][3])
        # dp문제로 각칸마다 최대가 될수 있는 값을 넣어준다
        land[i+1][1] += max(land[i][0],land[i][2],land[i][3])
        land[i+1][2] += max(land[i][0],land[i][1],land[i][3])
        land[i+1][3] += max(land[i][0],land[i][1],land[i][2])
   
    answer = max(land[-1]) 

    return answer

s = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(s))

'''
이 문제는 dp문제로 열이 정해져 있어서 가능한 문제이다
'''


