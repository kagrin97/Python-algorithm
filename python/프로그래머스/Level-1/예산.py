def solution(d, budget):
    d.sort()
    
    while budget < sum(d):
        d.pop()
    return len(d)


d = [0]
b = 10
print(solution(d, b))