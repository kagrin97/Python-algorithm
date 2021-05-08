def solution(n, k, cmd):
    answer = ''
    cur = k
    check = list(range(n))
    board = list(range(n))
    d_idx = []
    d_val = []
    for i in range(len(cmd)):
        if len(cmd[i]) > 1:
            use, val = cmd[i].split(' ')
            if use == 'D':
                cur += int(val)
            elif use == 'U':
                cur -= int(val)
        else:
            if cmd[i][0] == 'C':
                d_idx.append(cur)
                d_val.append(board[cur])
                del board[cur]
                cur -= 1
            elif cmd[i][0] == 'Z':
                if d_idx[-1] < cur:
                    cur += 1
                board.insert(d_idx.pop(), d_val.pop())

    for i in range(n):
        if check[i] not in board:
            answer += 'X'
        else:
            answer += 'O'
    return answer

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))