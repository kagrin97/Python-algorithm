def solution(n, arr1, arr2):
    answer = []

    for a1, a2 in zip(arr1, arr2):
        tmp = str(bin(a1 | a2)[2:]) # 수를 이진수로 바꿔주고 0b를 빼기위해 슬라이싱을 사용
        tmp = tmp.rjust(n, '0') # 오른쪽 정렬로 수를 오른쪽 정렬하고 n길이가 되게 0을 앞에 삽입
        tmp = tmp.replace('1', '#') # 1을 # 으로 바꿈
        tmp = tmp.replace('0', ' ')
        answer.append(tmp)
            

    return answer

n = 5
a1 = [9, 20, 28, 18, 11]
a2 = [30, 1, 21, 17, 28]
print(solution(n, a1, a2))

'''
위 문제는 비트 연산자 | 를 쓰는것이 관건이며 rjust라는 정렬 함수를
이용해 자릿수를 맞춰주고 문자열값을 replace로 바꿔 준다
'''

