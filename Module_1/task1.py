class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(point1, point2) -> float:
    """
    Расстояние между двумя точками
    """
    return round(((point1.x - point2.x) ** 2 +
                  (point1.y - point2.y) ** 2) ** 0.5, 2)


# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и
# используя функцию distance()

print("Расстояние между точками = ", distance(point1, point2))
