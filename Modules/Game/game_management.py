import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def game_start():
    clearConsole()
    print('Welcome to Chess Game')
    



