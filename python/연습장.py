from collections import deque

def solution(n, edge):
    def bfs():
        de = deque()
        de.append(1)
        
        while de:
            x = de.popleft()
    
            for i in node[x]:
                if ch[i] == -1:
                    ch[i] = ch[x] + 1
                    de.append(i)
                
    node = [[] for i in range(n + 1)]
    ch = [-1] * (n + 1)
    
    for i, j in edge:
        node[i].append(j)
        node[j].append(i)
        
    ch[1] = 0
    bfs()
    return ch.count(max(ch))

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
print(solution(n, vertex))

