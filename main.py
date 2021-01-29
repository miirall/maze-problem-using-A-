import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_board(board):
    for x in board:
        for y in x:
            print(y, end=" ")
        print()


# this function simply prints the board

def manhattan_distance(board, i, j, rows, cols):
    for x in range(0, cols):
        for y in range(0, rows):
            if(x%2)==0 and (y%2)==0  :
                board[x][y] = int((abs((2 * i - x)) + abs((2 * j - y))) / 2)
            elif ((x%2)==1 or (y%2)==1) :
                board[x][y]= ' '

# this function calculates the distance between every cell and goal
# using manhattan distance heuristic
def check_rand(rows):
    n = random.randint(0, 100)
    m=random.randint(0,100)
    if n >50 and m>50:
        return 1
    else : return 0
#this function generates two ranodm integers between 0 and 100 and if both of them are
#higher than 50 it returns 1 and if not returns 0
#if this function return 1 we put a wall and if not we dont
def put_walls(board , rows , cols):
    cnt=0
    for x in range(0,rows):
        for y in range(0,cols):
            if ((x % 2) == 1 or (y % 2) == 1):
                if (check_rand(rows)==1):
                    if x%2==0:
                        board[x][y]='|'
                        cnt=cnt+1
                        if(cnt>=int((2/10)*(rows*rows))):
                            return
                    elif y%2==0:
                        board[x][y]='-'
                        cnt = cnt + 1
                        if (cnt >= int((2 / 10) * (rows * rows))):
                            return
    return
