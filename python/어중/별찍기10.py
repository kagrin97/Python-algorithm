'''별찍기 10'''

import sys
'''sys stdout.write은 프린트문과 달리 띄어쓰기를 안하고 연속적으로 보여준다'''


def draw(x, y):
    while x != 0:
        '''x가 0이라면 while문을 나가 별을 찍는다'''
        if (x % 3) == 1 and (y % 3) == 1:
            '''x,y를 3으로 나눈값이 1이면 공백을 하나 찍는다 (1,4,7)'''
            sys.stdout.write(' ')
            return
        x = x // 3
        y = y // 3
        '''x,y를3으로 나누고 while을 돌렸을때 둘다 x,y 가1일경우 공백을 찍는다
        (3,4,5) <--가운데 빈공간을 생산한다'''

    sys.stdout.write('*')


n = int(input())
'''3의 배수를 입력 받는다'''
for i in range(n):
    for j in range(n):
        draw(j, i)
    sys.stdout.write('\n')
    '''한줄이 끝나면 다음으로 넘어가기위함'''
