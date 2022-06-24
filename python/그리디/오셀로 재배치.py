T = int(input())
for _ in range(T):
  N = int(input())
  before = input()
  after = input()
  cnt = 0
  Bcnt = 0
  Wcnt = 0
  ans = 0
  before_tmp, after_tmp = [], []

  for i in range(N):
    if before[i] != after[i]: # 같은 위치에 다른 돌이 있으면 추가해준다
      before_tmp.append(before[i])
      after_tmp.append(after[i])
  
  before_tmp.sort() # 정렬을해야지 같은 돌끼리 비교가능
  after_tmp.sort()

  for i in range(len(before_tmp)):
    if before_tmp[i] == after_tmp[i]: # 같은 돌일경우 돌끼리 교체가능
      ans += 0.5
    else: # 다른 돌일 경우 무조건 뒤집어야함
      ans += 1
  
  print(int(ans))

'''
이문제는 WBBWW, WBWBW 가 입력값으로 주어지면
각 정렬한 리스트는 BW, BW 가 된다. 두개의 인덱스는
 모두 같은 값이므로 0.5가 두 번 더해져 결과값이 1이된다.
BBBBBBB, BWBWBWB 가 입력값으로 주어지면
각 정렬한 리스트는 BBB, WWW 가 되고 3개의 인덱스가 모두 다른값이므로 결과값은 3이 된다
'''

  
