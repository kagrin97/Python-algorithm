def check(road):
    global count 
    for i in range(n):
        cur_h = road[i][0]
        flat = 1
        for j in range(1,n):
            if road[i][j] == cur_h:
                flat += 1
                cur_h = road[i][j]
            elif road[i][j] == cur_h+1 and flat >= 0:
                if flat >= l:
                    flat = 1
                    cur_h = road[i][j]
                else:
                    break
            elif road[i][j] == cur_h-1 and flat >= 0:
                flat = - l + 1
                cur_h = road[i][j]
            else:
                break
        else:
            if flat >= 0:
                count += 1

n, l = map(int, input().split())
road_row = [list(map(int, input().split())) for _ in range(n)]
road_col = []
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(road_row[j][i])
    road_col.append(tmp)
count = 0

check(road_row)
check(road_col)
print(count)
