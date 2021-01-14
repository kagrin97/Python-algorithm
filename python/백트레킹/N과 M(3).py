import sys

def n_queen(arr, n):
    global count
    if len(arr) == n:
        count += 1
        return
    candidate = list(range(n)) #n=4인 경우, candidate=[0,1,2,3]
    for i in range(len(arr)): #i는 어쩌면 행 번호
        if arr[i] in candidate:
            candidate.remove(arr[i])
        dist = len(arr) - i
        # arr[i]가 아닌 len(arr)로 하는 이유는, 다음 차례에 들어갈 칸이 현재 들어가있는 행길이 뒤에 들어가야하므로, 대각선의 차가 그만큼 나야한다.
        # 예를 들어서 현재 (0,0)만 arr에 있는 경우에는 다음에 놓일 퀸은 1행에 들어가게 되므로 대각선에 해당하는 값은 (1,1)밖에 없으므로 dist=1
        # 현재 (0,0) (1,2) 가 들어가있는 경우에는 (0,0)에서 확인하는 경우라도 다음에 놓일 퀸은 2행에 들어가게 되므로 대각선에 해당하는 값은 (2,2) 이르모 dist = 2 (len(arr)-i)
        if arr[i] + dist in candidate: #같은 대각선
            candidate.remove(arr[i] + dist)
        if arr[i] - dist in candidate:
            candidate.remove(arr[i] - dist)
    if candidate:
        for c in candidate:
            arr.append(c)
            n_queen(arr,n)
            arr.pop()
    else:
        return

count = 0
n = int(sys.stdin.readline().strip())
for i in range(n):
    n_queen([i], n)
print(count)