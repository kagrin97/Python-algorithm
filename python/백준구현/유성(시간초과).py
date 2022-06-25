import sys
input = sys.stdin.readline
R, S = map(int, input().split())
photo = [list(input()) for _ in range(R)]
new_photo = [['.'] * S for i in range(R)]
min_distance = R + 1
star_idx = []
for i in range(R):
    for j in range(S):
        if photo[i][j] == 'X':
            star_idx.append((i, j))
            for k in range(1, R-1):
                if photo[i+k][j] == '#':
                    min_distance = min(min_distance, k)
                    break
        elif photo[i][j] == '#':
            new_photo[i][j] = '#'

for i, j in star_idx:
    new_photo[i+min_distance-1][j] = 'X'

for i in new_photo:
    sys.stdout.write("".join(i))
    sys.stdout.write('\n')