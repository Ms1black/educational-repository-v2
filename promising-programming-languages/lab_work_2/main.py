def replace(input_string):
    count = input_string.count(':')
    modified_string = input_string.replace(':', '%')
    return modified_string, count

def process_array_from_input(N, elements):
    if N <= 0:
        print("Количество элементов должно быть положительным числом.")
        return None, None 

    arr = elements[:N] 
    if len(arr) < N: 
        print(f"Внимание: Получено меньше элементов ({len(arr)}) чем ожидалось ({N}).")
        
    if not arr: 
        print("Массив пуст, невозможно найти максимальный элемент или обратить.")
        return None, []


    max_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element
    
    print(f"Исходный массив: {arr}")
    print(f"Максимальный элемент: {max_element}")

    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    
    print(f"Массив в обратном порядке: {reversed_arr}")
    
    return max_element, reversed_arr

def replace_zeros_with_average(arr):
    if not arr:
        return []

    total_sum = 0.0 
    for item in arr:
        total_sum += item
    
    average = total_sum / len(arr)

    modified_arr = []
    for item in arr:
        if item == 0.0:
            modified_arr.append(average)
        else:
            modified_arr.append(item)
    
    return 

def create_phone_book_and_get_names(num_contacts, contact_data): 
    phone_book = {}
    if num_contacts <= 0:
        return [], {}

    for i in range(min(num_contacts, len(contact_data))):
        name, phone_number = contact_data[i]
        phone_book[name] = phone_number

    print("\nПолная телефонная книга:")
    for name, number in phone_book.items():
        print(f"  {name}: {number}")

    names_list = list(phone_book.keys())
    
    print(f"\nСписок всех имен: {names_list}") 
    return names_list, phone_book


def check_sequence_for_duplicates(sequence_str):
    results = []
    seen_numbers = set()

    numbers_str = sequence_str.split()

    print(f"Входная последовательность: {numbers_str}")
    print("Результаты проверки:")

    for num_str in numbers_str:
        try:
            number = int(num_str)
            if number in seen_numbers:
                results.append("Да")
            else:
                results.append("Нет")
                seen_numbers.add(number)
        except ValueError:
            results.append(f"Ошибка: '{num_str}' не является числом")

    for res in results:
        print(res)
        
    return results

def find_min_max_even_in_file(input_filename, output_filename):
    min_even = None
    max_even = None
    found_any = False

    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            for line in infile:
                try:
                    num = int(line.strip())
                    if num > 0 and num % 2 == 0:
                        found_any = True
                        if min_even is None or num < min_even:
                            min_even = num
                        if max_even is None or num > max_even:
                            max_even = num
                except ValueError:
                    continue 
    except FileNotFoundError:
        return None, None, "Входной файл не найден"
    
    result_message = ""
    if found_any:
        result_message = f"Минимальное четное положительное: {min_even}\n"
        result_message += f"Максимальное четное положительное: {max_even}\n"
    else:
        result_message = "Четных положительных чисел в файле не найдено.\n"

    try:
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(result_message)
    except Exception as e:
        return None, None, f"Ошибка записи файла: {e}"
        
    return min_even, max_even, result_message