import pytest
from main import matrix_formation
from conftest import print_matrix

def test_matrix_formation():
    print("\n--- Тест matrix_formation ---")

    M1 = 3
    expected_matrix1 = [
        [1, 0, 0],
        [2, 1, 0],
        [3, 2, 1]
    ]
    actual_matrix1 = matrix_formation(M1)
    
    print(f"Вход M: {M1}")
    print("Визуализация полученной матрицы:")
    print_matrix(actual_matrix1)
    assert actual_matrix1 == expected_matrix1, "Матрица для M=3 не совпадает."
    print("✅ PASS: Тест 1 (M=3)")

    M2 = 5
    expected_matrix2 = [
        [1, 0, 0, 0, 0],
        [2, 1, 0, 0, 0],
        [3, 2, 1, 0, 0],
        [4, 3, 2, 1, 0],
        [5, 4, 3, 2, 1]
    ]
    actual_matrix2 = matrix_formation(M2)

    print(f"\nВход M: {M2}")
    print("Визуализация полученной матрицы:")
    print_matrix(actual_matrix2)
    assert actual_matrix2 == expected_matrix2, "Матрица для M=5 не совпадает."
    print("✅ PASS: Тест 2 (M=5)")

    M3 = 1
    expected_matrix3 = [
        [1]
    ]
    actual_matrix3 = matrix_formation(M3)

    print(f"\nВход M: {M3}")
    print("Визуализация полученной матрицы:")
    print_matrix(actual_matrix3)
    assert actual_matrix3 == expected_matrix3, "Матрица для M=1 не совпадает."
    print("✅ PASS: Тест 3 (M=1)")