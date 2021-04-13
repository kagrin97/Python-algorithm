for i in range(n):
    s.append(list(map(int, input().split())))
    for j in range(len(s[i])):
        if s[i][j] != 0 and s[i][j] != 6:
            q.append([i, j, s[i][j]])
            cctv_cnt += 1