import pytest
from main import process_array_from_input

@pytest.mark.parametrize("N, elements, expected_max, expected_reversed_arr, expected_stdout_msg_part, description", [
    (3, [10, 20, 5], 20, [5, 20, 10], "Максимальный элемент: 20", "Положительные числа"),
    (5, [1, 2, 3, 4, 5], 5, [5, 4, 3, 2, 1], "Максимальный элемент: 5", "Возрастающая последовательность"),
    (4, [100, 20, 50, 5], 100, [5, 50, 20, 100], "Максимальный элемент: 100", "Максимум в начале"),
    (1, [42], 42, [42], "Максимальный элемент: 42", "Один элемент"),
    (3, [-1, -5, -2], -1, [-2, -5, -1], "Максимальный элемент: -1", "Отрицательные числа"),
    (0, [], None, None, "Количество элементов должно быть положительным числом.", "Пустой массив N=0"), 
    (-5, [], None, None, "Количество элементов должно быть положительным числом.", "Некорректное N"), 
    
    (3, [1, 2], 2, [2, 1], "Внимание: Получено меньше элементов", "Недостаточно элементов"), 
    
    (2, [], None, [], "Массив пуст, невозможно найти максимальный элемент или обратить.", "Массив пуст (N>0, но elements пуст)")
])
def test_new_task2_process_array_from_input(N, elements, expected_max, expected_reversed_arr, expected_stdout_msg_part, description, capsys):
    print(f"\n--- Тест Задание 2: {description} ---")
    
    actual_max, actual_reversed_arr = process_array_from_input(N, elements)
    
    print(f"    Вход: N={N}, элементы={elements}")
    print(f"    Ожидаемый максимум: {expected_max}, Полученный максимум: {actual_max}")
    print(f"    Ожидаемый массив в обратном порядке: {expected_reversed_arr}, Полученный: {actual_reversed_arr}")

    assert actual_max == expected_max, f"❌ FAIL: Максимальный элемент не совпадает."
    assert actual_reversed_arr == expected_reversed_arr, f"❌ FAIL: Массив в обратном порядке не совпадает."

    captured = capsys.readouterr()
    actual_stdout = captured.out.strip()

    print(f"    Ожидаемая часть сообщения в stdout: '{expected_stdout_msg_part}'")
    print(f"    Захваченный stdout: '{actual_stdout}'")
    assert expected_stdout_msg_part in actual_stdout, f"❌ FAIL: Ожидаемое сообщение '{expected_stdout_msg_part}' не найдено в stdout."
    
    print("    ✅ Пройдено.")