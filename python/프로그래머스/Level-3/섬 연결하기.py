def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) # 가격을 기준으로 오름차순으로 정렬한다
    routes = set([costs[0][0]]) # 초기에 시작할 섬을 넣음
    
    while len(routes) != n: 
        for i, cost in enumerate(costs): # 0 [0,1,1] 같은 형태
            if cost[0] in routes and cost[1] in routes: # 둘다 set에 존재하면 갈 필요 x
                continue
            if cost[0] in routes or cost[1] in routes: # 한곳을 아직 안갔다는 의미이다 
                routes.update([cost[0], cost[1]]) # update는 set에 여러개 값을 넣는 함수
                answer += cost[2] 
                costs[i] = [-1, -1, -1] # 다시 실행시키지 못하게 갱신
                break 

    return answer

n = 4       
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))

'''
위 문제는 Kruskal은 탐욕법을 이용하여 네트워크의 정점을 최소비용으로 연결하는 것이다
set을 이용해 연결할수있는 섬을 체크하고(10번줄) 이미 연결된 섬을 체크한다(8번줄)
그리고 연결한섬을 실행조차 못시키게 값을 -1,-1,-1로 바꿔준다
'''

