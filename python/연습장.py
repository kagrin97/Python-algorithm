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
    if before[i] != after[i]:
      before_tmp.append(before[i])
      after_tmp.append(after[i])
  
  

  for i in range(len(before_tmp)):
    if before_tmp[i] == after_tmp[i]:
      ans += 0.5
    else:
      ans += 1
  
  print(int(ans))

  
