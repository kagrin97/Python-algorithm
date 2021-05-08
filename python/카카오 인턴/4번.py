def solution(n, start, end, roads, traps):
    answer = 0
    val = 0
    flag = True
    while flag:
        for i in range(len(roads)):
            if start in traps:
                roads[i][0], roads[i][1] = roads[i][1], roads[i][0]
            if roads[i][0] == start:
                start = roads[i][1]
                val += roads[i][2]
                  
    return val


n = 3
start = 1
end = 3
roads = [[1, 2, 2], [3, 2, 3]]
traps = [2]