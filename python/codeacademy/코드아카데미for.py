single_digits = range(10)
# 변수에 0~9까지 숫자 할당

squares = []
# 빈 변수 만듦


for item in single_digits:
 #변수를 반복하여 item이라는 변수에 적용
  print(item)
  squares.append(item**2)
  # 스퀘어 변수에 아이템 제곱 값을 추가

cubes = [item**3 for item in single_digits]
# 한줄로 목록 만드는법 single_digits 에 값을 가져와 item에 할당하고 item**3 값을 cubes에 집어넣기
print(cubes)