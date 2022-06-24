'''
1300 k번쨰수
'''

n = int(input())
k = int(input())

def find_k(start, end, n, k):
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in range(1, n + 1):
            count += min(mid // i, n)
        if count >= k:
            result = mid
            end = mid - 1
        else :
            start = mid + 1
    return result

print(find_k(1, n*n, n, k))

'''
10 * 10 행렬에서 15보다 작은수를 구하는 방법은 1행에서 15보다 작은수는
1*1, 1*2 ~ 1*10 총 10개이다. 그렇다면 2행에서는 2*1, 2*2~~2*7 총 7개 즉
15 // 2 == 7과 같다. 하지만 1행에서는 15 // 1 == 15인데 왜 10개이냐면 열이 10
개 이기 때문이다. 그래서 min()을 사용해서 나눈값과 열의 수중에 작은 값을 넣으면 된다.
'''