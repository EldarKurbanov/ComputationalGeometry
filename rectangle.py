from point import Point


class Rectangle:
    def __init__(self, x=None, y=None):
        self.x, self.y = x, y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)


if __name__ == '__main__':
    p1 = Rectangle(Point(1, 1), Point(2, 2))
    p2 = Rectangle(Point(4, 5), Point(6, 8))
    print(p1, p2)
