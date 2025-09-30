import pytest
from main import check_sequence_for_duplicates

@pytest.mark.parametrize("sequence_str, expected_results, description", [
    ("1 2 3 2 1 4 5", ["Нет", "Нет", "Нет", "Да", "Да", "Нет", "Нет"], "Несколько дубликатов"),
    ("10 20 30 40", ["Нет", "Нет", "Нет", "Нет"], "Нет дубликатов"),
    ("5 5 5 5 5", ["Нет", "Да", "Да", "Да", "Да"], "Только дубликаты"),
    ("1 abc 2 1", ["Нет", "Ошибка: 'abc' не является числом", "Нет", "Да"], "С нечисловым элементом"),
    ("", [], "Пустая строка"),
    ("  ", [], "Строка только из пробелов"),
])
def test_check_sequence_for_duplicates(sequence_str, expected_results, description, capsys):
    print(f"\n--- Тест Задание 5: {description} ---")

    numbers_str_for_print = [s for s in sequence_str.split() if s]
    print(f"Входная последовательность: {numbers_str_for_print}")
    print("Результаты проверки:")

    actual_results = check_sequence_for_duplicates(sequence_str)
    
    for res in actual_results:
        print(res)

    print(f"    Входная строка: '{sequence_str}'")
    print(f"    Ожидаемые результаты: {expected_results}")
    print(f"    Полученные результаты: {actual_results}")

    assert actual_results == expected_results, f"❌ FAIL: Список результатов не совпадает."

    captured = capsys.readouterr()

    expected_output_lines = [
        f"Входная последовательность: {numbers_str_for_print}",
        "Результаты проверки:"
    ] + expected_results

    actual_output_lines = [line.strip() for line in captured.out.strip().split('\n') if line.strip()]

    filtered_actual_output_lines = []
    in_test_output_section = False
    for line in actual_output_lines:
        if line.startswith("Входная последовательность:") or line.startswith("Результаты проверки:") or line in ["Нет", "Да"] or line.startswith("Ошибка:"):
            filtered_actual_output_lines.append(line)
            in_test_output_section = True 
        elif in_test_output_section and line.startswith("--- Тест Задание 5:"): 
             in_test_output_section = False


    for i, exp_line in enumerate(expected_output_lines):
        if i < len(filtered_actual_output_lines):
            assert exp_line in filtered_actual_output_lines[i] or filtered_actual_output_lines[i] in exp_line, \
                f"❌ FAIL: Строка вывода {i} не совпадает. Ожидалось: '{exp_line}', Получено: '{filtered_actual_output_lines[i]}'"
        else:
            pytest.fail(f"❌ FAIL: Вывод короче ожидаемого. Нет строки {i}: '{exp_line}'")
    
    assert len(filtered_actual_output_lines) == len(expected_output_lines), \
        f"❌ FAIL: Количество строк вывода не совпадает. Ожидалось: {len(expected_output_lines)}, Получено: {len(filtered_actual_output_lines)}"

    print("    ✅ Пройдено.")