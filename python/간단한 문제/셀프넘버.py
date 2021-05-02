self_num = set(range(1, 10001)) # 셀프넘버
num = set() # 생성자 모음

for i in range(1, 10001): # i = 850
    for j in str(i): # j = '8','5','0'
        i += int(j)  # 850 + 8 + 5 + 0 = 863
    num.add(i) # 생성자가 있는 숫자들

self_num = sorted(self_num - num) # 정렬(모든숫자 - 생성자가 있는 숫자) = 셀프넘버
for i in self_num:
    print(i)
    
