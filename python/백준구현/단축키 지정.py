import sys
input = sys.stdin.readline

N = int(input())
short_cut = []        # 단축키 지정
word = [list(input().split()) for _ in range(N)]

for i in range(len(word)):

    flag = False
    for j in range(len(word[i])):
        if word[i][j][0] not in short_cut:          # 해당 단어 첫 글자가 단축키 지정이 안되있으면
            short_cut.append(word[i][j][0].upper())
            short_cut.append(word[i][j][0].lower())
            word[i][j] = '[' + word[i][j][0] + ']' + word[i][j][1:]
            flag = True
            break

    if not flag:                # 모든 단어의 첫글자를 검사해도 다 단축키 지정이 되어있으면
        flag = False
        for j in range(len(word[i])):
            for k in range(len(word[i][j])):        # 모든 알파벳을 검사함
                if word[i][j][k] not in short_cut:
                    short_cut.append(word[i][j][k].upper())
                    short_cut.append(word[i][j][k].lower())
                    word[i][j] = word[i][j][:k] + '[' + word[i][j][k] + ']' + word[i][j][k+1:]
                    flag = True
                    break
            if flag:        # 2중 for문을 벗어나기위함
                break
for i in word:
    print(*i)
