import pytest
from main import checker_equivalence_of_numeric_and_text_values

def test_checker_equivalence_of_numeric_and_text_values():
    print("\n--- Тест checker_equivalence_of_numeric_and_text_values ---")
    assert checker_equivalence_of_numeric_and_text_values("1") is True, "Текст '1'"
    assert checker_equivalence_of_numeric_and_text_values("a2") is True, "Текст 'a2'"
    assert checker_equivalence_of_numeric_and_text_values("abc123def") is False, "Текст 'abc123def'"
    assert checker_equivalence_of_numeric_and_text_values("1234") is False, "Текст '1234'"
    assert checker_equivalence_of_numeric_and_text_values("test") is False, "Текст без цифр"
    assert checker_equivalence_of_numeric_and_text_values("") is True, "Пустой текст"
    assert checker_equivalence_of_numeric_and_text_values("000") is False, "Текст '000'"
    assert checker_equivalence_of_numeric_and_text_values("a0") is False, "Текст 'a0'"
    print("✅ PASS: checker_equivalence_of_numeric_and_text_values работает корректно.")