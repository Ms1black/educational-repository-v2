import pytest
from main import find_min_max_even_in_file
import os

@pytest.fixture
def create_test_file():
    def _create_test_file(filename, content):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return filename
    return _create_test_file

@pytest.mark.parametrize("input_content, expected_min, expected_max, expected_message_part, description", [
    ("10\n-2\n0\n4\nhello\n8\n100\n6", 4, 100, "Минимальное четное положительное: 4", "Файл с четными положительными числами"),
    ("-1\n-3\n5\nabc\n0", None, None, "Четных положительных чисел в файле не найдено.", "Файл без четных положительных чисел"),
    ("2\n2\n2", 2, 2, "Минимальное четное положительное: 2", "Файл с одинаковыми четными положительными числами"),
    ("", None, None, "Четных положительных чисел в файле не найдено.", "Пустой файл"),
    ("1\n3\n5\n7", None, None, "Четных положительных чисел в файле не найдено.", "Только нечетные числа"),
])
def find_min_max_even_in_file(tmp_path, create_test_file, input_content, expected_min, expected_max, expected_message_part, description):
    print(f"\n--- Тест Задание 6: {description} ---")
    
    input_file = create_test_file(tmp_path / "numbers_in.txt", input_content)
    output_file = tmp_path / "numbers_out.txt"

    print(f"  Входной файл '{input_file}' содержит:")
    print("--------------------------------------------------")
    print(input_content.strip() if input_content else "[Пусто]")
    print("--------------------------------------------------")

    actual_min, actual_max, actual_message = find_min_max_even_in_file(str(input_file), str(output_file))
    
    print(f"  Ожидаемый min: {expected_min}, Полученный min: {actual_min}")
    print(f"  Ожидаемый max: {expected_max}, Полученный max: {actual_max}")
    print(f"  Ожидаемая часть сообщения: '{expected_message_part}'")
    print(f"  Полученное сообщение: '{actual_message.strip()}'")

    assert actual_min == expected_min, f"❌ FAIL: Минимальное четное число не совпадает."
    assert actual_max == expected_max, f"❌ FAIL: Максимальное четное число не совпадает."
    assert expected_message_part in actual_message, f"❌ FAIL: Сообщение в выходном файле не содержит ожидаемой части."

    with open(output_file, 'r', encoding='utf-8') as f:
        output_content = f.read()
    assert expected_message_part in output_content, f"❌ FAIL: Содержимое выходного файла не соответствует ожидаемому."
    
    print("    ✅ Пройдено.")

def find_min_max_even_in_file_non_existent_input(tmp_path, capsys):
    print("\n--- Тест Задание 6: Несуществующий входной файл ---")
    
    input_file = tmp_path / "non_existent.txt"
    output_file = tmp_path / "output.txt"
    
    actual_min, actual_max, actual_message = find_min_max_even_in_file(str(input_file), str(output_file))
    
    print(f"  Ожидаемое сообщение об ошибке: 'Входной файл не найден'")
    print(f"  Полученное сообщение: '{actual_message.strip()}'")

    assert actual_min is None and actual_max is None, "❌ FAIL: Ожидались None для min/max."
    assert "Входной файл не найден" in actual_message, "❌ FAIL: Сообщение об ошибке файла не содержит 'Входной файл не найден'."
    
    captured = capsys.readouterr()
    assert "Входной файл не найден" in captured.out, "❌ FAIL: Ошибка 'Входной файл не найден' не была выведена."
    
    print("    ✅ Пройдено.")