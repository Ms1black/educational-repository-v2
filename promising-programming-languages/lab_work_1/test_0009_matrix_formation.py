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
    
    print(f"  Вход M: {M1}")
    print_matrix(expected_matrix1, "Ожидаемая матрица")
    print_matrix(actual_matrix1, "Полученная матрица")
    assert actual_matrix1 == expected_matrix1, "❌ FAIL: Матрица для M=3 не совпадает."
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

    print(f"\n  Вход M: {M2}")
    print_matrix(expected_matrix2, "Ожидаемая матрица")
    print_matrix(actual_matrix2, "Полученная матрица")
    assert actual_matrix2 == expected_matrix2, "❌ FAIL: Матрица для M=5 не совпадает."
    print("✅ PASS: Тест 2 (M=5)")

    M3 = 1
    expected_matrix3 = [
        [1]
    ]
    actual_matrix3 = matrix_formation(M3)

    print(f"\n  Вход M: {M3}")
    print_matrix(expected_matrix3, "Ожидаемая матрица")
    print_matrix(actual_matrix3, "Полученная матрица")
    assert actual_matrix3 == expected_matrix3, "❌ FAIL: Матрица для M=1 не совпадает."
    print("✅ PASS: Тест 3 (M=1)")