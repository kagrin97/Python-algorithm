
def middle_element(lst):
  if len(lst) % 2 == 0:
    # lst에 짝수개 요소가 있으면
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    # sum에 2,3번쨰 요소를 저장
    return sum / 2
    # 중간값의 평균 리턴
  
  else:
    return lst[int(len(lst)/2)]
  # 홀수일 경우 중간요소 리턴

print(middle_element([5, 2, -10, -4, 4, 5]))


# 문제지문 :lst라는 하나의 매개 변수가있는 middle_element라는 함수를  작성하십시오.

# lst에 홀수 개의 요소가 있으면 함수는 중간 요소를 반환해야합니다.
# 짝수 요소가있는 경우 함수는 중간 두 요소의 평균을 반환해야합니다.