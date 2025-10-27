from debugs import d_terminal, d_time
from handlers import h_visualisation

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
        h_visualisation.visual_sort(av, param)
    return av

def selection_sort(av: list[int], param) -> list[int]:
    d_terminal.t_clear()
    for sorted in range(len(av)):
        min_index = sorted
        for j in range(sorted + 1, len(av)):
            if av[j] < av[min_index]:
                min_index = j
        av[sorted], av[min_index] = av[min_index], av[sorted]
        d_time.moove_count += 1
        h_visualisation.visual_sort(av, param)
    return av
