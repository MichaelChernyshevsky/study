class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, x1, y1, x2, y2):

        self.top_left = Point(min(x1, x2), min(y1, y2))
        self.bottom_right = Point(max(x1, x2), max(y1, y2))

    def is_contains(self, point: Point) -> bool:
        return self.top_left.x <= point.x < self.bottom_right.x and self.top_left.y <= point.y < self.bottom_right.y


def calculate_rectangles_intersections(rectangles: list[Rectangle], point: Point) -> int:
    intersections: int = 0
    for rectangle in rectangles:
        if rectangle.is_contains(point):
            intersections += 1
    return intersections


def get_point(line: str) -> Point:
    x, y = line.split()
    return Point(int(x), int(y))


def get_rectangle(line: str) -> Rectangle:
    x1, y1, x2, y2 = line.split()
    return Rectangle(int(x1), int(y1), int(x2), int(y2))


points = []
rectangles = []
n = int(input())
for i in range(0, n):
    rectangles.append(get_rectangle(input()))
m = int(input())
for i in range(0, m):
    points.append(get_point(input()))

for point in points:
    print(calculate_rectangles_intersections(rectangles, point), end=' ')
print()
