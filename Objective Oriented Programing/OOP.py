import turtle


class Polygons:
    def __init__(self, sides, name, size=100, color='red', line_thickness=4):
        self.sides = sides
        self.name = name
        self.size = size
        self.line_thickness = line_thickness
        self.color = color
        self.interior_angles = (self.sides - 2) * 180
        self.angle = self.interior_angles / self.sides

    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(self.size)  # 100 pixels
            turtle.right(180 - self.angle)  # angle


# print("8" * 100)
# def draw_function(sides, name, angle, size, color, line_thickness):  # without class method
#     turtle.color(color)
#     turtle.pensize(line_thickness)
#     for i in range(sides):
#         turtle.forward(size)  # 100 pixels
#         turtle.right(180 - angle)  # angle
#     turtle.done()
# print("8" * 100)


# square = Polygons(4, "Square")
# pentagon = Polygons(5, "Pentagon")
# square.draw()
# print(square.interior_angles)
# print(square.angle)
# pentagon.draw()
# hexagon = Polygons(6, "Hexagon", color='blue', line_thickness=20)
# hexagon.draw()

# ############## without class method ###############
# draw_function(4, "Square", 90, 100, "yellow", 10) # without class method
# ###################################################
## Sub -classing, method overwriting

class Square(Polygons):
    def __init__(self, size=100, color='red', line_thickness=4):
        super().__init__(4, "Square", size, color, line_thickness)

    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()


square = Square(color="#abcd11")

print(square.sides)
print(square.angle)
square.draw()
turtle.done()