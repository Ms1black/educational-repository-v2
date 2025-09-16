import pytest
from main import checker_equivalence_of_numeric_and_text_values

def test_checker_equivalence_of_numeric_and_text_values():
    print("\n--- Тест checker_equivalence_of_numeric_and_text_values ---")
    
    test_cases = [
        ("1", True, "Текст '1'"),
        ("a2", True, "Текст 'a2'"),
        ("abc123def", False, "Текст 'abc123def'"),
        ("1234", False, "Текст '1234'"),
        ("test", False, "Текст без цифр"),
        ("", True, "Пустой текст"),
        ("000", False, "Текст '000'"),
        ("a0", False, "Текст 'a0'"),
    ]

    for text_input, expected, desc in test_cases:
        actual = checker_equivalence_of_numeric_and_text_values(text_input)
        print(f"\n  Тестовый случай: {desc}")
        print(f"    Вход: '{text_input}'")
        print(f"    Ожидалось: {expected}, Получено: {actual}")
        assert actual == expected, f"❌ FAIL для '{desc}'. Ожидалось {expected}, получено {actual}."
        print("    ✅ Пройдено.")

    print("\n✅ PASS: checker_equivalence_of_numeric_and_text_values работает корректно.")