# 0001_test_function_evaluation.py
import pytest
import math
from main import function_evaluation # Импорт функции из main.py

# АДАПТИРОВАНО: Этот тест предполагает, что function_evaluation не принимает аргументов
def test_function_evaluation_fixed_output():
    # Функция function_evaluation() всегда вычисляет один и тот же фиксированный диапазон (x от 0.0 до 1.1).
    # Мы не можем изменить диапазон через параметры.
    
    results = function_evaluation() # <--- ВЫЗЫВАЕТСЯ БЕЗ АРГУМЕНТОВ
    
    # x < 1.2 означает 0.0, 0.1, ..., 1.1 - всего 12 значений.
    assert len(results) == 12

    # Проверяем первое значение (для x=0.0)
    expected_f_x_00 = math.sin(0.0) + math.pow(math.sin(math.pow(0.0,2)),2) + math.pow(math.sin(math.pow(0.0,3)),3)
    assert math.isclose(results[0][0], 0.0, rel_tol=1e-9)
    assert math.isclose(results[0][1], expected_f_x_00, rel_tol=1e-6)

    # Проверяем последнее значение (для x=1.1)
    x_last = 1.1
    expected_f_x_last = math.sin(x_last) + math.pow(math.sin(math.pow(x_last,2)),2) + math.pow(math.sin(math.pow(x_last,3)),3)
    assert math.isclose(results[11][0], x_last, rel_tol=1e-9)
    assert math.isclose(results[11][1], expected_f_x_last, rel_tol=1e-6)

    # Убедимся, что 1.2 не включено (потому что цикл while x < 1.2)
    # На самом деле, math.isclose(results[11][0], 1.1, rel_tol=1e-9)
    assert results[11][0] < 1.2

# Удалены параметризованные тесты и тесты с передачей x_end_value,
# потому что function_evaluation() их не принимает.
# Включаю здесь тест, который будет пропущен для демонстрации в отчете
@pytest.mark.skip(reason="Эта функция пока неактивна или в разработке (демонстрация пропуска).")
def test_skipped_function_evaluation_example():
    assert function_evaluation()[0][1] == 0.0 