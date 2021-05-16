true = True
false = False
def solution(absolutes, signs):
    for i in range(len(signs)):
      if signs[i] == false:
        absolutes[i] = -absolutes[i]
      
    return sum(absolutes)

absolutes = [4, 7, 12]
signs = [true, false, true]
print(solution(absolutes, signs))

'''
이문제는 signs안에 들어있는 true값을 문자열로 주는게 아닌 변수로 주는
바람에 변수를 따로 정의 후에 실행 해야하는 이상한 문제이다
'''