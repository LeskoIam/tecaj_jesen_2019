# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


class Hisa:

    def __init__(self, st_vrat, st_oken, st_dimnikov):
        self.st_vrat = st_vrat
        self.st_oken = st_oken
        self.st_dimnikov = st_dimnikov

    def show(self):
        print(f"St. vrat: {self.st_vrat}\nSt. oken: {self.st_oken}\nSt. dimnikov: {self.st_dimnikov}")

    def add_window(self, n=None):
        if n is None:
            self.st_oken += 1
        else:
            self.st_oken += n


my_house = Hisa(1, 5, 1)
your_house = Hisa(2, 1, 2)

my_house.show()
your_house.show()

print("-"*20)
my_house.show()
my_house.add_window()
my_house.show()
my_house.add_window(100)
my_house.show()
