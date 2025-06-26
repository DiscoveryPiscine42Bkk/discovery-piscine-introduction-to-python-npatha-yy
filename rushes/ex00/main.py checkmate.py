
def checkmate(board):
    size = len(board)

    king_row = -1
    king_colum = -1
    for i in range(size):
        for j in range(size):
            if board[i][j] == "k":
                king_row = i
                king_colum = j
