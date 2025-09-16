import pytest
import random
from main import format_array_from_array

def test_format_array_from_array():
    print("\n--- Тест format_array_from_array ---")

    random.seed(42) 

    array_A, array_Y = format_array_from_array()
    
    print(f"  Длина массива A: {len(array_A)}")
    print(f"  Первые 5 элементов A: {array_A[:5]}...")
    assert len(array_A) == 75, f"❌ FAIL: Длина массива A неверна. Ожидалось 75, получено {len(array_A)}."
    
    print(f"  Массив A содержит все значения в диапазоне [-5, 40]")
    for val in array_A:
        assert -5 <= val <= 40, f"❌ FAIL: Массив A содержит значение {val} вне диапазона [-5, 40]."
    
    expected_Y_from_A = [val for val in array_A if val < 20]
    
    print(f"  Длина массива Y: {len(array_Y)}")
    print(f"  Первые 5 элементов Y: {array_Y[:5]}...")
    print(f"  Ожидаемый Y (частично): {expected_Y_from_A[:5]}...")
    
    assert sorted(array_Y) == sorted(expected_Y_from_A), "❌ FAIL: Массив Y не соответствует ожидаемому."
    
    print("✅ PASS: format_array_from_array работает корректно.")