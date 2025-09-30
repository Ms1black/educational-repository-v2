import pytest
from main import replace_colons_and_count

@pytest.mark.parametrize("input_string, expected_modified_string, expected_count, description", [
    ("Это строка: с двоеточиями: и ещё одним:", "Это строка% с двоеточиями% и ещё одним%", 3, "Несколько двоеточий"),
    ("Строка без двоеточий.", "Строка без двоеточий.", 0, "Без двоеточий"),
    ("", "", 0, "Пустая строка"),
    (":::::", "%%%%%", 5, "Только двоеточия"),
    (":Один:Два:", "%Один%Два%", 3, "Двоеточия в начале/конце и середине"),
])
def test_replace_colons_and_count(input_string, expected_modified_string, expected_count, description):
    print(f"\n--- Тест Задание 1: {description} ---")
    
    actual_modified_string, actual_count = replace_colons_and_count(input_string)
    
    print(f"    Входная строка: '{input_string}'")
    print(f"    Ожидаемая изменённая строка: '{expected_modified_string}'")
    print(f"    Полученная изменённая строка: '{actual_modified_string}'")
    print(f"    Ожидаемое количество замен: {expected_count}")
    print(f"    Полученное количество замен: {actual_count}")

    assert actual_modified_string == expected_modified_string, f"❌ FAIL: Изменённая строка не совпадает."
    assert actual_count == expected_count, f"❌ FAIL: Количество замен не совпадает."
    print("    ✅ Пройдено.")