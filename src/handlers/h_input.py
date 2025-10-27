from data import d_enum
from handlers import h_sort
from debugs import d_time
from handlers import h_read

import random

def handle_input() -> bool: 
    param = d_enum.s_param()
    scanned_sort_type = h_read.scan_sort_type()
    if not scanned_sort_type:
        return False
    
    scanned_numbers = h_read.scan_numbers_type()
    if not scanned_numbers:
        return False
    
    scanned_speed = h_read.scan_speed_type()
    if not scanned_speed:
        return False

    res_list = create_list(scanned_numbers)
    param.speed = scanned_speed

    timer = d_time.Debug()
    start_sorting(scanned_sort_type, res_list, param)
    timer.stop()
    return True

def create_list(nb: int) -> list[int]:
    list_of_ints: list[int] = []
    for i in range(nb):
        list_of_ints.append(i)
    
    if len(list_of_ints) < 2:
        return (list_of_ints)
    random.shuffle(list_of_ints)
    while h_sort.is_sort(list_of_ints):
        random.shuffle(list_of_ints)
    return (list_of_ints)
    
def start_sorting(scanned: int, list_int: list[int], param) -> list[int]:
    if scanned == 1:
        res = h_sort.bubble_sort(list_int, param)
        return res
    elif scanned == 2:
        res = h_sort.selection_sort(list_int, param)
        return res