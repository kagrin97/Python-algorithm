s = input()

card = [0] * 10
for i in str(s):
    if i == '6' or i == '9': # 둘중 하나면
        if card[6] == card[9]: # 먼저 6먼저 사용
            card[6] += 1
        else:
            card[9] += 1 # 후에 9사용
    else:
        card[int(i)] += 1 # 같은 수를 여러번 사용한만큼 세트를 깐다

print(max(card))  