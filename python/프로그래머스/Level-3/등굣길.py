def solution(m, n, puddles):

    graph = [[0 for _ in range(m+1)] for _ in range(n+1)]

    graph[1][1] = 1 # 초기값
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1: # 처음위치이면 무시
                continue
            if [j, i] in puddles: # 2중 for문 이랑 puddles순서가 반대여서
                graph[i][j] = 0 # i,j를 돌려준다
            else: 
                graph[i][j] = graph[i-1][j] + graph[i][j-1]

    return graph[-1][-1] % 1000000007

m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))

'''
이 문제는 처음에 dfs문제인줄 알았는데
그렇게 풀게되면 최단거리는 나오지만 총 몇가지인지를
알수가 없었다
하지만 의외로 엄청 간단했다
웅덩이를 -1로 설정해서 풀려했더니 왼쪽 + 위 값이 오히려 
작아져서 0으로 대체했다
'''
