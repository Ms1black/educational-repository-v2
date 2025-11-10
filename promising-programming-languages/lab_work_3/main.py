import random

def remove_chars_and_count(input_string):
    original_string = input_string
    removed_count = original_string.lower().count('а') 
    new_string = original_string.replace('а', '').replace('А', '')

    print(f"Исходная строка: {original_string}")
    print(f"Строка после удаления 'а' и 'А': {new_string}")
    print(f"Количество удаленных символов: {removed_count}")

def find_negative_pairs(arr):
    print(f"Исходный массив: {arr}")
    
    found_pairs = False
    for i in range(len(arr) - 1):
        if arr[i] < 0 and arr[i+1] < 0:
            print(f"Найденная пара: ({arr[i]}, {arr[i+1]})")
            found_pairs = True
    
    if not found_pairs:
        print("Отрицательные числа, стоящие рядом, не найдены.")

def remove_duplicates_from_array(original_arr):
    print(f"Исходный массив: {original_arr}")
    
    new_arr = []
    for item in original_arr:
        if item not in new_arr:
            new_arr.append(item)
    
    print(f"Массив с уникальными элементами (сохраняя порядок): {new_arr}")

def shop_checkout(products_data):
    print("Добро пожаловать в магазин!")
    for product, price in products_data.items():
        print(f" - {product.capitalize()}: {price} руб.")

    total_price = 0
    while True:
        try:
            num_items_to_buy = int(input("\nСколько разных товаров вы хотите купить? (Введите 0 для завершения): "))
            if num_items_to_buy == 0:
                break
            if num_items_to_buy < 0:
                print("Пожалуйста, введите положительное число.")
                continue
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

    items_bought_count = 0
    while items_bought_count < num_items_to_buy:
        item_name = input(f"Введите название товара для покупки ({items_bought_count + 1}/{num_items_to_buy}): ").lower()
        
        if item_name in products_data:
            total_price += products_data[item_name]
            print(f"'{item_name.capitalize()}' (цена: {products_data[item_name]} руб.) добавлен в корзину.")
            items_bought_count += 1
        else:
            print(f"Товара '{item_name.capitalize()}' нет в наличии. Попробуйте ввести другое название.")
    
    print(f"\nОбщая сумма покупки: {total_price} руб.")

def compare_strings_with_sets(str_a, str_b):
    print(f"Строка 1: '{str_a}'")
    print(f"Строка 2: '{str_b}'")

    set_a = set(str_a)
    set_b = set(str_b)

    if set_a == set_b:
        print(f"Строки '{str_a}' и '{str_b}' состоят из одинаковых символов.")
    else:
        print(f"Строки '{str_a}' и '{str_b}' состоят из разных символов.")

def sum_digits(n):
    s = 0
    n = abs(n)
    if n == 0:
        return 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def sort_numbers_by_digit_sum(input_file, output_file):
    numbers_with_sum = []

    try:
        with open(input_file, 'r') as infile:
            for line in infile:
                try:
                    num = int(line.strip())
                    numbers_with_sum.append((num, sum_digits(num)))
                except ValueError:
                    print(f"Предупреждение: Пропущена нечисловая строка '{line.strip()}' в файле '{input_file}'.")
    except FileNotFoundError:
        print(f"Ошибка: Входной файл '{input_file}' не найден. Пожалуйста, убедитесь, что файл существует по пути '{input_file}', или укажите полный путь к нему.")
        return
    except IOError:
        print(f"Ошибка: Произошла ошибка ввода-вывода при чтении файла '{input_file}'. Возможно, нет прав доступа.")
        return
    
    if not numbers_with_sum:
        print(f"В файле '{input_file}' не найдено ни одного числа для обработки. Выход.")
        return

    sorted_numbers = sorted(numbers_with_sum, key=lambda x: (x[1], x[0]))

    try:
        with open(output_file, 'w') as outfile:
            print(f"Числа из файла '{input_file}' отсортированы по сумме цифр и записаны в '{output_file}'.")
            for num, digit_sum in sorted_numbers:
                outfile.write(str(num) + '\n')
                print(f" - Число: {num}, Сумма цифр: {digit_sum}")
    except IOError:
        print(f"Ошибка: Не удалось записать в выходной файл '{output_file}'. Возможно, нет прав доступа.")

if __name__ == "__main__":
    
    print("Задание 1: Удаление символов 'а' и 'А'")
    input_str = "А роза упала на лапу Азора, А Зоя играла."
    remove_chars_and_count(input_str)

    print("\nЗадание 2: Пары отрицательных чисел, стоящих рядом")
    input_array_task2 = [10, -5, -8, 2, -1, 0, -3, -6, 7, -9]
    find_negative_pairs(input_array_task2)
    
    input_array_task2_no_negatives = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    find_negative_pairs(input_array_task2_no_negatives)

    print("\nЗадание 3: Удаление дубликатов из массива")
    input_array_task3 = [1, 5, 2, 8, 5, 1, 9, 2, 4, 8]
    remove_duplicates_from_array(input_array_task3)

    print("\nЗадание 4: Словарь товаров и расчет покупки ---")
    shop_products_data = {
        "яблоко": 50,
        "молоко": 100,
        "хлеб": 40,
        "сыр": 250,
        "сок": 80
    }
    shop_checkout(shop_products_data) 

    print("\nЗадание 5: Сравнение строк на одинаковые символы с использованием множеств")
    string_a_task5 = "programming"
    string_b_task5 = "grimmnigop"
    string_c_task5 = "program"
    compare_strings_with_sets(string_a_task5, string_b_task5)
    compare_strings_with_sets(string_a_task5, string_c_task5)

    input_file_path_task6 = "promising-programming-languages/lab_work_3/input_numbers.txt"
    output_file_path_task6 = "promising-programming-languages/lab_work_3/output_sorted_numbers.txt"
    sort_numbers_by_digit_sum(input_file_path_task6, output_file_path_task6)