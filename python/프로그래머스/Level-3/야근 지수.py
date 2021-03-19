import heapq

def solution(n, works):
    answer = 0
    heap=[]

    for work in works:
        heapq.heappush(heap, (-work, work)) # [(-4, 4), (-3, 3), (-3, 3)]
                                            # 위와 같이 넣어준다 
    while True:
        if n == 0: # 남은 시간이 없으면 종료
            break
        work = heapq.heappop(heap)[1] - 1 # heap의[1]값이 진짜 작업량값이며 거기서 -1해준다
        heapq.heappush(heap, (-work, work)) # 갱신
        n -= 1    # 남은 시간 감소

    for h in heap:
        if h[1] < 0: # -값일경우 실행 x
            continue
        answer += h[1] ** 2  # 제곱해서 값에 추가해준다

    return answer

n = 4
work = [4, 3, 3]
print(solution(n, work))

'''
이 문제의 경우 가장큰수를 어떻게든 작게만들어야 제곱값이 훨씬 적어지기
때문에 가장큰수를 -1씩 빼준다 일반적인 방법으로 정렬하거나 max를 하면 
시간초과가 나기 때문에 heap을 이용해 최대힙을 구현해 준다
18번줄 같은 경우는 모든 work값들이 -값이 라는 말이기 때문에
-를 제곱할경우 양수가 되버리기 때문에 결과 값이 커진다
그렇기 때문에 아무런 행동도 취해주지 않는 방법이다(안할경우 테케 13틀림) 
'''