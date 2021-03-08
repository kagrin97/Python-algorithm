def solution(n):
    battery = 0

    while n > 0:
        battery += n % 2 
        n //= 2 

    return battery 

n = 5000
print(solution(n))

'''
n을 2로 나눈값이 순간이동 가능 값이 되는데 만약 0이 아니라면
나머지만큼 점프를 해야하기 때문에 배터리를 소모해 점프하고
다시 순간이동해 총거리를 2로 나눈다
'''