T = int(input())
Q, D, N, P = 25, 10, 5, 1

for _ in range(T):
    money = int(input())
    change = 0
    q_cnt, d_cnt, n_cnt, p_cnt = 0, 0, 0, 0

    while 1:
        if money == change:
            break
        elif money - change >= Q:
            change += Q
            q_cnt += 1
        elif money - change >= D:
            change += D
            d_cnt += 1
        elif money - change >= N:
            change += N
            n_cnt += 1
        elif money - change >= P:
            change += P
            p_cnt += 1
        
        
    print(q_cnt, d_cnt, n_cnt, p_cnt)

'''
거스름돈 문제이다
미국식 동전들이 나온다 쿼터 다임 
'''



    
