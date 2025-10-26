from enum import IntEnum, StrEnum

class s_err(StrEnum):
     max_list = "\nThe list cannot be greater than 99999"
     inv_entry = "\nInvalid entry"

class s_def(IntEnum):
     MIN_SIZE = 1
     MAX_SIZE = 99999
