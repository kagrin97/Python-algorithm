import sys
import heapq

numbers = int(sys.stdin.readline())
max_heap = []
min_heap = []

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, (num, num))
    
    if min_heap and max_heap[0][1] > min_heap[0][1]:
        temp_max = heapq.heappop(max_heap)[1]
        temp_min = heapq.heappop(min_heap)[1]
        heapq.heappush(max_heap, (-temp_min, temp_min))
        heapq.heappush(min_heap, (temp_max, temp_max))
    print(max_heap[0][1])

    '''
    시간이 0.6초 밖에 주어지지 않아서 우선순위큐로 풀면 시간초과가 난다
    그래서 힙을 두개로 쪼갰다.
    max힙에 제일큰값이 min힙 제일 작은 값보다 클 경우에는 그 두개의 값을
    서로 체인지 한다 15~19줄 max를 구현하기 위해 -값을 받고 출력할때
    는 본래의 값인 [0][1] 값을 출력해준다.
    설명 사이트: https://www.crocus.co.kr/625
    '''