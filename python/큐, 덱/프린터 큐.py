''' 
프린터 큐
'''

t = int(input())
# 테스트 개수
for i in range(t):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    s_ = [0 for i in range(n)]
    s_[m] = 1
    # s_라는 리스트를 따로 생성 찾고자 한는 인덱스에 1을 부여
    cnt = 0
    # 몇번째로 인쇄되는지
    while True:
        if s[0] == max(s):
            # 가장큰수가 가장 앞에 올경우
            cnt += 1
            # 찾고자하는 값이 몇번째인지 세기 위한 값
            if s_[0] == 1:
                print(cnt)
                break
            # 찾고자 하는 값을 찾으면 출력후 종료
            else:
                del s[0]
                del s_[0]
            # 찾고자하는 값을 찾을떄까지 수를 뺌
        else:
            s.append(s[0])
            del s[0]
            s_.append(s_[0])
            del s_[0]
            # 가장큰수가 가장 앞에 올때까지 수를 뺴고 삽입
