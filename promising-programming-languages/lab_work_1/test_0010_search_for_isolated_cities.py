import pytest
from main import search_for_isolated_cities

def test_search_for_isolated_cities():
    print("\n--- Тест search_for_isolated_cities ---")

    N1 = 5
    M1 = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0]
    ]
    expected_isolated1 = [1]
    actual_isolated1 = search_for_isolated_cities(N1, M1)
    assert actual_isolated1 == expected_isolated1, "Неверный список изолированных городов для M1."
    print(f"✅ PASS: Тест 1 (есть изолированные: {actual_isolated1})")

    N2 = 2
    M2 = [
        [0, 1],
        [1, 0]
    ]
    expected_isolated2 = []
    actual_isolated2 = search_for_isolated_cities(N2, M2)
    assert actual_isolated2 == expected_isolated2, "Неверный список изолированных городов для M2."
    print(f"✅ PASS: Тест 2 (нет изолированных)")

    N3 = 3
    M3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    expected_isolated3 = [1, 2, 3]
    actual_isolated3 = search_for_isolated_cities(N3, M3)
    assert actual_isolated3 == expected_isolated3, "Неверный список изолированных городов для M3 (все изолированы)."
    print(f"✅ PASS: Тест 3 (все изолированы: {actual_isolated3})")

    N4 = 4
    M4 = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    expected_isolated4 = [4]
    actual_isolated4 = search_for_isolated_cities(N4, M4)
    assert actual_isolated4 == expected_isolated4, "Неверный список изолированных городов для M4."
    print(f"✅ PASS: Тест 4 (сложная сеть: {actual_isolated4})")