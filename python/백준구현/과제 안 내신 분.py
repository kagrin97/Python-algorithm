attendance = [i for i in range(1,31)]

for i in range(28):
    attendance.remove(int(input()))

for i in attendance:
    print(i)