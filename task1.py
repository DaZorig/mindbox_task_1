# Импортируем библиотеку math для использований математических функций и констант
import math


# Пишем функцию для определения площади круга по заданному радиусу (S = pi*r^2)
def circle_area(radius):
    return math.pi * radius ** 2


# Пишем функцию для определения площади треугольника по заданным сторонам (формула Герона)
def triangle_area(side_one, side_two, side_three):
    p = (side_one + side_two + side_three) / 2  # Находим полупериметр треугольника
    return math.sqrt(p * (p - side_one) * (p - side_two) * (p - side_three))


# Пишем функцию для проверки, является ли треугольник прямоугольным
# Функция вернет True, если будет выполняться теорема Пифагора, соответственно, треугольник будет прямоугольным
def right_triangle(side_one, side_two, side_three):
    all_sides = [side_one, side_two, side_three]  # Добавим все стороны в массив для удобства последующей работы
    hypotenuse = max(all_sides)  # Гипотетическая гипотенуза - большая среди сторон
    all_sides.remove(hypotenuse)  # Уберем из массива сторон гипотенузу
    return hypotenuse == math.sqrt(all_sides[0]**2 + all_sides[1]**2)


# Напишем юнит-тесты для проверки определенных функций
# Импортируем библиотеку unittest
import unittest


# Определим класс TestFunctions для создания тестов
class TestFunctions(unittest.TestCase):
    def test_circle_area(self):  # Проверка вычисления площади круга с точностью до двух знаков после запятой
        self.assertAlmostEqual(circle_area(4), 50.265, places=3)


    def test_triangle_area(self):  # Проверка вычисления площади треугольника с точностью до двух знаков после запятой
        self.assertAlmostEqual(triangle_area(6, 7, 8), 20.33, places=2)


    def test_right_triangle(self): # Проверка определения прямоугольного прямоугольника по трем сторонам
        self.assertTrue(right_triangle(5, 12, 13))
        self.assertFalse(right_triangle(5, 6, 10))


if __name__ == '__main__':
    unittest.main()