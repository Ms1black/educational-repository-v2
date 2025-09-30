import pytest
from main import process_array_from_input

@pytest.mark.parametrize("N, elements, expected_max, expected_reversed_arr, description", [
    (3, [10, 20, 5], 20, [5, 20, 10], "Положительные числа"),
    (5, [1, 2, 3, 4, 5], 5, [5, 4, 3, 2, 1], "Возрастающая последовательность"),
    (4, [100, 20, 50, 5], 100, [5, 50, 20, 100], "Максимум в начале"),
    (1, [42], 42, [42], "Один элемент"),
    (3, [-1, -5, -2], -1, [-2, -5, -1], "Отрицательные числа"),
    (0, [], None, [], "Пустой массив N=0"), 
    (-5, [], None, [], "Некорректное N"), 
    (3, [1, 2], None, [], "Недостаточно элементов"), 
])
def process_array_from_input(N, elements, expected_max, expected_reversed_arr, description, capsys):
    print(f"\n--- Тест Задание 2: {description} ---")
    
    actual_max, actual_reversed_arr = process_array_from_input(N, elements)
    
    print(f"    Вход: N={N}, элементы={elements}")
    print(f"    Ожидаемый максимум: {expected_max}, Полученный максимум: {actual_max}")
    print(f"    Ожидаемый массив в обратном порядке: {expected_reversed_arr}, Полученный: {actual_reversed_arr}")

    assert actual_max == expected_max, f"❌ FAIL: Максимальный элемент не совпадает."
    assert actual_reversed_arr == expected_reversed_arr, f"❌ FAIL: Массив в обратном порядке не совпадает."

    captured = capsys.readouterr()
    if N <= 0 or not elements[:N]:
        assert "Количество элементов должно быть положительным числом." in captured.out or "Массив пуст" in captured.out, "❌ FAIL: Неверное сообщение для некорректного N или пустого массива."
    else:
        assert f"Максимальный элемент: {expected_max}" in captured.out, "❌ FAIL: Максимальный элемент не выведен в консоль."
        assert f"Массив в обратном порядке: {expected_reversed_arr}" in captured.out, "❌ FAIL: Обратный массив не выведен в консоль."

    print("    ✅ Пройдено.")