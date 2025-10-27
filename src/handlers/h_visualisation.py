from debugs import d_terminal
from data import d_enum
import time
import os

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
            if (av[i] == i):
                print(str(d_enum.bcolors.OKGREEN) + "#" * (int(av[i] * scale_x)))
            else:
                print(str(d_enum.bcolors.FAIL) + "#" * (int(av[i] * scale_x)))
            last_print_value = i
    if param.speed > 1:
        if param.speed == 2:
            time.sleep(0.005)
        elif param.speed == 3:
            time.sleep(0.030)