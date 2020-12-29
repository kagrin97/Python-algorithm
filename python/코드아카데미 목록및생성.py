first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
# first_names에 4명의 이름을 집어넣음

age = []
# 빈 age 생성

age.append(42)
# age에 42라는 숫자를 집어 넣음

all_ages = [32, 41, 29] + age
# all_ages에 나이와 위에 나이를 집어넣음(42)

name_and_age = zip(first_names, all_ages)
# name_and_age에 zip을 이용해 합쳐 집어넣기

ids = range(4)
# ids 에 범위가 0~3 까지 를 집어넣음

ida = range(1, 8, 3)
# 범위 1부터 20까지 3씩 저장 (1,4,7)

print(list(ids))
# list를 이용해 0,1,2,3을 프린트해줌
# list를 사용하지 않을경우 [0, 4] 이렇게만 나옴


print(list(name_and_age))