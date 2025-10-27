import os
from data import d_enum

def t_clear():
    if os.name is 'posix':
        os.system('clear')
    else:
        os.system('cls')
    print(str(d_enum.bcolors.ENDC), end="")