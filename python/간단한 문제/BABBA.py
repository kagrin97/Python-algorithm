import sys
input = sys.stdin.readline
k = int(input())
num = [0, 1]

for _ in range(k-1):
    num[0], num[1] = num[1], num[0] + num[1]
    
print(num[0], num[1])

'''
첨에 이문제를 풀떄 2중 for문으로 풀었더니 시간초과가 나와서
문제의 답의 규칙성을 찾아보니 버튼을 한번 누를때마다
num[0], num[1] = num[1], num[0] + num[1] 이런식으로 바뀐다는것을
알았다
'''
