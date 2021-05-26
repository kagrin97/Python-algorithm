import heapq
n, m = map(int, input().split())
card = list(map(int, input().split()))
heapq.heapify(card)

for _ in range(m):
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    c = a + b
    heapq.heappush(card, c)
    heapq.heappush(card, c)


print(sum(card))

'''
해당문제를 일반적인 pop으로 풀려고하면 시간 제한이 걸릴것 같아서
heap으로 풀었다
'''