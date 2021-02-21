def solution(s, n):
    answer = ''

    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
        # 문자가 공백, 대문자, 소문자 밖에 없으니 아래는 대문자 아니면 소문자겠죠
        # 대문자일 경우
        elif 65 <= ord(s[i]) <= 90:
            # 아래 % 26 연산이 key 입니다.
            # 모든 문자들을 shift 한 후 다시 아스키코드로 바꾸어 줍니다
            tmp = (ord(s[i]) - 65 + n) % 26 + 65
            answer += chr(tmp)
        #  97 <= ord(s[i]) <= 122
        else: 
            tmp = (ord(s[i]) - 97 + n) % 26 + 97
            answer += chr(tmp)

    return answer

for i in range(1, 26):
    print(solution("abcdefghijklmnopqrstuvwxyz", i))
    print(solution("ABCDEFGHIJKLMNOPQRSTUVWXYZ", i))

'''
(ord(s[i]) - 65 + n) 65는 A의값이 65 이기때문에 자리수를 얻기위한 값이다
26이란 값을 나눈 이유는 알파벳이 26글자라서 나눈 나머지 값이 구할 값이다 
tmp = (ord(s[i]) - 97 + n) 을뺸 이유는 97이 a의 아스키 코드 값이기 때문이다
'''