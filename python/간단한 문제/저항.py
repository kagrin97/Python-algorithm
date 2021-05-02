color = dict()
color["black"] = [0, 1]
color["brown"] = [1, 10]
color["red"] = [2, 100]
color["orange"] = [3, 1000]
color["yellow"] = [4, 10000]
color["green"] = [5, 100000]
color["blue"] = [6, 1000000]
color["violet"] = [7, 10000000]
color["grey"] = [8, 100000000]
color["white"] = [9, 1000000000]

result = ''
for i in range(3):
    c = input()
    if i == 2:
        print(int(result) * color[c][1])
    else:
        result += str(color[c][0])

