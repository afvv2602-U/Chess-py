#This module is in charge of compatibility between deeper modules and main module
from Modules import board , game

def start():
    board.createBoard()
    game.game_start()