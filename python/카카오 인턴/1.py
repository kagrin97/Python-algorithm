def solution(s):
    answer = 0
    tmp = ''
    result = ''
    alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(s)):
        try:
            if int(s[i]):
                result += s[i]
        except:
            tmp += s[i]
        if tmp in alpha:
            for i, v in enumerate(alpha):
                if v == tmp:
                    result += str(i)
                    tmp = ''
                
            

    return int(result)

s = "one4seveneight"
print(solution(s))