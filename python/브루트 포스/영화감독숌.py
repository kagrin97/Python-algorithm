'''
브루트 포스 영화감독 숌
'''


n = int(input())
# 영화 시리즈 몇번쨰인지 입력을 받는다

m = 666
# 실질적인 시리즈 넘버 카운팅용
while n:
    # n이 0이되면 멈춤
    if '666' in str(m):
        # m값이 666을 만날때마다 n을 1씩 줄인다
        n -= 1
    m += 1
    # m값을 1씩올리기 때문에 다음 666을 만날때까지 1을계쏙 더한다

print(m-1)
