import pytest
from main import counter_words_starting_with_A

def test_counter_words_starting_with_A():
    print("\n--- Тест counter_words_starting_with_A ---")
    
    test_cases = [
        ("Apple Banana orange ANNA", 2, "Смешанный регистр, английские"),
        ("Анна Банан апельсин Арбуз", 3, "Смешанный регистр, русские"),
        ("Бананы Груши Яблоки", 0, "Нет слов на 'А'"),
        ("", 0, "Пустая строка"),
        ("Арбузы, Апельсины! Ананасы?", 3, "Пунктуация"),
        ("А", 1, "Одно слово на 'А'"),
        ("А1234 А3456 Банан", 2, "Цифры и 'А'"),
        ("а б в г д а", 2, "Короткие слова"),
    ]

    for text_input, expected, desc in test_cases:
        actual = counter_words_starting_with_A(text_input)
        print(f"\n  Тестовый случай: {desc}")
        print(f"    Входной текст: '{text_input}'")
        print(f"    Ожидалось: {expected}, Получено: {actual}")
        assert actual == expected, f"❌ FAIL для '{desc}'. Ожидалось {expected}, получено {actual}."
        print("    ✅ Пройдено.")

    print("\n✅ PASS: counter_words_starting_with_A работает корректно.")