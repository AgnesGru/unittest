# plottng with classes, operator overloading

import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # other is like another point
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x, y)  # we create a new point which is from adding a and b
        else:  # this is for floats
            x = self.x + other
            y = self.y + other
            return Point(x, y)

    def plot(self):
        plt.scatter(self.x, self.y)


# a.plot()
# plt.show()

# point1 = Point(4, 5)
# print(point1.x)

# a = Point(3, 3)
# b = Point(1, 1)
# c = a + b # we need special type ___ add__ to add it
# print(c.x, c.y)

# a = Point(0, 2)
# d = a + 5  # 5 is not a point
# print(d.x, d.y)

# a = Point(0, 2)
# d = a + Point(3, 3)
# print(d.x, d.y)
