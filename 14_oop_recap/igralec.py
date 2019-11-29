import random

# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.



class Player:

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def __str__(self):
        return f"Name: {self.name}\nHealth: {self.health}\nAttack: {self.attack}"

    def do_attack(self, player_obj):
        if self.name == player_obj.name:
            return False
        player_obj.health -= random.randint(0, self.attack)

    def is_alive(self):
        return self.health > 0


player_1 = Player(name="Steve", health=100, attack=10)
player_2 = Player(name="Jebediah", health=100, attack=5)

# Izvedi napad
player_1.do_attack(player_2)
print(player_1)
print(player_2)

player_2.do_attack(player_1)
print(player_1)
print(player_2)

