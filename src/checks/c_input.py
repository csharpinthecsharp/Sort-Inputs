from data import d_enum

def is_valid(av_len: int, av: list) -> bool:
    if av_len <= 1:
            print(d_enum.s_err.no_arg.value)
            return (False)
        
    for i in av[1:]:
        try:
            int(i)
        except ValueError:
            print(d_enum.s_err.not_nbr.value)
            return (False)
    return (True)