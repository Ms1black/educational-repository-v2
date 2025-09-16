import pytest
from main import four_digit_number_of_the_offender

def test_four_digit_number_of_the_offender():
    print("\n--- Тест four_digit_number_of_the_offender ---")
    expected_number = 8778
    actual_number = four_digit_number_of_the_offender()
    
    print(f"Ожидаемый номер нарушителя: {expected_number}")
    print(f"Полученный номер нарушителя: {actual_number}")

    assert actual_number == expected_number, f"❌ FAIL: Ожидалось: {expected_number}, Получено: {actual_number}."
    print(f"✅ PASS: four_digit_number_of_the_offender вернул корректный номер {actual_number}.")