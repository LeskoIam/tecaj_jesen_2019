from math import pi

# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


class Circle:

    def __init__(self, r):
        self.r = r

    def area(self):
        return pi*self.r**2

    def circumference(self):
        return 2*pi*self.r


r = int(input("fd"))
c = Circle(r)
c1 = Circle(4)
print(c.area())
print(c.circumference())

print(c1.area())
print(c1.circumference())
