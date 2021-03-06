#감시
#https://www.acmicpc.net/workbook/view/1152
import sys
import copy
sys.stdin = open("input.txt","r")
n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
cctv=[]
direction=[4,2,4,4,1] #회전할 수 있는 경우의 수
ccsize=0
sol=1e9
#입력
for i in range(n):
    for j in range(m):
        if 1<=board[i][j]<=5: #cctv면
            cctv.append((i,j,board[i][j]-1))
            ccsize+=1

def update(dir,idx):
    dir=dir%4 #0 우 1 상 2 좌 3 하
    curh=cctv[idx][0]
    curw=cctv[idx][1]
    if dir==0: #오른쪽
        for w in range(curw+1,m):
            if board[curh][w]==6:
                break
            board[curh][w]=-1
    elif dir==1: #위
        for h in range(curh-1,-1, -1):
            if board[h][curw] == 6:
                break
            board[h][curw]= -1
    elif dir==2: #왼쪽
        for w in range(curw-1,-1,-1):
            if board[curh][w]==6:
                break
            board[curh][w]=-1
    elif dir == 3:  # 아래쪽
        for h in range(curh+1,n):
            if board[h][curw] == 6:
                break
            board[h][curw]= -1



def dfs(idx):
    global sol,board
    if idx==ccsize:
        cnt=0
        for i in range(n):
            for j in range(m):
                if board[i][j]==0: #사각지대
                    cnt+=1
        # for k in range(n):
        #     print(board[i])
        # print()
        sol=min(sol,cnt)
        return
    else:
        type=cctv[idx][2]

        for dir in range(direction[type]):
            #백업
            tmp=copy.deepcopy(board)

            #update
            if type==0: #1번 cctv
                update(dir,idx)
            elif type==1:
                update(dir, idx)
                update(dir+2,idx)
            elif type==2:
                update(dir,idx)
                update(dir + 1, idx)
            elif type==3:
                update(dir, idx)
                update(dir + 1,idx)
                update(dir + 2,idx)
            elif type==4:
                update(dir, idx)
                update(dir + 1, idx)
                update(dir + 2, idx)
                update(dir + 3, idx)

            dfs(idx+1)

            #백트래킹
            board=copy.deepcopy(tmp)
dfs(0)
print(sol)
