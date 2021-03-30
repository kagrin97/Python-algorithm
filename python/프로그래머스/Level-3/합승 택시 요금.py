def solution(n, s, a, b, fares):
    INF = int(1e9) # 무한을 표시한수 1e9은 소수로 표시됨으로 int로 바꿔줌                                 
    graph = [[INF] * n for _ in range(n)]			

    for i in range(n):                              
        graph[i][i] = 0 # 자기 자신의 노드로 가는 비용은 0으로 바꿔줌

    for i in fares:
        graph[i[0] - 1][i[1] - 1] = i[2] # 출발 -> 도착 = 비용   
        graph[i[1] - 1][i[0] - 1] = i[2] # 도착 -> 출발 = 비용		
    
    for t in range(n): # 플로이드를 위한 3중 for문
        for i in range(n):
            for j in range(i, n): # 범위를 n으로만 지정한것보다 i,n이 2배는 빠르다          
                if i != j: # 자기 자신으로가는 노드가 아닐때                         
                    graph[i][j] = graph[j][i] = min(graph[i][j], graph[i][t] + graph[t][j]) # 플로이드 와샬
                    
    answer = INF
    for t in range(n): # t는 경유해가는 노드를 의미                           
        temp = graph[s-1][t] + graph[t][b-1] + graph[t][a-1]       
        answer = min(answer, temp)

    return answer

n = 6 
s = 4 
a = 6 
b = 2 
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], 
        [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))

'''
이문제는 노드의수가 적어서 플로이드 와샬을 사용해도 된다
21번쨰줄은 t는 경유해가는 노드이고 해석을 하면 
(시작노드 s -> 경유노드 t) + (경유노드 t -> b ) + (경유노드 t -> a) = 총 비용
'''