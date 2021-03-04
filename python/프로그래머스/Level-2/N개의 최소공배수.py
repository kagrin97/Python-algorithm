from math import gcd

def solution(arr):

    def LCM(x, y):
        return x * y // gcd(x, y)

    while True:
        arr.append(LCM(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]

a = [3,4,9,16]
print(solution(a))

'''
최소 공배수를 계속 구해주면서 1나만 남을때까지
뺴준다 LCM은 Least common multiple == 최소 공배수
의 약자이다
'''

