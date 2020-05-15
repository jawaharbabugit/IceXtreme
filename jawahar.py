#!/usr/bin/python

# Head ends here

import math
def next_move(pos,board):
    p=[]
    c=0
    a=0
   
    for l in board:
        count=0
        for i in l:
            if i=='d':
                p.append([c,count])
            count+=1
        c+=1
    short=10
    for i in p:
        score=math.sqrt(((pos[0]-i[0])**2)+((pos[1]-i[1])**2))
        if score<short:
            short=score
            p1=i
    if p1==pos:
        print('CLEAN')
    elif p1[1]!=pos[1]:
        if pos[1]>p1[1]:
            print('LEFT')
            pos[1]-=1
        elif pos[1]<p1[1]:
            print('RIGHT')
            pos[1]+=1 
    elif p1[0]!=pos[0]:
        if pos[0]>p1[0]:
            print('UP')
            pos[0]-=1
        elif pos[0]<p1[0]:
            print('DOWN')
            pos[0]+=1
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos, board)
