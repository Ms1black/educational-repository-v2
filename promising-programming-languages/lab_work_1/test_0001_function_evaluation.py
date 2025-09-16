import pytest
import math
from main import function_evaluation

def test_function_evaluation_output():
    print("\n--- Тест function_evaluation ---")
    
    actual_values = function_evaluation()

    expected_values = []
    x = 0.0
    step = 0.1
    while x < 1.2:
        val = math.sin(x) + math.pow((math.sin(math.pow(x,2))),2) + math.pow((math.sin(math.pow(x,3))),3)
        expected_values.append((x, val))
        x = round(x + step, 10)
    
    print(f"Ожидаемое количество точек: {len(expected_values)}, Получено: {len(actual_values)}")
    assert len(actual_values) == len(expected_values), "Длина списка результатов не совпадает"

    for i in range(len(expected_values)):
        x_expected, val_expected = expected_values[i]
        x_actual, val_actual = actual_values[i]
        
        print(f"  Точка {i}: X_ожид={x_expected:.6f}, Val_ожид={val_expected:.6f} | X_получено={x_actual:.6f}, Val_получено={val_actual:.6f}")
        
        assert x_actual == pytest.approx(x_expected, rel=1e-9), f"Неверное значение x в индексе {i}."
        assert val_actual == pytest.approx(val_expected, rel=1e-9), f"Неверное значение функции в индексе {i}."
    
    print("✅ PASS: function_evaluation генерирует корректные значения.")