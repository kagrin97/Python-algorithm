import math
def decimal(num): # 소수판별 제곱근까지 구해야 시간초과가 안남
    if num == 2 or num == 3:
        return True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def convert(n, base): # n진법으로 변환
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert(q, base) + T[r] if q else T[r]

def solution(n, k):
    li = convert(n, k).split('0')
    remove_set = {"1", ""}
    li = [i for i in li if i not in remove_set] # 배열안 특정 문자 모두 지우기

    cnt = 0
    for i in li:
        i = int(i)
        if decimal(i):
            cnt += 1
    return cnt
n = 437674
k = 3
print(solution(n, k))