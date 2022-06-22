l, r = input().split()
s = input()
keypad = {"q":(0,0),"w":(0,1),"e":(0,2),"r":(0,3),"t":(0,4),"y":(0,5),"u":(0,6),"i":(0,7),"o":(0,8),"p":(0,9),
          "a":(1,0),"s":(1,1),"d":(1,2),"f":(1,3),"g":(1,4),"h":(1,5),"j":(1,6),"k":(1,7),"l":(1,8),
          "z":(2,0),"x":(2,1),"c":(2,2),"v":(2,3),"b":(2,4),"n":(2,5),"m":(2,6)}
l_state = keypad[l]
r_state = keypad[r]
time = 0
for i in s:
    if i in ["q","w","e","r","t","a","s","d","f","g","z","x","c","v"]:
        target_x, target_y = keypad[i][0], keypad[i][1]
        cur_x, cur_y = l_state[0], l_state[1]
        distance = abs(cur_x-target_x) + abs(cur_y-target_y)
        time += distance + 1
        l_state = keypad[i]
    else:
        target_x, target_y = keypad[i][0], keypad[i][1]
        cur_x, cur_y = r_state[0], r_state[1]
        distance = abs(cur_x - target_x) + abs(cur_y - target_y)
        time += distance + 1
        r_state = keypad[i]

print(time)