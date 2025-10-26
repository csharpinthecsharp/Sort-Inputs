from checks import c_input
from handlers import h_sort
from debugs import d_time

def cvrt_int(av: list[str]) -> list[int]:
    return [int(x) for x in av]

def handle_input(av: list[str]) -> bool:
    av_len = len(av)
    if not c_input.is_valid(av_len, av):
        return (False)
    
    res = read_user_input()
    scanned = scan_type(res)
    if scan_type is None:
        print("Invalid entry")
        return (False)
    
    cleaned_av = av[1:]
    list_int = cvrt_int(cleaned_av)

    time_in_ms = d_time.Debug()

    sort_list = start_sorting(scanned, list_int)
    print("")
    for i in range(len(sort_list)):
        print(f"{sort_list[i]}")

    time_in_ms.stop()
    return True

def scan_type(arg: str) -> int | None:
    if arg == "1":
        return 1
    return None
    
def start_sorting(scanned: int, list_int: list[int]) -> list[int]:
    if scanned == 1:
        res = h_sort.bubble_sort(list_int)
        return res    
def read_user_input() -> str:
    print("(1): Bubble sort\n")
    return input("Select sort type $> ")
