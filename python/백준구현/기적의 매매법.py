cash = int(input())
stock = [i for i in map(int, input().split())]
j_money, j_stock = cash, 0
s_money, s_stock = cash, 0

for i in stock:
    if i <= j_money:
        j_stock += j_money // i
        j_money = j_money % i
j_total = (j_stock * stock[-1]) + j_money

for i in range(3, len(stock)):
    if stock[i-3] > stock[i-2] > stock[i-1]:
        if stock[i] <= s_money:
            s_stock += s_money // stock[i]
            s_money = s_money % stock[i]

    elif stock[i-3] < stock[i-2] < stock[i-1]:
        if s_stock != 0:
            s_money = s_stock * stock[i]
            s_stock = 0
s_total = (s_stock * stock[-1]) + s_money

if j_total > s_total:
    print("BNP")
elif j_total < s_total:
    print("TIMING")
else:
    print("SAMESAME")