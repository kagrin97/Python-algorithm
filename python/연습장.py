def solution(s, n):
    answer = ''

    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
        elif ord(s[i]) == 90 or ord(s[i]) == 122:
            answer += chr(ord(s[i]) - 26 + n)
        elif 48 < ord(s[i]) < 122: 
             answer += chr(ord(s[i]) + n)
    return answer



a = "a B z"
b = 4	
print(solution(a, b))
