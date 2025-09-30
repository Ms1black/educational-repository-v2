import pytest
from main import check_sequence_for_duplicates

@pytest.mark.parametrize("sequence_str, expected_results, description", [
    ("1 2 3 2 1 4 5", ["NO", "NO", "NO", "YES", "YES", "NO", "NO"], "Несколько дубликатов"),
    ("10 20 30 40", ["NO", "NO", "NO", "NO"], "Нет дубликатов"),
    ("5 5 5 5 5", ["NO", "YES", "YES", "YES", "YES"], "Только дубликаты"),
    ("1 abc 2 1", ["NO", "Ошибка: 'abc' не является числом", "NO", "YES"], "С нечисловым элементом"),
    ("", [], "Пустая строка"),
    ("  ", [], "Строка только из пробелов"),
])
def check_sequence_for_duplicates(sequence_str, expected_results, description, capsys):
    print(f"\n--- Тест Задание 5: {description} ---")
    
    actual_results = check_sequence_for_duplicates(sequence_str)
    
    print(f"    Входная строка: '{sequence_str}'")
    print(f"    Ожидаемые результаты: {expected_results}")
    print(f"    Полученные результаты: {actual_results}")

    assert actual_results == expected_results, f"❌ FAIL: Список результатов не совпадает."

    captured = capsys.readouterr()
    expected_output_lines = [f"Входная последовательность: {[s for s in sequence_str.split() if s]}", "Результаты проверки:"] + expected_results
    actual_output_lines = [line.strip() for line in captured.out.strip().split('\n') if line.strip()]

    for i, exp_line in enumerate(expected_output_lines):
        if i < len(actual_output_lines):
            assert exp_line in actual_output_lines[i] or actual_output_lines[i] in exp_line, f"❌ FAIL: Строка вывода {i} не совпадает. Ожидалось: '{exp_line}', Получено: '{actual_output_lines[i]}'"
        else:
            pytest.fail(f"❌ FAIL: Вывод короче ожидаемого. Нет строки {i}: '{exp_line}'")
    assert len(actual_output_lines) == len(expected_output_lines), "❌ FAIL: Количество строк вывода не совпадает."

    print("    ✅ Пройдено.")