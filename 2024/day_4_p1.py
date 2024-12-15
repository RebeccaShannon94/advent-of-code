import numpy as np


def xmas_counter(input_lst: list):
    """Count number of occurrences of words XMAS and SAMX in items in list"""
    count = 0
    for item in input_lst:
        count += item.count("XMAS") + item.count("SAMX")
    return count


def lst_str_to_array(input_lst: list):
    """Convert list of strings to an array of letters in the same shape as length of string"""
    matrix_array = []
    for item in input_lst:
        matrix_row = []
        for letter in item:
            matrix_row.append(letter)
        matrix_array.append(matrix_row)
    return np.array(matrix_array)


def get_diagonal_string(input_string: str, output_list=None):
    """Get list of diagonal strings if input strings are treated as rows in a table"""
    output_list = [] if output_list is None else output_list
    item = ""
    min = 0
    max = len(input_string) - 1
    for row in input_string:
        item += row[min]
        if min == max:
            output_list.append(item)
            input_string.pop(0)
            if len(input_string) == 0:
                break
            else:
                get_diagonal_string(input_string, output_list)
        else:
            min += 1

    return output_list


# List of rows
memory_text = open("data/input_day_4.txt", "r").read().splitlines()

# List of columns
memory_transpose = [
    "".join(letter) for letter in (lst_str_to_array(memory_text).T.tolist())
]

# List of diagonals LHS
memory_text_diag_left = get_diagonal_string(memory_text.copy())
memory_transpose_copy = memory_transpose.copy()
memory_transpose_copy.pop(0)
memory_transpose_diag_left = get_diagonal_string(memory_transpose_copy)

# List of diagonals RHS
memory_text_right_copy = memory_text.copy()
memory_text_right_copy.reverse()
memory_text_diag_right = get_diagonal_string(memory_text_right_copy.copy())
memory_transpose_right_copy = [
    "".join(letter)
    for letter in (lst_str_to_array(memory_text_right_copy.copy()).T.tolist())
]
memory_transpose_right_copy.pop(0)
memory_transpose_diag_right = get_diagonal_string(memory_transpose_right_copy)

xmas_count = 0
for lst in [
    memory_text,
    memory_transpose,
    memory_text_diag_left,
    memory_transpose_diag_left,
    memory_text_diag_right,
    memory_transpose_diag_right,
]:
    xmas_count += xmas_counter(lst)

print(f"The word XMAS appears {xmas_count} times")
