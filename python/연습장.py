from collections import deque

def end_game(b):
    if b.count('0') == 16:
        return True
    return False

def remove_element(b, e):
    b = b.replace(e, '0')
    return b

def move(b, y, x, dy, dx):
    ny, nx = y + dy, x + dx
    if 0 <= nx < 4 and 0 <= ny < 4 and b[ny * 4 + nx] == '0':
        return move(b, ny, nx, dy, dx)
    else:
        if 0 <= nx < 4 and 0 <= ny < 4:
            return (ny, nx)
        else:
            return (y, x)

def solution(board, r, c):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    b = ""
    for i in range(4):
        for j in range(4):
            b += str(board[i][j])
    q = deque()

    cnt = 0
    enter = -1
    q.append((r, c, b, cnt, enter))
    s = set()

    while q:
        y, x, b, c, e = q.popleft()
        pos = 4 * y + x

        if (y, x, b, e) in s:
            continue
        s.add((y, x, b, e))
        if end_game(b):
            return c
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                q.append((nx, ny, b, c+1, e))
        
        for i in range(4):
            ny, nx = move(b, y, x, dy[i], dx[i])
            if ny == y and nx == x:
                continue
            q.append((ny, nx, b, c+1, e))
        
        if b[pos] != 0:
            if e == -1:
                n_e = pos
                q.append((y, x, b, c+1, n_e))
            else:
                if e != pos and b[e] == b[pos]:
                    b = remove_element(b, b[e])
                    q.append((y, x, b, c+1, -1))
    return answer


board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
print(solution(board, r, c))