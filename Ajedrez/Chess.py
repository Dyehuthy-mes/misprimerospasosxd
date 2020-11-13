from Pawn import Pawn

board = [[0 for x in range(9)] for y in range(9)]

pawn=Pawn()
pawn.pos["x"]=7
pawn.pos["y"]=4

board[7][4]=pawn

print(board)

