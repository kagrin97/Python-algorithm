def solution(nums):
    answer = 0
    lengh = len(nums) // 2
    num = list(set(nums))
    '''
    for _ in num:
        if answer < lengh:
            answer += 1             1번 방법
    
    answer = min(lengh, len(num))   2번 방법
    '''
    return answer

s = [3,1,2,3]
print(solution(s))

'''
1번 방법은 다른 사이트 사람들의 풀이를 참고했고
2번 방법은 내가 스스로 생각해낸 방법이다
속도는 1번이 더 빠르다
'''