'''
1. n과 k 가 주어진다
2. n이 1이 될때까지 1씩 빼거나 k의 배수일 경우 n을 k로 나눈다
3. 1씩뺀 횟수와 한번씩 나눈 횟수를 다 더해서 1이되는 최소 횟수를 구하라
'''

n, k = map(int, input().split())

count = 0

while n >= k: # n이 k 이상이라면 실행
    while n % k != 0: # n이 k의 배수가 아니라면 1씩빼고 횟수 추가
        n -= 1
        count += 1
    n //= k # 배수가 됬을때 몫을 저장 및 횟수 추가
    count += 1

while n > 1: # n이 k보다 작고 1보다는 클때 1씩 뺴고 횟수 추가
    n -= 1
    count += 1

print(count)
