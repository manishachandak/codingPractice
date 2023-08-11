class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        pass

    def volume(self):
        Result = ((self.height * 3.14) * self.radius ** 2)
        return Result

    def surface_area(self):
        Result = (((2 * 3.14) * self.radius * self.height) + ((2 * 3.14) * self.radius ** 2))
        return Result


cyl = Cylinder()
cyl.radius = 3
cyl.height = 5
print("volume",cyl.volume())
print("surface area",cyl.surface_area())
