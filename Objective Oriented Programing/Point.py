# plottng with classes

import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # other is like a point type
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)  # we create a new point which is from adding a and b points

    def plot(self):
        plt.scatter(self.x, self.y)


point1 = Point(4, 5)
print(point1.x)

a = Point(3, 3)
b = Point(1, 1)

# a.plot()
# plt.show()
c = a + b
print(c.x, c.y)
