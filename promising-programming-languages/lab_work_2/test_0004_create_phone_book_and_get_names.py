import pytest
from main import create_phone_book_and_get_names
from conftest import print_matrix 

@pytest.mark.parametrize("num_contacts, contact_data, expected_names_list, expected_phone_book, description", [
    (2, [("Женя", "123"), ("Кирилл", "456")], ["Женя", "Кирилл"], {"Женя": "123", "Кирилл": "456"}, "Два контакта"),
    (0, [], [], {}, "Ноль контактов"),
    (1, [("Антон", "789")], ["Антон"], {"Антон": "789"}, "Один контакт"),
    (3, [("Анна", "111"), ("Борис", "222"), ("Анна", "333")], ["Анна", "Борис"], {"Анна": "333", "Борис": "222"}, "Дублирующиеся имена (последнее заменяет)"),
    (1, [("Алиса", "555"), ("Боб", "666")], ["Алиса"], {"Алиса": "555"}, "num_contacts меньше contact_data"),
])
def create_phone_book_and_get_names(num_contacts, contact_data, expected_names_list, expected_phone_book, description, capsys):
    print(f"\n--- Тест Задание 4: {description} ---")
    
    actual_names_list, actual_phone_book = create_phone_book_and_get_names(num_contacts, contact_data)
    
    print(f"    Вход: num_contacts={num_contacts}, contact_data={contact_data}")
    print(f"    Ожидаемый список имен: {expected_names_list}, Полученный: {actual_names_list}")
    print(f"    Ожидаемая телефонная книга: {expected_phone_book}")
    print(f"    Полученная телефонная книга: {actual_phone_book}")

    assert sorted(actual_names_list) == sorted(expected_names_list), f"❌ FAIL: Список имен не совпадает."
    assert actual_phone_book == expected_phone_book, f"❌ FAIL: Телефонная книга не совпадает."

    captured = capsys.readouterr()
    if num_contacts > 0 and contact_data:
        assert f"Список всех имен: {sorted(expected_names_list)}" in captured.out.replace("'", ""), "❌ FAIL: Список имен не выведен в консоль."
    elif num_contacts <=0:
         assert "Количество контактов должно быть положительным числом." in captured.out, "❌ FAIL: Ошибка 'Количество контактов должно быть положительным числом.' не выведена."

    print("    ✅ Пройдено.")