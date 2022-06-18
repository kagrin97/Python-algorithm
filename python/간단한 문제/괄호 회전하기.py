def check(s):
  stack = []
  for i in s:
    if not stack:
      stack.append(i)
    elif stack[-1] == '(' and i == ')':
      stack.pop()
    elif stack[-1] == '[' and i == ']':
      stack.pop()
    elif stack[-1] == '{' and i == '}':
      stack.pop()
    else:
      stack.append(i)

  if stack:
    return False
  else:
    return True


def solution(s):
  cnt = 0

  if len(s) == 1:
    return 0

  if check(s):
    cnt += 1

  for i in range(len(s) - 1):
    s = s[1:] + s[0]
    if check(s):
      cnt += 1
  return cnt

s = "([{)}]"
print(solution(s))