import heapq
def solution(scoville, k):
    heapq.heapify(scoville) # 리스트를 힙 형태로 변환 
    count = 0

    while scoville[0] < k: # 힙 최소값이 k보다 작을때만
        try:
            sum_num = 0       
            sum_num += heapq.heappop(scoville)
            sum_num += heapq.heappop(scoville) * 2
            heapq.heappush(scoville, sum_num)
            count += 1
        except IndexError: # 리스트에 더이상 남은게 없는 오류 IndexError
            return -1

    return count

s = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(s, k))

'''
위 문제는 항상 리스트에서 최소값을 찾아야 하는데
sort를 쓰면 시간복잡도가 너무 커서 heapq를 썻다
힙은 자동으로 오름차순으로 정렬을 해준다
'''