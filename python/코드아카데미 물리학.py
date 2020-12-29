train_mass = 22680 #질량 
train_acceleration = 10 #가속
train_distance = 100 #거리

bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
#화씨온도를 섭씨온도로 변환 하는 방정식
  return c_temp
  
f100_in_celsius = f_to_c(100) 

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
#섭씨온도를 화씨로 바꾸는 방정식
  return f_temp

c0_in_fahrenheit = c_to_f(0)

def get_force(mass, acceleration):
  return mass * acceleration
# 힘은 질량 x 가속
train_force = get_force(train_mass, train_acceleration)

print(train_force)

print("The GE train supplies " + str(train_force) +  " Newtons of force.")

def get_energy(mass, c = 3*10**8):
  return mass * c ** 2
# 질량 x 빛의속도 = 에너지
bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy)  + " Joules.")
  
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance
# 일 = 힘 x 거리, 일의 단위는 j
train_work = get_work(train_mass,train_acceleration,train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
  