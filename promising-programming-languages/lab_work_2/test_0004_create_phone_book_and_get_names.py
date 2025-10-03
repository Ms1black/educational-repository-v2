import pytest
from main import create_phone_book_and_get_names
from conftest import print_matrix

@pytest.mark.parametrize("num_contacts, contact_data, expected_names_list, expected_phone_book, expected_stdout_message, description", [
    (2, [("Женя", "123"), ("Кирилл", "456")], ["Женя", "Кирилл"], {"Женя": "123", "Кирилл": "456"}, "", "Два контакта"),
    (0, [], [], {}, "Количество контактов должно быть положительным числом.", "Ноль контактов"), 
    (1, [("Антон", "789")], ["Антон"], {"Антон": "789"}, "", "Один контакт"),
    (3, [("Анна", "111"), ("Борис", "222"), ("Анна", "333")], ["Анна", "Борис"], {"Анна": "333", "Борис": "222"}, "", "Дублирующиеся имена (последнее заменяет)"),
    (1, [("Алиса", "555"), ("Боб", "666")], ["Алиса"], {"Алиса": "555"}, "", "num_contacts меньше contact_data"),
])
def test_create_phone_book_and_get_names(num_contacts, contact_data, expected_names_list, expected_phone_book, expected_stdout_message, description, capsys):
    print(f"\n--- Тест Задание 4: {description} ---")
    
    actual_names_list, actual_phone_book = create_phone_book_and_get_names(num_contacts, contact_data)
    
    print(f"    Вход: num_contacts={num_contacts}, contact_data={contact_data}")
    print(f"    Ожидаемый список имен: {expected_names_list}, Полученный: {actual_names_list}")
    print(f"    Ожидаемая телефонная книга: {expected_phone_book}")
    print(f"    Полученная телефонная книга: {actual_phone_book}")

    assert sorted(actual_names_list) == sorted(expected_names_list), f"❌ FAIL: Список имен не совпадает."
    assert actual_phone_book == expected_phone_book, f"❌ FAIL: Телефонная книга не совпадает."

    captured = capsys.readouterr()
    actual_stdout = captured.out.strip()

    if expected_stdout_message: 
        print(f"    Ожидаемое сообщение в stdout: '{expected_stdout_message}'")
        print(f"    Захваченный stdout: '{actual_stdout}'")
        assert expected_stdout_message in actual_stdout, f"❌ FAIL: Ожидаемое сообщение '{expected_stdout_message}' не найдено в stdout."
    else: 
        if num_contacts > 0 and contact_data:
            assert f"Список всех имен: {sorted(expected_names_list)}" in actual_stdout.replace("'", "").replace("[", "").replace("]", ""), "❌ FAIL: Список имен не выведен в консоль."
        else:
            assert not actual_stdout, f"❌ FAIL: Неожиданный вывод в stdout: '{actual_stdout}'"


    print("    ✅ Пройдено.")