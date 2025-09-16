import pytest
from main import formatting_array_to_matrix
from conftest import print_matrix

def test_formatting_array_to_matrix():
    print("\n--- Тест formatting_array_to_matrix ---")

    input_s1 = [i for i in range(1, 27)]
    expected_matrix1 = [
        [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],
        [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]
    ]
    actual_matrix1 = formatting_array_to_matrix(input_s1)
    
    print(f"Вход S: {input_s1}")
    print("Визуализация полученной матрицы:")
    print_matrix(actual_matrix1)

    assert actual_matrix1 == expected_matrix1, "Матрица для S(26) не совпадает."
    print("✅ PASS: Тест 1 (S(26))")

    input_s2 = [10, 20, 30, 40, 50]
    expected_matrix2 = [
        [10, 30, 50],
        [20, 40]
    ]
    actual_matrix2 = formatting_array_to_matrix(input_s2)

    print(f"\nВход S: {input_s2}")
    print("Визуализация полученной матрицы:")
    print_matrix(actual_matrix2)

    assert actual_matrix2 == expected_matrix2, "Матрица для меньшего массива не совпадает."
    print("✅ PASS: Тест 2 (меньший массив)")