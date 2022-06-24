def solution(left, right):
    answer = 0

    num = [i for i in range(left, right+1)]

    for i in range(len(num)):
      cnt = 0
      for j in range(1, num[i]+1):
        if num[i] % j == 0:
          cnt += 1
      if cnt % 2 != 0:
        num[i] = -num[i]
    return sum(num)

left = 24
right = 27
print(solution(left, right))

'''
해당 숫자의 약수의 개수가 짝수이면 정수로 변환
홀수이면 음수로 변환해 총 합을 구하는 문제
'''