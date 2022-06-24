'''
수 정렬하기3
'''


import sys

n = int(sys.stdin.readline())

check_ls = [0] * 10001
# append를 쓰면 시간초과가 되기 때문에 미리 초기화 시켜준다
for _ in range(n):
    num = int(sys.stdin.readline())
    check_ls[num] += 1
# 숫자를 입력받고 해당하는 숫자의 인덱스 값을 1씩 올려준다

for i in range(10001):
    if check_ls[i] != 0:
        for _ in range(check_ls[i]):
            print(i)
'''
숫자 0부터 10000까지 비교해서 해당 인덱스값이 1이상이면 즉 숫자가
존재하면 해당 인덱스 값의 개수를 반복해서 출력해준다
'''
