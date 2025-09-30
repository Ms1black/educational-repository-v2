import pytest
from main import replace_zeros_with_average

@pytest.mark.parametrize("input_arr, expected_arr, description", [
    ([1.0, 0.0, 5.0, 0.0, 4.0], [1.0, 2.0, 5.0, 2.0, 4.0], "Несколько нулей"), 
    ([10.0, 20.0, 30.0], [10.0, 20.0, 30.0], "Нет нулей"), 
    ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], "Только нули"), 
    ([5.0], [5.0], "Один элемент, не ноль"), 
    ([0.0], [0.0], "Один элемент, ноль"), 
    ([], [], "Пустой массив"),
])
def replace_zeros_with_average(input_arr, expected_arr, description):
    print(f"\n--- Тест Задание 3: {description} ---")
    
    actual_arr = replace_zeros_with_average(input_arr)
    
    print(f"    Входной массив: {input_arr}")
    print(f"    Ожидаемый массив: {expected_arr}")
    print(f"    Полученный массив: {actual_arr}")

    if len(actual_arr) == len(expected_arr):
        for i in range(len(actual_arr)):
            assert actual_arr[i] == pytest.approx(expected_arr[i], rel=1e-9), f"❌ FAIL: Элемент {i} не совпадает."
    else:
        pytest.fail(f"❌ FAIL: Длина массива не совпадает. Ожидалось {len(expected_arr)}, получено {len(actual_arr)}.")
    
    print("    ✅ Пройдено.")