def dirt(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'd':
                l.append((i,j))
    return l
def mse(board, r,c,l):
    m = []
    for x in l:
        m.append(((r-x[0])**2) + ((c - x[1])**2))
    index = m.index(min(m))
    return l[index]



def next_move(r, c, board):
    l = dirt(board)
    x,y = mse(board, r,c,l)
    if x ==r and c == y:
        print("CLEAN")
    elif x!=r:
        if x>r:
            r += 1
            print("DOWN")
        elif x<r:
            r -= 1
            print("UP")
    elif c !=y:
        if c<y:
            c += 1
            print("RIGHT")

        elif c>y:
            c -= 1
            print("LEFT")
