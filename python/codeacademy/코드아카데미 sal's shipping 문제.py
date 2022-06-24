#개빡치는 파이썬 아카데미 문제중     살 배송 시스템 문제
#지상, 드론, 프리미엄 중 거리에따른 가격과 고객이 가진 거리에 따라 효율적인 배송 방향을 알려주는
#코드


def ground_shipping(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10: 
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  
  cost = 20 + (price_per_pound * weight)
  return cost

# 육로를 이용한 배송의 경우 2파운드 무게는 1.50달러  최종 코스트 방식은 20달러 + 무게에따를 가격 + 무게
print(ground_shipping(8.4))

premium_ground_shipping = 125.00
# 프리미엄 일경우 무조건 125달러

def drone_shipping(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10: 
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
 
  cost = price_per_pound * weight
  return cost

# 드론으로 인한 배송의 경우 2파운드 일경우 4.5달러 최종 코스트 : 위의 방식과 같지만 20달러를 추가 x
print(drone_shipping(1.5))

def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  premium = premium_ground_shipping
  drone = drone_shipping(weight)
  if premium < drone and premium < ground:
   return "Premium is the cheapest: $" + str(premium)
  
  elif drone < premium and drone < ground:
   return "Drone is the cheapest: $" + str(drone)
  
  else:
   return "Gorund is the cheapest: $" + str(ground)

#개빡치는 마지막문제 고객이 입력한 무게에따라 자동으로 추천 방식과 가격을 알려주는 코드

 

print(cheapest_shipping(4.8))
print(cheapest_shipping(41.5))
