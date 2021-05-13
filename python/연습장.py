case = 1
while 1:
  L, P, V = map(int, input().split())
  if L + P + L == 0:
    break
  
  res = (V//P) * L
  res += min((V%P), L)
  print(f'Case {case}: {res}')
  case += 1
  

