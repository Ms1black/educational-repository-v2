import pytest
from main import search_for_isolated_cities

def test_search_for_isolated_cities():
    print("\n--- Тест search_for_isolated_cities ---")

    test_cases = [
        (5, [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]], [1], "Есть изолированные города"),
        (2, [[0, 1], [1, 0]], [], "Нет изолированных городов"),
        (3, [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [1, 2, 3], "Все города изолированы"),
        (4, [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], [4], "Более сложная сеть"),
    ]

    for N, M, expected_isolated, desc in test_cases:
        actual_isolated = search_for_isolated_cities(N, M)
        print(f"\n  Тестовый случай: {desc}")
        print(f"    Вход N: {N}")
        print(f"    Вход Matrix (первые 3x3): {M[:3]}...")
        print(f"    Ожидаемые изолированные города: {expected_isolated}")
        print(f"    Полученные изолированные города: {actual_isolated}")
        assert actual_isolated == expected_isolated, f"❌ FAIL для '{desc}'. Ожидалось {expected_isolated}, получено {actual_isolated}."
        print("    ✅ Пройдено.")

    print("\n✅ PASS: search_for_isolated_cities работает корректно.")