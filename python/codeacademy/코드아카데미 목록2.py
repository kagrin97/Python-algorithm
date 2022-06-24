inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = len(inventory)
# 인벤토리 숫자
first = inventory[1]
# 인벤토리 첫번째 요소 저장
last = inventory[-1]
# 맨뒤 요소 저장
inventory_2_6 = inventory[2:6]
# 2 ~ 6 요소 저장
first_3 = inventory[0:3]
# 1번쨰 부터 3번쨰 요소 저장
twin_beds = inventory.count('twin bed')
# 트윈베드 카운트 저장
inventory.sort()
# 인벤토리를 정렬
print(inventory)