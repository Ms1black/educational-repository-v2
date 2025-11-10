import random
import math

class Factory:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def geolocation(self):
        print(f"Координаты: x={self.x}, y={self.y}")


class Employee(Factory):

    def __init__(self, x, y):
        super().__init__(x, y)

    def ChangePosition(self, dx, dy):
        """Метод для изменения координат работника."""
        self.x += dx
        self.y += dy
        print(f"Работник переместился. Новые координаты: x={self.x}, y={self.y}")

    def department(self):
        """Метод для вывода информации об отделе."""
        print("Работник принадлежит к отделу продаж.")

factory = Factory(5, 10)
print("Информация о заводе:")
factory.geolocation()
print("-" * 20)

employee = Employee(50, 50)
print("Начальная информация о работнике:")
employee.geolocation()
employee.department()
print("-" * 20)

random_dx = random.randint(-20, 20)
random_dy = random.randint(-20, 20)
print(f"Смещение работника на dx={random_dx}, dy={random_dy}...")
employee.ChangePosition(random_dx, random_dy)
print("-" * 20)

distance = math.sqrt((factory.x - employee.x)**2 + (factory.y - employee.y)**2)

print("Итоговая информация:")
print("Координаты завода:")
factory.geolocation()
print("Текущие координаты рабочего:")
employee.geolocation()
print(f"Расстояние между заводом и рабочим: {distance:.2f}")