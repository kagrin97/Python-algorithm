class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if stack:
                    if s[i] == ')' and '(' == stack[-1]:
                        stack.pop()
                    elif s[i] == ']' and '[' == stack[-1]:
                        stack.pop()
                    elif s[i] == '}' and '{' == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
    
        if stack:
            return False
        return True

'''
이 문제는 괄호 문제인데 무조건 괄호를 닫을때 바로 전에 여는 괄호가
있어야 한다
'''