hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price
  average_price = total_price / len(prices)
# 토탈 값에 값을 다넣어서 255를 생성후 가격 숫자 8을 나눠서 평균 가격 31이 나옴
print("Average Haircut Price " + str(average_price))

new_prices = [price-5 for price in prices]
# 새로운 가격임 전 메뉴 5달러 인하
print(new_prices)

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
# 총수익 가격과 이용 숫자 곱을 총수익 
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)
# 총수익에 7 나눠서 평균 수익 구함
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
# 30달러 미만 헤어만 따로 cuts_under_30에 저장
print(cuts_under_30)