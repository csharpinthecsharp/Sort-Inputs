from data import d_enum
from handlers import h_sort
from debugs import d_time
from handlers import h_read
import random

def handle_input() -> bool: 
    scanned_sort_type = h_read.scan_sort_type()
    if not scanned_sort_type:
        return False
    
    scanned_numbers = h_read.scan_numbers_type()
    if not scanned_numbers:
        return False

    res_list = create_list(scanned_numbers)

    timer = d_time.Debug()
    start_sorting(scanned_sort_type, res_list)
    timer.stop()
    return True

def create_list(nb: int) -> list[int]:
    min = int(d_enum.s_def.MIN_SIZE)
    max = int(d_enum.s_def.MAX_SIZE)

    list_of_ints: list[int] = []
    for i in range(nb):
        list_of_ints.append(random.randint(min, max))
    return (list_of_ints)
    
def start_sorting(scanned: int, list_int: list[int]) -> list[int]:
    if scanned == 1:
        res = h_sort.bubble_sort(list_int)
        return res