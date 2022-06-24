from collections import deque

def solution(n, edge):
    def bfs():
        de = deque()
        de.append(1) # 1부터 시작하기 위함
        
        while de:
            x = de.popleft()
    
            for i in node[x]:
                if ch[i] == -1: # 딱 한번씩만 실행되기 위함
                    ch[i] = ch[x] + 1 # ch[x]는 그전에 통과한 노드의 값이다
                    de.append(i) # 현재위치와 연결된 노드들 넣어줌
                
    node = [[] for i in range(n + 1)] # 각노드의 인덱스마다 그노드와 직결연결된 노드 값을 넣음
    ch = [-1] * (n + 1) # 계산하기 편하게 0번쨰를 사용x 길이를 1늘림
    
    for i, j in edge:
        node[i].append(j) # 노드를 넣어줌
        node[j].append(i)
        
    ch[1] = 0 # 1번노드부터 시작하기때문에 0으로 바꿔줌
    bfs()
    return ch.count(max(ch))

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
print(solution(n, vertex))

'''
위문제 13번쨰 줄의 ch[x]는 1번노드와 ch[i]번째 노드 사이에 연결된
노드의 값으로 i번쨰노드 = 1번노드와 x번째 노드의 거리 + 1
이다
16번쨰 줄에서 [[]] * (n+1)를 하고나서 19번째줄을 실행하면
모든 인덱스에 모든 값이 들어가는 오류가 발생한다
'''