s = list(str(input()))
visited = [0] * len(s)
total_duck = 0

if len(s) % 5 != 0:     # 5의 배수가 아닐경우 잘못된 입력이다
    print(-1)
    exit()

while 1:
    stack = []
    duck = 0
    for i in range(len(s)):
        try:                    # try를 쓴이유는 while문을 여러번 돌다가 u를 처음만나면 stack에 값이없어서 에러가나서 썻다
            if s[i] == 'q' and not stack and visited[i] == 0:
                stack.append('q')
                visited[i] = 1
            elif s[i] == 'u' and stack[-1] == 'q' and visited[i] == 0:
                stack.pop()
                stack.append('u')
                visited[i] = 1
            elif s[i] == 'a' and stack[-1] == 'u' and visited[i] == 0:
                stack.pop()
                stack.append('a')
                visited[i] = 1
            elif s[i] == 'c' and stack[-1] == 'a' and visited[i] == 0:
                stack.pop()
                stack.append('c')
                visited[i] = 1
            elif s[i] == 'k' and stack[-1] == 'c' and visited[i] == 0:
                stack.pop()
                visited[i] = 1
                duck = 1
        except:
            continue

    total_duck += duck
    if not duck:            # 한바퀴 돌아도 추가 오리가 없다면 잘못된 입력이다
        print(-1)
        exit()
    elif 0 not in visited:    # 모두 방문했으면 값을 출력후 종료
        print(total_duck)
        exit()

