def solution(n, computers):
    answer = 0 # 네트워크 개수를 저장할 곳
    bfs = [] # 탐색을위함
    visited = [0]*n # 방문했는지 여부

    while 0 in visited: # 0이 없을때까지 
        x = visited.index(0) # visited안에 0의 인덱스
        bfs.append(x) # 해당 인덱스값 삽입
        visited[x] = 1 # 방문완료
        
        while bfs:
            node = bfs.pop(0) # 연결된 컴퓨터들 검사
            visited[node] = 1 # 방문 완료
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1: #연결되있고 방문한적x일 경우
                    bfs.append(i) # 연결되 있는 컴퓨터 추가
                    visited[i] = 1 # 방문 기록함
        answer += 1 # 한복 끝날때마다 연결이 끊긴거임
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))

