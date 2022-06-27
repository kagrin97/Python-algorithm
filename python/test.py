import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def go(target, kinds): #탐색할 함수
    global f_num
    if target not in direc: #현재 탐색할 주체가 파일이나 폴더가 없다면 종료한다
        return

    for title, val in direc[target]:
        if val == 0:
            kinds.add(title)
            f_num += 1

        else: #폴더라면 더 탐색해서 들어감
            go(title, kinds)

    return

direc = {} #폴더 디렉토리
f_num = 0
N, M = map(int, input().split())

for i in range(N+M):
    From, To, Id = input().rstrip().split()
    if From not in direc:
        direc[From] = []
        direc[From].append([To, int(Id)])
    else:
        direc[From].append([To, int(Id)])

q = int(input())

for i in range(q):
    query = input().rstrip().split('/')
    SET = set()
    f_num = 0
    go(query[-1], SET)

    print(len(SET), f_num)