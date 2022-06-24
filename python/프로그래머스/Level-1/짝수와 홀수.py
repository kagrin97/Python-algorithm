def solution(num):
    answer = ''

    if num % 2 == 1:
        answer += "Odd"
        # num % 2 == 0를 쓰면 속도가 많이 느려지는것 같다 
    else:
        answer += "Even"
    return answer 

        
        
n = 6
print(solution(n))

'''
정수 num이 짝수일 경우 Even을 반환하고 
홀수인 경우 Odd를 반환하는 함수, solution을 완성해주세요.
'''
