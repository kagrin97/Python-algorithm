'''블랙잭 : 브루트 포스'''

n, m = map(int, input().split())
''' 카드수n 와 최대값m '''
num = list(map(int, input().split()))
'''카드 리스트 입력'''
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if num[i] + num[j] + num[k] > m:
                continue
            '''3장의 카드합이 넘어갈경우 아무일도 일어나지않음'''
            else:
                result = max(result, (num[i] + num[j] + num[k]))
            '''그전 카드합과 현카드합중 더 높은 값을 저장'''
print(result)
