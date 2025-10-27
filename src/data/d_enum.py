from enum import Enum

class s_err:
     max_list = "\nThe list cannot be greater than 99999"
     inv_entry = "\nInvalid entry"

class s_def:
     MIN_SIZE = 1
     MAX_SIZE = 99999

class s_param:
     def __init__(self):
          self.speed = 0

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
