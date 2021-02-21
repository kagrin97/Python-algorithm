def solution(s):
    new_list = s.split(" ")
    # 공백을 기준으로 문자 마다 리스트에 넣어줌
    a = []
    
    for i in new_list:
        answer = ''
        for j in range(0, len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        a.append(answer)
        # 문자 하나하나 검사해서 대문자, 소문자 넣어줌
        
    return " ".join(a)
    # 문자마다 공백을 넣어주면서 합쳐줌

n = "try hello world"
print(solution(n))

'''
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 
각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, 
solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

위 문제는 공백도 숫자로 치는 게 아닌 문자 하나 마다 몇번쨰 숫자인지 리셋을 해줘야 한다
'''
