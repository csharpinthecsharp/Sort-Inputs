def handle_input(av):
    av_len = len(av)
    if av_len <= 1:
            print("No argument found")
    else:
        for arg in av[1:]:
            print("Arguments found:", arg)
            