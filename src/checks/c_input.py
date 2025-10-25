def is_valid(av_len: int, av: list) -> bool:
    if av_len <= 1:
            print("\nNo argument found")
            return (False)
        
    for char in av:
        if (char.isalpha()):
            print("\nYou must use numbers")
            return (False)
    return (True)