#this function puts an amount of walls between the maze cells(parts)
#in cells that their number x or y is odd we can put walls
def successor(board , s1,s2,rows,cols,g1,g2,cnt):
    if s1==g1 and s2==g2:
        return board
    cnt=cnt+1
    min=0
    t1 =0
    t2=0
    if s1 ==0:
        if s2==0:
            if board[s1][s2+1] ==' ':
                if min ==0:
                    min = board[s1][s2+2]
                    t1=s1
                    t2=s2+2
                else:
                   if board[s1][s2+2] < min:
                       min= board[s1][s2+2]
                       t1=s1
                       t2=s2+2
            if board[s1+1][s2] ==' ':
                if min ==0:
                    min = board[s1+2][s2]
                    t1=s1+2
                    t2=s2
                else:
                    if board[s1+2][s2] < min:
                        min = board[s1+2][s2]
                        t1=s1+2
                        t2=s2
        elif s2==cols:
            if board[s1][s2-1] ==' ':
                if min ==0:
                    min = board[s1][s2-2]
                    t1=s1
                    t2=s2-2
                else:
                   if board[s1][s2-2] < min:
                       min= board[s1][s2-2]
                       t1=s1
                       t2=s2-2
            if board[s1+1][s2] ==' ':
                if min ==0:
                    min = board[s1+2][s2]
                    t1=s1+2
                    t2=s2
                else:
                    if board[s1+2][s2] < min:
                        min = board[s1+2][s2]
                        t1=s1+2
                        t2=s2
        else:
            if board[s1][s2 - 1] == ' ':
                if min == 0:
                    min = board[s1][s2 - 2]
                    t1 = s1
                    t2 = s2 - 2
                else:
                    if board[s1][s2 - 2] < min:
                        min = board[s1][s2 - 2]
                        t1 = s1
                        t2 = s2 - 2
            if board[s1 + 1][s2] ==' ':
                if min == 0:
                    min = board[s1 + 2][s2]
                    t1 = s1 + 2
                    t2 = s2
                else:
                    if board[s1 + 2][s2] < min:
                        min = board[s1 + 2][s2]
                        t1 = s1 + 2
                        t2 = s2
            if board[s1][s2+1] ==' ':
                if min ==0:
                    min = board[s1][s2+2]
                    t1=s1
                    t2=s2+2
                else:
                   if board[s1][s2+2] < min:
                       min= board[s1][s2+2]
                       t1=s1
                       t2=s2+2
    if s1 == rows:
        if s2 ==0:
            if board[s1][s2+1] ==' ':
                if min ==0:
                    min = board[s1][s2+2]
                    t1=s1
                    t2=s2+2
                else:
                   if board[s1][s2+2] < min:
                       min= board[s1][s2+2]
                       t1=s1
                       t2=s2+2
            if board[s1-1][s2] ==' ':
                if min ==0:
                    min = board[s1-2][s2]
                    t1=s1-2
                    t2=s2
                else:
                    if board[s1-2][s2]<min:
                        min=board[s1-2][s2]
                        t1=s1-2
                        t2=s2
        elif s2==cols:
            if board[s1-1][s2] ==' ':
                if min ==0:
                    min = board[s1-2][s2]
                    t1=s1-2
                    t2=s2
                else:
                    if board[s1-2][s2]<min:
                        min=board[s1-2][s2]
                        t1=s1-2
                        t2=s2
            if board[s1][s2 - 1] == ' ':
                if min == 0:
                    min = board[s1][s2 - 2]
                    t1 = s1
                    t2 = s2 - 2
                else:
                    if board[s1][s2 - 2] < min:
                        min = board[s1][s2 - 2]
                        t1 = s1
                        t2 = s2 - 2
        else:
            if board[s1 - 1][s2] == ' ':
                if min == 0:
                    min = board[s1 - 2][s2]
                    t1 = s1 - 2
                    t2 = s2
                else:
                    if board[s1 - 2][s2] < min:
                        min = board[s1 - 2][s2]
                        t1 = s1 - 2
                        t2 = s2
            if board[s1][s2 - 1] == ' ':
                if min == 0:
                    min = board[s1][s2 - 2]
                    t1 = s1
                    t2 = s2 - 2
                else:
                    if board[s1][s2 - 2] < min:
                        min = board[s1][s2 - 2]
                        t1 = s1
                        t2 = s2 - 2
            if board[s1][s2+1] ==' ':
                if min ==0:
                    min = board[s1][s2+2]
                    t1=s1
                    t2=s2+2
                else:
                   if board[s1][s2+2] < min:
                       min= board[s1][s2+2]
                       t1=s1
                       t2=s2+2
    elif s2==0 and (s1!=0 and s1!=rows):
        if board[s1 - 1][s2] != '-':
            if min == 0:
                min = board[s1 - 2][s2]
                t1 = s1 - 2
                t2 = s2
            else:
                if board[s1 - 2][s2] < min:
                    min = board[s1 - 2][s2]
                    t1 = s1 - 2
                    t2 = s2
        if board[s1][s2 + 1] == ' ':
            if min == 0:
                min = board[s1][s2 + 2]
                t1 = s1
                t2 = s2 + 2
            else:
                if board[s1][s2 + 2] < min:
                    min = board[s1][s2 + 2]
                    t1 = s1
                    t2 = s2 + 2
        if board[s1 + 1][s2] == ' ':
            if min == 0:
                min = board[s1 + 2][s2]
                t1 = s1 + 2
                t2 = s2
            else:
                if board[s1 + 2][s2] < min:
                    min = board[s1 + 2][s2]
                    t1 = s1 + 2
                    t2 = s2
    elif s2==cols and (s1!=0 and s1!= rows):
        if board[s1 - 1][s2] == ' ':
            if min == 0:
                min = board[s1 - 2][s2]
                t1 = s1 - 2
                t2 = s2
            else:
                if board[s1 - 2][s2] < min:
                    min = board[s1 - 2][s2]
                    t1 = s1 - 2
                    t2 = s2
        if board[s1 + 1][s2] == ' ':
            if min == 0:
                min = board[s1 + 2][s2]
                t1 = s1 + 2
                t2 = s2
            else:
                if board[s1 + 2][s2] < min:
                    min = board[s1 + 2][s2]
                    t1 = s1+2
                    t2=s2
        if board[s1][s2 - 1] == ' ':
            if min == 0:
                min = board[s1][s2 - 2]
                t1 = s1
                t2 = s2 - 2
            else:
                if board[s1][s2 - 2] < min:
                    min = board[s1][s2 - 2]
                    t1 = s1
                    t2 = s2 - 2
    elif ((s1!=0 and s1!=cols) and (s2!=0 and s2!=rows)):
        if board[s1 - 1][s2] == ' ':
            if min == 0:
                min = board[s1 - 2][s2]
                t1 = s1 - 2
                t2 = s2
            else:
                if board[s1 - 2][s2] < min:
                    min = board[s1 - 2][s2]
                    t1 = s1 - 2
                    t2 = s2
        if board[s1 + 1][s2] == ' ':
            if min == 0:
                min = board[s1 + 2][s2]
                t1 = s1 + 2
                t2 = s2
            else:
                if board[s1 + 2][s2] < min:
                    min = board[s1 + 2][s2]
                    t1 = s1+2
                    t2=s2
        if board[s1][s2 - 1] == ' ':
            if min == 0:
                min = board[s1][s2 - 2]
                t1 = s1
                t2 = s2 - 2
            else:
                if board[s1][s2 - 2] < min:
                    min = board[s1][s2 - 2]
                    t1 = s1
                    t2 = s2 - 2
        if board[s1][s2 + 1] == ' ':
            if min == 0:
                min = board[s1][s2 + 2]
                t1 = s1
                t2 = s2 + 2
            else:
                if board[s1][s2 + 2] < min:
                    min = board[s1][s2 + 2]
                    t1 = s1
                    t2 = s2 + 2
  #  if cnt>=50:
    #board[t1][t2]=70
        #cnt=0
    #else:
    board[t1][t2]=50
    if board[s1][s2]!=50:
        board[s1][s2]=50
    if t1 == g1 and t2==g2:
        return
    else:
        successor(board,t1,t2,rows,cols,g1,g2,cnt)
        return board
#this function checks every cell.if we can go from that cell to the next cell(top,botton,left,right)
#and if so... we check the neighbour cells to find which one has the lowest distance and we choose it
#and this function goes on until we reach the goal
#for example for (0,0) we only check right and bottom.for middle cells we check every direction
#and like this we go on and find the path from s to g
#for every next cell we find we put number 50 for previous cell so the path can be marked
def way_specify(board,n):
    for i in range(0,n):
        for j in range(0,n):
            if board[i][j]==50:
                board[i][j]='*'
#when the path is marked with 50s . we find the 50s and change it with *
#so it has a nicer look

rows, cols = (19, 19)
board = [[0 for i in range(cols)] for j in range(rows)]
print("please enter the desired position of start and goal point")
s1 = int(input())
s2=int(input())
g1 = int(input())
g2 = int(input())
manhattan_distance(board, g1, g2, rows, cols)
#board[2*s1][2*s2]='s'
#board[2*g1][2*g2] = 'G'
put_walls(board,rows,cols)
print_board(board)
successor(board,(2*s1),(2*s2),rows-1,cols-1,(2*g1),(2*g2),0)
print("this is the board after we found the path")
way_specify(board,rows)
print_board(board)
