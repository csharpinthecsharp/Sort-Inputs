import os

def t_clear():
    if os.name is 'posix':
        os.system('clear')
    else:
        os.system('cls')