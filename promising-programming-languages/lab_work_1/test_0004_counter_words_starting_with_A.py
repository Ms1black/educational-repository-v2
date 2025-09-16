import pytest
from main import counter_words_starting_with_A

def test_counter_words_starting_with_A():
    print("\n--- Тест counter_words_starting_with_A ---")
    assert counter_words_starting_with_A("Apple Banana orange ANNA") == 2, "Смешанный регистр, английские"
    assert counter_words_starting_with_A("Анна Банан апельсин Арбуз") == 3, "Смешанный регистр, русские"
    assert counter_words_starting_with_A("Бананы Груши Яблоки") == 0, "Нет слов на 'А'"
    assert counter_words_starting_with_A("") == 0, "Пустая строка"
    assert counter_words_starting_with_A("Арбузы, Апельсины! Ананасы?") == 3, "Пунктуация"
    assert counter_words_starting_with_A("А") == 1, "Одно слово на 'А'"
    assert counter_words_starting_with_A("А1234 А3456 Банан") == 2, "Цифры и 'А'"
    assert counter_words_starting_with_A("а б в г д а") == 2, "Короткие слова"
    print("✅ PASS: counter_words_starting_with_A работает корректно.")