from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)] 

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque()
q.append(1) # 루트노드부터 시작
ans = {}
check = [False for _ in range(n+1)] # 방문처리
while q:
    parent = q.popleft() 
    for i in tree[parent]: # 해당노드와 연결된 노드들
        if not check[i]: # 방문한적이 없다면
            ans[i] = parent # 딕셔너리 형태로 저장
            q.append(i) 
            check[i] = True

for i in range(2, n+1): # 문제에서 2번노드부터 끝까지 출력이 조건임
    print(ans[i])