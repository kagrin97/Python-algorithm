'''
n과 m 1번
'''


from itertools import permutations
# 순열을 구해주는 함수
n, m = map(int, input().split())
# 최대 값 n 과 순열의 길이인 m
p = permutations(range(1, n+1), m)
# 함수를 이용해 1~n 까지의 값을 최대 m길이 까지 p에저장
for i in p:
    print(' '.join(map(str, i)))

'''
# p에 저장된 순열을 하나씩 출력 permutations은 튜플 형식이기때문에
str로 바꿔서 출력
'''
