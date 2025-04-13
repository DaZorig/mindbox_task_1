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


# Вычислим площадь фигуры без знания типа фигуры
# Вопрос в том, какие данные известные у фигуры ?
# Допустим, известны все стороны и углы между ними


# Рассмотрим фигуры с 4-мя сторонами, необходимо написать проверку
# на тип фигуры (квадрат, прямоугольник,  ромб, параллелограм
def define_figure(side_one, side_two, side_three, side_four, angle_one, angle_two, angle_three, angle_four):
    if side_one == side_two and side_one == side_three and side_one == side_four:
        if angle_one == angle_two and angle_one == angle_three and angle_one == angle_four:
            return side_one**2  # Если все стороны и углы равны, то это фигура - квадрат, площадь = a^2
        else:  # Если не все углы равны, то эта фигура ромб, необходимо найти высоту для вычисления площади
            all_angles = [angle_one, angle_two, angle_three, angle_four]  # Добавим все углы в массив
            min_angle = min(all_angles)  # Найдем меньший из углов
            height = side_one * math.sin(min_angle * math.pi / 180)  # Т.к. min_angle - острый угол, найдем высоту ромба
            return side_one * height  # Вычислим площадь ромба как произведение стороны на высоту
    else:  # Проверим 4-угольник на тип фигуры (прямоугольник, параллелограм)
        all_sides = [side_one, side_two, side_three, side_four]
        min_side = min(all_sides)
        max_side = max(all_sides)
        all_sides.remove(min_side)
        all_sides.remove(max_side)
        flag = 0  # Флаг используется как проверка на то, чтобы было две пары одинаковых сторон
        for side in all_sides:
            if side == min_side or side == max_side:
                flag += 1
        if flag == 2:  # Эта фигура прямоугольник или параллелограм
            if angle_one == angle_two and angle_one == angle_three and angle_one == angle_four:
                return min_side * max_side  # Если все углы равны, то это фигура - прямоугольик, площадь = a*b
            else:  # Если не все углы равны, то эта фигура параллелограм, необходимо найти высоту для вычисления площади
                all_angles = [angle_one, angle_two, angle_three, angle_four]  # Добавим все углы в массив
                min_angle = min(all_angles)  # Найдем меньший из углов
                height = min_side * math.sin(
                    min_angle * math.pi / 180)  # Т.к. min_angle - острый угол, найдем высоту параллеограма
                return max_side * height  # Вычислим площадь параллелограма как произведение стороны на высоту


# Напишем юнит-тесты для проверки определенных функций
# Импортируем библиотеку unittest
import unittest


# Определим класс TestFunctions для создания тестов
class TestFunctions(unittest.TestCase):
    def test_circle_area(self):  # Проверка вычисления площади круга с точностью до двух знаков после запятой
        self.assertAlmostEqual(circle_area(4), 50.265, places=3)


    def test_triangle_area(self):  # Проверка вычисления площади треугольника с точностью до двух знаков после запятой
        self.assertAlmostEqual(triangle_area(6, 7, 8), 20.33, places=2)


    def test_right_triangle(self):  # Проверка определения прямоугольного прямоугольника по трем сторонам
        self.assertTrue(right_triangle(5, 12, 13))
        self.assertFalse(right_triangle(5, 6, 10))


    def test_define_figure(self):  # Проверка вычисления площади частных случаев четырехугольников
        self.assertAlmostEqual(define_figure(4, 4, 4, 4, 90, 90, 90, 90), 16)  # Квадрат
        self.assertAlmostEqual(define_figure(5, 5, 5, 5, 120, 60, 60, 120), 21.65, places=2)  # Ромб
        self.assertAlmostEqual(define_figure(4, 4, 8, 8, 90, 90, 90, 90), 32)  # Прямоугольник
        self.assertAlmostEqual(define_figure(5, 7, 7, 5, 120, 60, 60, 120), 30.31, places=2)  # Параллелограм


if __name__ == '__main__':
    unittest.main()
