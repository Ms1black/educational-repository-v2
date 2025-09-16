import pytest
from main import sum_of_the_k_lowest_digits

def test_sum_of_the_k_lowest_digits():
    print("\n--- Тест sum_of_the_k_lowest_digits ---")
    
    test_cases = [
        (12345, 2, 9, "k меньше длины N"),
        (123, 3, 6, "k равно длине N"),
        (56, 3, 11, "k больше длины N"),
        (123, 0, 0, "k = 0"),
        (0, 1, 0, "N = 0"),
        ("abc", 1, 'я могу принимать только натуральные числа', "N - некорректный тип (строка)"),
        (123, "a", 'я могу принимать только натуральные числа', "k - некорректный тип (строка)"),
        (7, 1, 7, "N - однозначное число, k=1"),
        (7, 5, 7, "N - однозначное число, k>1"),
    ]

    for N, k, expected, desc in test_cases:
        actual = sum_of_the_k_lowest_digits(N, k)
        print(f"\n  Тестовый случай: {desc}")
        print(f"    Вход: N={repr(N)}, k={repr(k)}")
        print(f"    Ожидалось: {expected}, Получено: {actual}")
        assert actual == expected, f"❌ FAIL для '{desc}'. Ожидалось {expected}, получено {actual}."
        print("    ✅ Пройдено.")
    
    print("\n✅ PASS: sum_of_the_k_lowest_digits работает корректно.")