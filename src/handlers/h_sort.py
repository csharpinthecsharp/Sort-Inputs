from debugs import d_terminal, d_time
from data import d_enum
import time
import os

def is_sort(av: list[int]) -> bool:
    for i in range(len(av) - 1):
        if (av[i] > av[i + 1]):
            return False
    return True

def bubble_sort(av: list[int], param) -> list[int]:
    d_terminal.t_clear()
    while not(is_sort(av)):
        for j in range(len(av) - 1):
            if av[j] > av[j + 1]:
                av[j], av[j + 1] = av[j + 1], av[j]
            d_time.moove_count += 1
        visual_sort(av, param)
    return av

def visual_sort(av, param):
    d_terminal.t_clear()
    x_size, y_size = os.get_terminal_size()

    scale_x = 1
    scale_y = 1
    if max(av) >= x_size:
        scale_x = x_size / max(av)
    scale_y = len(av) / y_size

    last_print_value = -1
    for i in range(len(av)):
        if i - last_print_value >= scale_y:
            print("#" * (int(av[i] * scale_x)))
            last_print_value = i
    if param.speed > 1:
        if param.speed == 2:
            time.sleep(0.005)
        elif param.speed == 3:
            time.sleep(0.030)