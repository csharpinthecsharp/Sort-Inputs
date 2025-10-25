from checks import c_input

def handle_input(av: list) -> bool:

    av_len = len(av)

    if not c_input.is_valid(av_len, av):
        return (False)
    else:
        for i, arg in enumerate(av[1:], start=1):
            print(f"\nArguments found[{i}]: {arg}")
    return (True)