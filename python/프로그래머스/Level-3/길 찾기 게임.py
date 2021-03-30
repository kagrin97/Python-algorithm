import sys
sys.setrecursionlimit(10**6) #이걸 안해주면 횟수제한에 걸려서 재귀가 막혀버림

preorder = list() # 전위 순회
postorder = list() # 후위 순회

def order(nodeList, level, curLevel):
    n = nodeList
    cur = n.pop(0) # 리스트의 맨 앞 노드를 불러온다. 
    preorder.append(cur[0]) # 그걸 preorder에 붙인다.
    if n:
        for i in range(len(n)): # 남아 있는 리스트 중에서
            if n[i][1][1] == level[curLevel+1]: # 다음 레벨에 있는 노드인데,
                if n[i][1][0] < cur[1][0]: # x 값이 현재 노드보다 작으면, 왼쪽
                    order( [x for x in n if x[1][0] < cur[1][0]], level, curLevel + 1 ) 
                    # x값이 작은 노드를 모두 가지고 다시 재귀 함수 선언 
                else: # 보다 크면 오른쪽 
                    order( [x for x in n if x[1][0] > cur[1][0]], level, curLevel + 1 ) 
                    # x값이 더 큰 노드들을 가지고 재귀함수 선언
                    break 
                # 오른쪽이 한번 나오면 중지 하는 이유 : 오른쪽이 나오는 순간 형제 노드 순회가 종료된 것이기 때문
    postorder.append(cur[0]) # 마지막에 postorder에 cur 를 붙여주면 후위 순회가 완성된다.

def solution(nodeinfo):
    
    levels = sorted(list({x[1] for x in nodeinfo}), reverse=True) # 어떤 레벨이 있는지 파악 
    nodes = sorted(list(zip(range(1, len(nodeinfo)+1),nodeinfo) ), key= lambda x: (-x[1][1], x[1][0])) #노드좌표와 인덱스를 서로 연결 해 줌 
    order(nodes, levels, 0)

    return [preorder, postorder]

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))