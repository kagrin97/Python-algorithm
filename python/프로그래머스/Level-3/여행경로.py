def solution(tickets):
    tickets.sort(reverse=True) #사전에 거꾸로 넣어서 거꾸로 뽑기위함
    routes = dict()
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2) # 키가 있으면 리스트에 추가
        else:
            routes[t1] = [t2] # 딕셔너리안에 리스트를 만듦
    start = ['ICN']
    result = []

    while start:
        now = start[-1] 
        if now not in routes or len(routes[now]) == 0: # 첫번쨰 결과 값이 완성된 상태라면
            result.append(start.pop()) # 밑에서 만든 첫번째결과물 값을 모두 뺴야지 while문이 종료되기떄문에 이코드를 만듦
        else:
            start.append(routes[now].pop()) # 첫번째 결과 값을 만듦
        
    result.reverse() # 완성된코드를 뒤집으
    return result


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))

'''
위문제는 최단거리가아닌 모든 여행권을 소모해야한다
모든 곳을 다가봐야한다 그리고 갈수있는 곳이 여러곳일 경우
사전순으로 실행을 한다
그리고 이문제의 경우 while문을 평범하게 start.pop()를 하고 result를 하게
되면 start에 아무런 값이 남지가 않기때문에 억지로 start에 값을 넣기위해서
첫번째 완성품을 완성하고 start값을 다빼서 다시 리버스를 해줘야 한다
'''