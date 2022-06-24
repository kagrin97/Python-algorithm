from itertools import combinations as combi 

N = int(input()) # 총 선수
S = [list(map(int, input().split())) for _ in range(N)] 
members = [i for i in range(N)] # combi를 위한 배열
combi_team = []
min_val = int(1e9) # 최소값 갱신을위한 변수

#조합으로 가능한 팀 생성해주기
for team in list(combi(members, N//2)):
    combi_team.append(team)

for i in range(len(combi_team)//2): # 딱 2팀으로 나누기위한 //2
    team = combi_team[i] # 현재 선수 번호 예:(0,1)
    stat_a = 0
    for j in range(N//2): 
        x = team[j] # x값을 바꿔주기위해 N//2
        for y in team:
            stat_a += S[x][y] # Y값을 바꾸기위함
    
    team = combi_team[-i-1] # -I-1하면 뒤에서부터 실행 함
    stat_b = 0
    for j in range(N//2):
        x = team[j]
        for y in team:
            stat_b += S[x][y]
    
    min_val = min(min_val, abs(stat_a - stat_b))
print(min_val)

