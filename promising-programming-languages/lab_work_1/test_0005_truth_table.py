import pytest
from main import truth_table
from conftest import print_matrix

def test_truth_table_output():
    print("\n--- Тест truth_table ---")
    actual_table = truth_table()

    expected_table = [
        ["A", "B", "C", "A v B", "not(A v B)", "A != C", "not(A v B) & (A != C)"],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 0],
        [1, 0, 0, 1, 0, 1, 0],
        [1, 0, 1, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 0, 0, 0]
    ]

    print("Визуализация полученной таблицы истинности:")
    print_matrix(actual_table)
    assert actual_table == expected_table, "Содержимое таблицы истинности не совпадает."
    print("✅ PASS: truth_table генерирует корректную таблицу.")