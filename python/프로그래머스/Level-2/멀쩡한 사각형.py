import math
def solution(w, h):
    return w*h - (w+h - math.gcd(w,h))

    
w = 8
print(solution(w))




