def solution(x):
    x = str(x)
    number = []
    for i in range(len(x)):
        number.append(int(x[i]))

    number_sum = sum(number)
    if int(x) % number_sum == 0:
        return True
    else:
        return False

n = 10
print(solution(n))

'''
위 문제는 정수를 나누기 위해 str로 변환후 int형으로 list에
하나씩 넣은 다음에 sum을해 총합을 구한후 검사를 하는 방식이다
sum을 사용하기 위해서는 list에 int형만 있어야한다 (str = x)
'''




