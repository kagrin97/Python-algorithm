def solution(s):
    answer = -1
    x = len(s)
    cnt = 0
    for i in range(x):
      stack = []
      flag = True
      if i != 0:
        s += s[0]
        s = s[1:]
      
      for k in range(len(s)):
        if s[k] == '(' or s[k] == '[' or s[k] == '{':
          stack.append(s[k])
        else:
          try:
            if s[k] == ')' and '(' == stack[-1]:
              stack.pop()
            elif s[k] == ']' and '[' == stack[-1]:
              stack.pop()
            elif s[k] == '}' and '{' == stack[-1]:
              stack.pop()
            else:
              flag = False
              break
          except:
            flag = False
            break
      
      if flag and not stack:
        cnt += 1

    return cnt

s = "([{)}]"
print(solution(s))