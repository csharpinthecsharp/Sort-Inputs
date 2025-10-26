from debugs import d_terminal, d_time
import time
import os

def is_sort(av: list[int]) -> bool:
    for i in range(len(av) - 1):
        if (av[i] > av[i + 1]):
            return False
    return True

def bubble_sort(av: list[int]) -> list[int]:
    d_terminal.t_clear()
    while not(is_sort(av)):
        for j in range(len(av) - 1):
            if av[j] > av[j + 1]:
                av[j], av[j + 1] = av[j + 1], av[j]
        visual_sort(av)
    return av

def visual_sort(av):
    d_terminal.t_clear()
    x_size, y_size = os.get_terminal_size()
    scale_x = x_size / max(av)
    scale_y =  len(av) / y_size
    last_print_value = -1
    for i in range(len(av)):
        if i - last_print_value >= scale_y:
            print("#" * (int(av[i] * scale_x)))
            last_print_value = i
    time.sleep(0.05)
    d_time.moove_count += 1

         