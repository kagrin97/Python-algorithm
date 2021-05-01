N, M = map(int, input().split())

pokemon = dict()
for i in range(1, N+1):
    name = input()
    pokemon[i] = name
    pokemon[name] = i

for i in range(M):
    quiz = input()
    if quiz.isalpha():
        print(pokemon[quiz])
    else:
        print(pokemon[int(quiz)])
    
