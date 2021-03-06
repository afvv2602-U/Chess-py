#This module take care of all the functionalities that the board involves.

game_board = {
        'A':{'A1':0,'A2':0,'A3':0,'A4':0,'A5':0,'A6':0,'A7':0,'A8':0},
        'B':{'B1':0,'B2':0,'B3':0,'B4':0,'B5':0,'B6':0,'B7':0,'B8':0},
        'C':{'C1':0,'C2':0,'C3':0,'C4':0,'C5':0,'C6':0,'C7':0,'C8':0},
        'D':{'D1':0,'D2':0,'D3':0,'D4':0,'D5':0,'D6':0,'D7':0,'D8':0}, 
        'E':{'E1':0,'E2':0,'E3':0,'E4':0,'E5':0,'E6':0,'E7':0,'E8':0},
        'F':{'F1':0,'F2':0,'F3':0,'F4':0,'F5':0,'F6':0,'F7':0,'F8':0},
        'G':{'G1':0,'G2':0,'G3':0,'G4':0,'G5':0,'G6':0,'G7':0,'G8':0},
        'H':{'H1':0,'H2':0,'H3':0,'H4':0,'H5':0,'H6':0,'H7':0,'H8':0}}

def createBoard():
    #Define the starting position of white pieces
    white_board = {
    'Pawns':{'P1':'A7','P2':'B7','P3':'C7','P4':'D7','P5':'E7','P6':'F7','P7':'G7','P8':'H7'},
    'Rooks':{'R1':'A8','R2':'H8'},
    'Knights':{'Kn1':'B8','Kn2':'G8'},
    'Bishops':{'Bs1':'C8','Bs2':'F8'},
    'Queen':{'Q1':'D8'},
    'King':{'K1':'E8'}}

    #Define the starting position of black pieces
    black_board = {
    'Pawns':{'P1':'A2','P2':'B2','P3':'C2','P4':'D2','P5':'E2','P6':'F2','P7':'G2','P8':'H2'},
    'Rooks':{'R1':'A1','R2':'H1'},
    'Knights':{'Kn1':'B1','Kn2':'G1'},
    'Bishops':{'Bs1':'C1','Bs2':'F1'},
    'Queen':{'Q1':'D1'},
    'King':{'K1':'E1'}}
    #Update the empty board with the starter values.
    #True  = White, False = Black
    update_board(board = white_board, sw = True)
    update_board(board = black_board , sw = False)

def update_board(board : dict, sw : bool):
    for key_dict, nested_dict in board.items():
        for nested_key,nested_value in nested_dict.items():
            check_piece(key_dict,nested_value,sw)

#Pieces:
#White : Pawns(1) , Rooks (2) ,  Knights (3) , Bishops (4) , Queen (5) , King (6)
#Black : Pawns(7) , Rooks (8) ,  Knights (9) , Bishops (10) , Queen (11) , King (12)
def check_piece(key : str , value : str, sw : bool):
    for k,v in game_board.items():
            if k == value[0]:
                match(key):
                    case 'Pawns':
                        if sw:
                            game_board[k][value] = 1
                        else:
                            game_board[k][value] = 7
                    case 'Rooks':
                        if sw:
                            game_board[k][value] = 2
                        else:
                            game_board[k][value] = 8
                    case 'Knights':
                        if sw:
                            game_board[k][value] = 3
                        else:
                            game_board[k][value] = 9
                    case 'Bishops':
                        if sw:
                            game_board[k][value] = 4
                        else:
                            game_board[k][value] = 10
                    case 'Queen':
                        if sw:
                            game_board[k][value] = 5
                        else:
                            game_board[k][value] = 11
                    case 'King':
                        if sw:
                            game_board[k][value] = 6
                        else:
                            game_board[k][value] = 12
                    
def show_board():
    for k,v in game_board.items():
        print('%10s %10s'%(k,v))