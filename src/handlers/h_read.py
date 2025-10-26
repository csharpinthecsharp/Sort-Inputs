from data import d_enum
from handlers import h_print

def read_user_input(sort_tempo, sort, number) -> str:
    if sort == 1:
        match sort_tempo:
            case 1:
                h_print.print_sel_algo()
                return input("Select sort type $> ")
            case _:
                return None
    elif number == 1:
        return input("\nTell us how many numbers to sort $> ")
    return None

def user_sort_type(arg: str) -> int | None:
    if arg == "1":
        return 1
    return None

def scan_sort_type() -> bool | int:
    res = read_user_input(1, 1, 0)
    scanned = user_sort_type(res)
    if scanned is None:
        print(str(d_enum.s_err.inv_entry))
        return (False)
    return (scanned)

def scan_numbers_type() -> bool | int:
    res = read_user_input(2, 0, 1)
    if res is None or not res.isdigit():
        print(str(d_enum.s_err.inv_entry))
        return False
    number = int(res)
    if (number > int(d_enum.s_def.MAX_SIZE)):
        print(str(d_enum.s_err.max_list))
        return False
    return (number)