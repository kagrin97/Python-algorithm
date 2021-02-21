def solution(n):
    a = set([i for i in range(3, n+1, 2)])
    print(a)
    # 3부터 2씩 n까지 증가하는 수열을 만듦
    for i in range(3, n+1, 2):
        # 3, 5, 7, 9 ... 등등의 배수를 반복 제거
        if i in a:
            a -= set([i for i in range(i*2, n+1, i)])
            # i*2부터 n까지 i만큼 증가하는 배수 모두 제거(i은남김)
    
    return len(a) + 1

s = 10	
print(solution(s))

'''
에라토스테네스의 체 
알고리즘을 이용한다 2부터 n까지의 수중 2를 제외하면 모든 2의 배수를 없애고
3을 제외한 모든 3의 배수를 없애고 5를 제외한 모든 5의 배수를 없앤다
+2씩 제거할 값들의 소수를 증가 시켜서 모두 반복하면
소수만 남는다
'''
