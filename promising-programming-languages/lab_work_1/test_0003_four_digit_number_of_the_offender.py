import pytest
from main import four_digit_number_of_the_offender

def test_four_digit_number_of_the_offender():
    print("\n--- Тест four_digit_number_of_the_offender ---")
    expected_number = 8778
    actual_number = four_digit_number_of_the_offender()
    
    assert actual_number == expected_number, f"Ожидалось: {expected_number}, Получено: {actual_number}"
    print(f"✅ PASS: four_digit_number_of_the_offender вернул корректный номер {actual_number}.")