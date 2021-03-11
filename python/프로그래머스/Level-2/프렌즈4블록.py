class G:
    pending = set()
    bombed = 0
    board = []

def bomb():
    for i, j in reversed(sorted(G.pending)):
        # 인덱스값이 엉망이 되지 않도록 위에서부터 제거 (밑에서 반대로 넣었으니 또반대면 위에서 시작함)
        G.board[i].pop(j)
        G.bombed += 1
    G.pending = set()

def traverse(i, j):
    if j >= len(G.board[i+1]) - 1:
        return

    if G.board[i][j] == G.board[i][j+1] == G.board[i+1][j] == G.board[i+1][j+1]:
        for x, y in [(i + 1, j + 1), (i + 1, j), (i, j + 1), (i, j)]:
            G.pending.add((x, y))
            # 중복 방지를 위한 set에 제거할 인덱스 값을 넣는다

def solution(m, n, board):
    G.board = [[board[i][j] for i in reversed(range(m))] for j in range(n)]
    # 총 n길이안에 m길이의 리스트를 생성한다 reversed를 사용 꺼꾸로 넣음
    # 처음 이문제를 풀때의 꺼꾸로 넣지않아 삭제되고 난후 인덱스 값이 엉망이됬음
    while True:
        for i in range(len(G.board) - 1):
            for j in range(len(G.board[i]) - 1):
                traverse(i, j)
        if not G.pending:
            break
        # 제거할 값이 없으면 종료
        bomb()

    return G.bombed

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m,n,board))