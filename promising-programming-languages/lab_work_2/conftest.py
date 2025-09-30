import pytest

def print_matrix(matrix, title=""):
    if title:
        print(f"\n{title}:")
    if not matrix:
        print("[Пусто]")
        return
    
    has_header = False
    if len(matrix) > 0 and isinstance(matrix[0], list) and any(isinstance(x, str) for x in matrix[0]):
        try:
            [int(x) for x in matrix[0][:3]]
        except ValueError:
            has_header = True

    column_widths = [0] * len(matrix[0])
    for r_idx, row in enumerate(matrix):
        for j, item in enumerate(row):
            if len(str(item)) > column_widths[j]:
                column_widths[j] = len(str(item))
    
    if has_header:
        for j, item in enumerate(matrix[0]):
            print(f" {str(item):<{column_widths[j]}} ", end="")
        print()
        for j in range(len(matrix[0])):
            print(f"{'-' * (column_widths[j] + 2)}", end="")
        print()

    start_data_row = 1 if has_header else 0
    for row in matrix[start_data_row:]:
        for j, item in enumerate(row):
            print(f" {str(item):<{column_widths[j]}} ", end="")
        print() 