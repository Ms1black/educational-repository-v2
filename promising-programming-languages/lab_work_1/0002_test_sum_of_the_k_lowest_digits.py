import pytest
from main import sum_of_the_k_lowest_digits

def test_sum_of_the_k_lowest_digits():
    print("\n--- Тест sum_of_the_k_lowest_digits ---")
    assert sum_of_the_k_lowest_digits(12345, 2) == 9, "12345, k=2 -> 4+5=9"
    assert sum_of_the_k_lowest_digits(123, 3) == 6, "123, k=3 -> 1+2+3=6"
    assert sum_of_the_k_lowest_digits(56, 3) == 11, "56, k=3 -> 5+6=11"
    assert sum_of_the_k_lowest_digits(123, 0) == 0, "123, k=0 -> 0"
    assert sum_of_the_k_lowest_digits(0, 1) == 0, "0, k=1 -> 0"
    assert sum_of_the_k_lowest_digits("abc", 1) == 'я могу принимать только натуральные числа', "Некорректный N"
    assert sum_of_the_k_lowest_digits(123, "a") == 'я могу принимать только натуральные числа', "Некорректный k"
    assert sum_of_the_k_lowest_digits(7, 1) == 7, "7, k=1 -> 7"
    assert sum_of_the_k_lowest_digits(7, 5) == 7, "7, k=5 -> 7"
    print("✅ PASS: sum_of_the_k_lowest_digits работает корректно.")