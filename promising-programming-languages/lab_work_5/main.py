import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg, integrate
from PIL import Image, ImageDraw

def process_matrix_operations():
    chess_matrix = np.full((5, 5), -5)
    chess_matrix[::2, 1::2] = 7
    chess_matrix[1::2, ::2] = 7
    print("Исходная матрица:\n", chess_matrix)

    initial_determinant = linalg.det(chess_matrix)
    print(f"Определитель исходной: {initial_determinant:.2f}")

    values_range = np.arange(3, 15)
    target_mask = (values_range > 6) & (values_range < 8)
    values_range[target_mask] *= -1
    
    even_numbers_sum = values_range[values_range % 2 == 0].sum()
    
    modified_matrix = chess_matrix - even_numbers_sum
    print("Модифицированная матрица:\n", modified_matrix)
    
    modified_determinant = linalg.det(modified_matrix)
    print(f"Определитель итоговой: {modified_determinant:.2f}")

    plt.figure()
    labels = ['Исходная', 'Итоговая']
    values = [initial_determinant, modified_determinant]
    
    bars = plt.bar(labels, values, color=['blue', 'orange'])
    plt.title('Сравнение определителей')
    plt.ylabel('Значение')
    plt.axhline(0, color='black', linewidth=0.8)
    plt.ylim(-1, 1)
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., 
                 0.1 if height >= 0 else -0.1,
                 f'{height:.1f}',
                 ha='center', va='bottom', color='red', fontweight='bold')
    
    plt.show()

def solve_linear_equation_system():
    coefficients_matrix = np.array([[5, 7], [1, 2]])
    dependent_variable_vector = np.array([14, 3])
    
    solution = linalg.solve(coefficients_matrix, dependent_variable_vector)
    print(f"Решение системы: x = {solution[0]:.2f}, y = {solution[1]:.2f}")

def calculate_definite_integral():
    integrand_function = lambda x: np.sin(x) / (x + 1)
    integral_value, absolute_error = integrate.quad(integrand_function, 1, 3)
    print(f"Значение интеграла: {integral_value:.5f}")

def create_and_process_house_image():
    canvas_size = (400, 400)
    base_image = Image.new('RGB', canvas_size, 'white')
    draw_context = ImageDraw.Draw(base_image)
    
    house_walls_coords = [(100, 200), (300, 200), (300, 350), (100, 350)]
    roof_coords = [(100, 200), (200, 100), (300, 200)]
    window_coords = [(150, 250), (250, 250), (250, 300), (150, 300)]
    
    draw_context.polygon(house_walls_coords, fill='pink', outline='black')
    draw_context.polygon(roof_coords, fill=(255, 105, 180), outline='black')
    draw_context.polygon(window_coords, fill='lightblue', outline='black')
    
    base_image.save('house_original.jpg')
    
    grayscale_image = base_image.convert('L')
    grayscale_image.save('house_grayscale.jpg')
    print("Изображения сохранены (house_original.jpg и house_grayscale.jpg)")
    
    try:
        grayscale_image.show()
    except:
        pass

def plot_quadratic_function():
    x_values = np.arange(-10, 10.01, 0.01)
    y_values = x_values**2
    
    custom_linestyle = '--'
    custom_color = 'purple'
    custom_linewidth = 2
    
    plt.figure()
    plt.plot(
        x_values, 
        y_values, 
        color=custom_color, 
        linestyle=custom_linestyle, 
        linewidth=custom_linewidth, 
        label='y = x^2'
    )
    
    plt.title('График параболы')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    process_matrix_operations()
    solve_linear_equation_system()
    calculate_definite_integral()
    create_and_process_house_image()
    plot_quadratic_function()