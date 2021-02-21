import math
def solution(w, h):
    return w*h - (w+h - math.gcd(w,h))

    
w = 8
h = 12	
print(solution(w,h))

''' 
w와 h의 최대 공약수는 4이다
w+h - 최대공약수, 를하면 지나가는 사각형의 수를 알수있다
'''



