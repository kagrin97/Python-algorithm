'''
1번 정답은 하나씩 빼기 때문에  느리고 100억이상 되는 수를 가정했을때 빠르게 동작
하기위해서 n이 k의 배수가 되는 빠른 방식의 소스코드
'''

n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k # n이 k의 배수가 되는 수 구하기
    result += (n - target) # n이 k의 배수가 된 수를 뺀 값 즉 횟수를 저장
    n = target # n에 k의 배수가된 n을 저장
    if n < k: # n이 k로 나눠지지 않을떄 탈출
        break
    result += 1 
    n //= k # n // k 나눈 값을 n에 저장및 횟수 추가

result = (n - 1) # 나눠지지 않는 n이 1 이 될떄까지 뺀 횟수 저장
print(result)