import heapq
def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1 # 9번째줄 if문을 실행해주기 위한 -1
    heap = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now: # 시작시간이 start보다 크고 now보다 작거나 같아야함
                heapq.heappush(heap, [j[1], j[0]]) # 소요시간기준으로 힙을 만들어줌
        if len(heap) > 0: # 시작할수있는 일이 있으면
            current = heapq.heappop(heap) # 일을 빼서 넣음
            start = now # 시작시간 갱신
            now += current[0] # 현재시간 갱신
            answer += (now - current[1]) # 소요시간 - 시작시간
            i += 1 
        else:
            now += 1 # 시작할수있는 일이 없으면 현재를 늘려줌
    
    return int(answer / len(jobs))

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))

'''
힙을 사용한 이유는 시작시간이 똑같은 디스크가 있을
수가 있기때문에 시작시같이 같아도 소요시간이 짧은
디스크부터 처리하기위해 heap을 이용했다
'''

