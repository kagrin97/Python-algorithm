def count(n):
    zero_count = [1, 0, 1]
    one_count = [0, 1, 1]
    
    for i in range(3, n + 1):
        zero_count.append(zero_count[i - 1] + zero_count[i - 2])
        one_count.append(one_count[i - 1] + one_count[i - 2])
    return zero_count, one_count


n = int(input())
zero_count, one_count = count(40)

for i in range(n):
    m = int(input())
    print("%d %d" % (zero_count[m], one_count[m]))

'''
해당 문제는 시간 제한이 0.25초 이기 때문에 미리 값을 구해놔야
통과 할수가 있다(최대 40이니 다행)
'''