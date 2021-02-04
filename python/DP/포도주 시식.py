import sys

n = int(sys.stdin.readline())

array = [0,0,0]
for i in range(n):
    array.append(int(sys.stdin.readline()))

table = [0 for _ in range(len(array))]
for i in range(3, n+3):
    table[i] = max(table[i-1], table[i-2] + array[i], 
    table[i-3] + array[i-1] + array[i])


print(table[n+2])

'''
table[i] = i번쨰 위치에서 마실수 있는 최댓값이라면
3가지 점화식 중 가장 큰값을 선택한다
1. i-1번쨰와 i-2번쨰 둘다 마신경우 = i번째 마실수 없으니 table[i-1]
2. i-1번쨰를 마시지 않은 경우 = table[i-2] + arrary[i]
3. i-3번쨰 마시지 않은 경우 = table[i-3] + arrary[i-1] + arrary[i] 
점화식에 i-3이들어가기 때문에 최소 3부터 순회해야 하기때문에
배열 3개를 생성해주고 결과 값도 n-1에서 +3 해줘야한다
'''

