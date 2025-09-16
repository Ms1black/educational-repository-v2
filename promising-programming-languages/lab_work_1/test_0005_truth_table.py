import pytest
from main import truth_table
from conftest import print_matrix

def parse_truth_table_output(raw_output):
    lines = raw_output.strip().split('\n')
    parsed_data = []

    for line in lines:
        parts = []
        for p in line.split("  "):
            if p.strip() and p.strip().isdigit():
                parts.append(int(p.strip()))
        if parts:
            parsed_data.append(parts)
    return parsed_data

def test_truth_table_output(capsys):
    print("\n--- Тест truth_table ---")
    
    expected_data = [
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 0],
        [1, 0, 0, 1, 0, 1, 0],
        [1, 0, 1, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 0, 0, 0]
    ]
    expected_header = ["A", "B", "C", "A ИЛИ B", "НЕ(A ИЛИ B)", "A Экв. C", "НЕ(A ИЛИ B) & (A Экв. C)"]

    truth_table()
    captured = capsys.readouterr()
    raw_output = captured.out.strip()

    output_lines = raw_output.split('\n')

    actual_header_line_idx = -1
    for i, line in enumerate(output_lines):
        if "A ИЛИ B" in line: 
            actual_header_line_idx = i
            break
    
    assert actual_header_line_idx != -1, "❌ FAIL: Заголовок таблицы не найден в выводе."
    actual_header_parts = [p.strip() for p in output_lines[actual_header_line_idx].split("  ") if p.strip()]
    data_start_idx = actual_header_line_idx + 1
    if data_start_idx < len(output_lines) and all(c == '-' or c == ' ' for c in output_lines[data_start_idx]):
        data_start_idx += 1 
    
    actual_data_raw = "\n".join(output_lines[data_start_idx:])
    actual_data = parse_truth_table_output(actual_data_raw)

    print("\n--- Ожидаемый вывод (Заголовок) ---")
    print_matrix([expected_header], title="")
    print("\n--- Ожидаемый вывод (Данные) ---")
    print_matrix(expected_data, title="")
    
    print("\n--- Захваченный вывод (Заголовок) ---")
    print_matrix([actual_header_parts], title="")
    print("\n--- Захваченный вывод (Данные) ---")
    print_matrix(actual_data, title="")
    
    assert actual_header_parts == expected_header, "❌ FAIL: Заголовок таблицы не совпадает."
    assert actual_data == expected_data, "❌ FAIL: Содержимое таблицы истинности не совпадает."
    
    print("✅ PASS: truth_table генерирует и печатает корректную таблицу.")