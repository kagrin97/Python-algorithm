N, M = map(int, input().split())

pokemon = dict()
for i in range(1, N+1):
    name = input()
    pokemon[i] = name
    pokemon[name] = i # 1:민규, 민규:1 이런 형태로 저장

for i in range(M):
    quiz = input()
    if quiz.isalpha(): # 문제가 알파벳이면
        print(pokemon[quiz]) # 바로 key값으로 찾기
    else:
        print(pokemon[int(quiz)]) # 문제가 숫자면 숫자로 바꿔주고 찾기
    

'''
이문제는 처음에 포켓몬을 리스트에 넣고 for문으로 하나씩 맞는 이름을 찾을떄
번호를 출력하도록 했는데 그렇게하니까 시간 초과가 나와서 
딕셔너리 형태로 1:민규, 민규:1 이런 형태로 저장하고 출력하니 
시간초과가 해결되었다
'''