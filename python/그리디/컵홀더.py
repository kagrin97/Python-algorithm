N = int(input())
seat = input()

cnt = seat.count('LL')

if cnt <= 1:
    print(len(seat))
else:
    print(len(seat) - cnt + 1)

'''
여러 경우의 수를 생각하다 보니, 커플석 (LL)의 수에 따라 출력이 변하였습니다.
커플석 (LL)이 2자리 이상일 때, 커플석이 한 자리 많아질수록 한 명이 컵홀더를 사용할 수 없습니다.
구현을 해보자면,
먼저 N과 seat를 입력 받습니다. 그리고 seat에서 커플석(LL)이 몇 개인지 count해줍니다.
만약 LL이 1개 또는 0개라면 사람의 수를 그대로 출력합니다. (모두 컵홀더 사용 가능)
만약 LL이 2개 이상이라면 count를 빼주고 1을 더해줍니다. (LL이 2개면 -1, LL이 3개면 -2 이므로)
'''