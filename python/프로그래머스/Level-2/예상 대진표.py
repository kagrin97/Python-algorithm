def solution(n,a,b):
    answer = 0

    while a != b:
        answer += 1
        a, b = (a+1) // 2, (b+1) // 2
            
    return answer

n = 8
a = 4
b = 7
print(solution(n, a, b))

'''
공식을 보면 풀리는 문제 ;;
'''