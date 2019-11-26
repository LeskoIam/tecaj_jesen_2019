# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


class Animal:
    def __init__(self, st_tac, rep):
        """Represents generic animal

        :param st_tac: number of paws
        :param rep: bool, has tail?
        """
        self.st_tac = st_tac
        self.rep = rep

    def __str__(self):
        return f"St. tac: {self.st_tac}\nIma rep: {self.rep}"

    def is_four_legged_creature(self):
        # if self.st_tac == 4:
        #     return True
        # return False
        return self.st_tac == 4


class Dog(Animal):
    def __init__(self, ime, pasma, st_tac, rep):
        self.ime = ime
        self.pasma = pasma

        super(Dog, self).__init__(st_tac, rep)

    def __str__(self):
        return f"Ime: {self.ime}\nPasma: {self.pasma}\nSt. tac: {self.st_tac}\nIma rep: {self.rep}"


fik = Dog("Fik", "bernardinec", 3, True)

print(fik)

print(fik.is_four_legged_creature())
