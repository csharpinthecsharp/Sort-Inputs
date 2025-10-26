import os
import debugs.d_time

def is_sort(av: list[int]) -> bool:
    for i in range(len(av) - 1):
        if (av[i] > av[i + 1]):
            return False
    return True

def bubble_sort(av: list[int]) -> list[int]:
    t_clear()
    while not(is_sort(av)):
        for j in range(len(av) - 1):
            if av[j] > av[j + 1]:
                av[j], av[j + 1] = av[j + 1], av[j]
                visual_sort(av, j)
    return av

def t_clear():
    if os.name is 'posix':
        os.system('clear')
    else:
        os.system('cls')

def visual_sort(av, j):
    print(f"{av[j + 1]} => {av[j]}")
    debugs.d_time.moove_count += 1

         