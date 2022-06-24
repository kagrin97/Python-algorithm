toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives',
 'anchovies', 'mushrooms']
# 토핑
prices = [2, 6, 1, 3, 2, 7, 2]
# 가격
num_pizzas = len(toppings)
# 토핑 총개수 저장
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
# 토핑의 개수 프린트
pizzas = list(zip(prices, toppings))
# 오류 안나게 list로 zip으로 둘이 합쳐 저장
pizzas.sort()
# 피짜 정렬
cheapest_pizza = pizzas[1]
# 피자 두번째 저장 (2번쨰로 싼것)
priciest_pizza = pizzas[-1]
# 피자 맨뒤 저장 (가장 비싼것)
three_cheapest = pizzas[:3]
# 피자 싼피자 3가지 
num_two_dollar_slices = prices.count(2)
# 가격 변수에 2달러 요소 개수 카운트

print(cheapest_pizza)
