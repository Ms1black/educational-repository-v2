# conftest.py
import pytest

def print_matrix(matrix):
    """
    Вспомогательная функция для красивого вывода матриц в тестах.
    """
    if not matrix:
        print("[]")
        return
    
    # Расчет ширины столбцов
    # Пропускаем заголовки, если это таблица истинности, чтобы не искажать ширину
    start_row = 0
    if len(matrix) > 0 and isinstance(matrix[0], list) and any(isinstance(x, str) for x in matrix[0]):
        start_row = 1 # Предполагаем, что первая строка - заголовок

    column_widths = [0] * len(matrix[0])
    for r_idx, row in enumerate(matrix):
        for j, item in enumerate(row):
            if len(str(item)) > column_widths[j]:
                column_widths[j] = len(str(item))
    
    # Печатаем заголовок, если он есть
    if start_row == 1:
        for j, item in enumerate(matrix[0]):
            print(f" {str(item):<{column_widths[j]}} ", end="")
        print()
        for j, item in enumerate(matrix[0]):
            print(f"{'-' * (column_widths[j] + 2)}", end="") # +2 для пробелов по бокам
        print()


    for row in matrix[start_row:]:
        for j, item in enumerate(row):
            print(f" {str(item):<{column_widths[j]}} ", end="")
        print()