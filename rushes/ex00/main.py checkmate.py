#!/usr/bin/env python3
def checkmate(board):
    size = len(board)

    king_row = -1
    king_colum = -1
    for i in range(size):
        for j in range(size):
            if board[i][j] == "K":
                king_row = i
                king_colum = j
    if king_row == -1:
        print("Fail")
        return

    pawn_attracks = [(-1, -1), (-1, 1)]
    for dr, dc in pawn_attracks:
        r = king_row + dr
        c = king_colum + dc
        if 0 <= r < size and 0 <= c < size:
            if board[r][c] == "P":
                print("Success")
                return

    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonals:
        r = king_row + dr
        c = king_colum + dc
        while 0 <= r < size and 0 <= c < size:
            piece = board[r][c]
            if piece == ".":
                r += dr
                c += dc
                continue
            if piece == "B" or piece == "Q":
                print("Success")
            break

    lines = [(-1, -0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in lines:
        r = king_row + dr
        c = king_colum + dc
        while 0 <= r < size and 0 <= c < size:
            piece = board[r][c]
            if piece == ".":
                r += dr
                c += dc
                continue
            if piece == "R" or piece == "Q":
                print("Success")
                return
            break

    print("Fail")


