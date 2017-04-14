#/usr/bin/env python

#def identify_piece_moving(origin):
#example: brdmove/smove origin -> a8 -> board[0][0] -> 'r' -> rook
#example: brdmove/smove origin -> h1 -> board[7][7] -> 'R' -> rook
#      0 1 2 3 4 5 6 7
#    +-----------------+
#  8 | r n b q k b n r | 0
#  7 | p p . . p p p p | 1
#  6 | . . . . . . . . | 2
#  5 | . . p p . . . . | 3
#  4 | P . . . . . . . | 4
#  3 | . . N . . . . . | 5
#  2 | . P P P P P P P | 6
#  1 | R . B Q K B N R | 7
#    +-----------------+
#      A B C D E F G H

#       0  1  2  3  4  5  6  7
#    +-------------------------+
#  8 | 00 01 02 03 04 05 06 07 | 0
#  7 | 10 11 12 13 14 15 16 17 | 1
#  6 | 20 21 . . . . . . | 2
#  5 | 30 31 . . . . . . | 3
#  4 | 40 41 . . . . . . | 4
#  3 | 50 51 . . . . . . | 5
#  2 | 60 61 62 63 64 65 66 67 | 6
#  1 | 70 71 72 73 74 75 76 77 | 7
#    +-------------------------+
#       A  B  C  D  E  F  G  H
#    result = None
#    li  = list(origin) #take the origin coordinate of a move and split into two.
#    #Then, pick the piece symbol from the board, translating the row/col AN
#    #into two board coordinates.
#    origin_col_x_coord = ord(li[0])-96-1
#    origin_row_y_coord = ord(li[1])-42
#    result = maxchess._board[origin_row_y_coord][origin_col_x_coord]
#    return result

def read_board(chessboard):
    from os import system
    this = [0,1,2,3,4,5,6,7]
    that = [0,1,2,3,4,5,6,7]
    for i in this:
           for j in that:
               system('say ,' + chessboard._board[i][j])
            
def identify_piece_moving(origin, chessboard):
    result = ""
    li  = list(origin)#take the origin coordinate of a move and split into two.
    col = li[0]
    row = li[1]
    isinstance(col, basestring)
    isinstance(row, basestring)
    if col == 'a':
        if row=='1':
            result = chessboard._board[7][0]
            print(result)
        elif row=='2':
            result = chessboard._board[6][0]
            print(result)
        elif row=='3':
            result = chessboard._board[5][0]
            print(result)
        elif row=='4':
            result = chessboard._board[4][0]
            print(result)
        elif row=='5':
            result = chessboard._board[3][0]
            print(result)
        elif row=='6':
            result = chessboard._board[2][0]
            print(result)
        elif row=='7':
            result = chessboard._board[1][0]
            print(result)
        elif row=='8':
            result = chessboard._board[0][0]
            print(result)
    elif col == 'b':
        if row=='1':
            result = chessboard._board[7][1]
            print(result)
        elif row=='2':
            result = chessboard._board[6][1]
            print(result)
        elif row=='3':
            result = chessboard._board[5][1]
            print(result)
        elif row=='4':
            result = chessboard._board[4][1]
            print(result)
        elif row=='5':
            result = chessboard._board[3][1]
            print(result)
        elif row=='6':
            result = chessboard._board[2][1]
            print(result)
        elif row=='7':
            result = chessboard._board[1][1]
            print(result)
        elif row=='8':
            result = chessboard._board[0][1]
            print(result)
    elif col == 'c':
        if row=='1':
            result = chessboard._board[7][2]
            print(result)
        elif row=='2':
            result = chessboard._board[6][2]
            print(result)
        elif row=='3':
            result = chessboard._board[5][2]
            print(result)
        elif row=='4':
            result = chessboard._board[4][2]
            print(result)
        elif row=='5':
            result = chessboard._board[3][2]
            print(result)
        elif row=='6':
            result = chessboard._board[2][2]
            print(result)
        elif row=='7':
            result = chessboard._board[1][2]
            print(result)
        elif row=='8':
            result = chessboard._board[0][2]
            print(result)
    elif col == 'd':
        if row=='1':
            result = chessboard._board[7][3]
            print(result)
        elif row=='2':
            result = chessboard._board[6][3]
            print(result)
        elif row=='3':
            result = chessboard._board[5][3]
            print(result)
        elif row=='4':
            result = chessboard._board[4][3]
            print(result)
        elif row=='5':
            result = chessboard._board[3][3]
            print(result)
        elif row=='6':
            result = chessboard._board[2][3]
            print(result)
        elif row=='7':
            result = chessboard._board[1][3]
            print(result)
        elif row=='8':
            result = chessboard._board[0][3]
            print(result)
    elif col == 'e':
        if row=='1':
            result = chessboard._board[7][4]
            print(result)
        elif row=='2':
            result = chessboard._board[6][4]
            print(result)
        elif row=='3':
            result = chessboard._board[5][4]
            print(result)
        elif row=='4':
            result = chessboard._board[4][4]
            print(result)
        elif row=='5':
            result = chessboard._board[3][4]
            print(result)
        elif row=='6':
            result = chessboard._board[2][4]
            print(result)
        elif row=='7':
            result = chessboard._board[1][4]
            print(result)
        elif row=='8':
            result = chessboard._board[0][4]
            print(result)
    elif col == 'f':
        if row=='1':
            result = chessboard._board[7][5]
            print(result)
        elif row=='2':
            result = chessboard._board[6][5]
            print(result)
        elif row=='3':
            result = chessboard._board[5][5]
            print(result)
        elif row=='4':
            result = chessboard._board[4][5]
            print(result)
        elif row=='5':
            result = chessboard._board[3][5]
            print(result)
        elif row=='6':
            result = chessboard._board[2][5]
            print(result)
        elif row=='7':
            result = chessboard._board[1][5]
            print(result)
        elif row=='8':
            result = chessboard._board[0][5]
            print(result)
    elif col == 'g':
        if row=='1':
            result = chessboard._board[7][6]
            print(result)
        elif row=='2':
            result = chessboard._board[6][6]
            print(result)
        elif row=='3':
            result = chessboard._board[5][6]
            print(result)
        elif row=='4':
            result = chessboard._board[4][6]
            print(result)
        elif row=='5':
            result = chessboard._board[3][6]
            print(result)
        elif row=='6':
            result = chessboard._board[2][6]
            print(result)
        elif row=='7':
            result = chessboard._board[1][6]
            print(result)
        elif row=='8':
            result = chessboard._board[0][6]
            print(result)
    elif col == 'h':
        if row=='1':
            result = chessboard._board[7][7]
            print(result)
        elif row=='2':
            result = chessboard._board[6][7]
            print(result)
        elif row=='3':
            result = chessboard._board[5][7]
            print(result)
        elif row=='4':
            result = chessboard._board[4][7]
            print(result)
        elif row=='5':
            result = chessboard._board[3][7]
            print(result)
        elif row=='6':
            result = chessboard._board[2][7]
            print(result)
        elif row=='7':
            result = chessboard._board[1][7]
            print(result)
        elif row=='8':
            result = chessboard._board[0][7]
            print(result)
    else:
        print("Something is wrong")

    return result
