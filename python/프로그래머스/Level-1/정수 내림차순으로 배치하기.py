def solution(n):
    answer = []
    n = str(n)

    for i in range(len(n)):
        answer.append(str(n[i]))

    answer.sort(reverse=True)
    answer = int(''.join(answer))
    return answer 

            
n = 118372
print(solution(n))

"""
함수 solution은 정수 n을 매개변수로 입력받습니다. 
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
예를들어 n이 118372면 873211을 리턴하면 됩니다.

int -> str -> int 3단계에 걸쳐서 푸는 문제이다
"""
