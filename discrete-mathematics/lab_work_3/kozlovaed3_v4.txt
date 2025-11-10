import itertools
import numpy as np
import matplotlib.pyplot as plt

def task_1():

    print("Задача 1: Генерация 'слов'")
    
    symbols = ['X', 'Y', 'Z']
    word_length = 2

    words = list(itertools.product(symbols, repeat=word_length))
    
    print(f"Символы: {symbols}")
    print(f"Длина слова: {word_length}")
    print(f"Все возможные 'слова':")
    for word in words:
        print(''.join(word), end=' ')
    print(f"\n\nОбщее количество 'слов': {len(words)}")
    print("-" * 30 + "\n")


def task_2():

    print("Задача 2: Генерация сочетаний")
    
    letters = ['A', 'B', 'C', 'D', 'E']
    k = 4

    combinations = list(itertools.combinations(letters, k))
    
    print(f"Набор букв: {letters}")
    print(f"Размер комбинации: {k}")
    print(f"Все возможные комбинации:")
    for combo in combinations:
        print(combo)
    
    print(f"\nОбщее количество комбинаций: {len(combinations)}")
    print("-" * 30 + "\n")


def task_3():

    print("Задача 3: Генерация перестановок с оптимизацией (Задача коммивояжера)")
    
    cities = {
        0: "Москва",
        1: "Санкт-Петербург",
        2: "Казань",
        3: "Сочи"
    }
    
    distances = np.array([
        [0, 700, 800, 1200],
        [700, 0, 1100, 1500],
        [800, 1100, 0, 900],
        [1200, 1500, 900, 0]
    ])

    start_city_index = 0
    other_cities_indices = [i for i in cities if i != start_city_index]

    routes = list(itertools.permutations(other_cities_indices))

    min_distance = float('inf')
    best_route = None

    print("Все возможные маршруты, начинающиеся и заканчивающиеся в Москве:\n")
    
    for route in routes:
        full_route_indices = (start_city_index,) + route + (start_city_index,)
        current_distance = 0

        for i in range(len(full_route_indices) - 1):
            from_city = full_route_indices[i]
            to_city = full_route_indices[i+1]
            current_distance += distances[from_city, to_city]
            
        full_route_names = [cities[j] for j in full_route_indices]
        print(f"Маршрут: {' -> '.join(full_route_names)}, Расстояние: {current_distance} км")

        if current_distance < min_distance:
            min_distance = current_distance
            best_route = full_route_names
    
    print("\nРезультат")
    print(f"Самый короткий маршрут: {' -> '.join(best_route)}")
    print(f"Минимальное расстояние: {min_distance} км")
    print("-" * 30 + "\n")


def task_4():

    print("Задача 4: Генерация сочетаний с ограничениями")
    
    players = [f'P{i}' for i in range(1, 8)]
    team_size = 4
    restricted_pair = {'P1', 'P2'}

    all_teams = list(itertools.combinations(players, team_size))

    valid_teams = []
    for team in all_teams:
        if not restricted_pair.issubset(set(team)):
            valid_teams.append(team)

    print(f"Всего игроков: {players}")
    print(f"Размер команды: {team_size}")
    print(f"Ограничение: {restricted_pair} не могут играть вместе.")
    print("\nВсе допустимые комбинации команд:")
    for team in valid_teams:
        print(team)
    
    print(f"\nОбщее количество допустимых комбинаций: {len(valid_teams)}")
    print("-" * 30 + "\n")


def task_5():

    print("Задача 5: Исследование Принципа Дирихле")
    
    num_books = 1000
    num_shelves = 10
    num_experiments = 1000
    threshold = 100

    print(f"Условия: {num_books} книг, {num_shelves} полок.")
    print(f"Проверяемое утверждение: 'хотя бы на одной полке будет БОЛЕЕ {threshold} книг'.")
    
    pigeonhole_holds_count = 0
    
    for _ in range(num_experiments):

        distribution = np.random.multinomial(num_books, [1/num_shelves] * num_shelves)

        if np.any(distribution > threshold):
            pigeonhole_holds_count += 1

    success_rate = (pigeonhole_holds_count / num_experiments) * 100
    
    print("\nСтатистический анализ")
    print(f"Проведено экспериментов: {num_experiments}")
    print(f"Количество случаев, когда условие выполнилось: {pigeonhole_holds_count}")
    print(f"Вероятность выполнения принципа (в формулировке 'более 100'): {success_rate:.2f}%")

    print("\nВизуализация")
    final_distribution = np.random.multinomial(num_books, [1/num_shelves] * num_shelves)
    
    plt.figure(figsize=(10, 6))
    shelves_labels = [f"Полка {i+1}" for i in range(num_shelves)]
    plt.bar(shelves_labels, final_distribution, color='skyblue')
    
    plt.axhline(y=threshold, color='r', linestyle='--', label=f'Порог ({threshold} книг)')
    plt.title('Гистограмма распределения книг по полкам (один эксперимент)')
    plt.xlabel('Полки')
    plt.ylabel('Количество книг')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    print("Гистограмма сгенерирована. Пожалуйста, посмотрите в окне вывода графики.")
    plt.show()

    print("-" * 30 + "\n")


if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()