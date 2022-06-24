import sys
input = sys.stdin.readline

N = int(input())
W = int(input())
num = list(map(int, input().split(" ")))

photo = dict()
for i in range(W) :
    if num[i] in photo :
        photo[num[i]][0] += 1
    else :
        if len(photo) < N :
            photo[num[i]] = [1, i]
        else :
            del_list = sorted(photo.items(), key= lambda x : (x[1][0] , x[1][1]) )
            del_key = del_list[0][0]
            del(photo[del_key])
            photo[num[i]] = [1, i]

ans = list(sorted(photo.keys()))
print(*ans)

# 이 문제는 딕셔너리로 풀었는데 딕셔너리는 sorted 할때 자동으로 들어온 순서대로 정렬하지 않아서
# 들어온 순서를 i 값으로 따로 넣어주었다