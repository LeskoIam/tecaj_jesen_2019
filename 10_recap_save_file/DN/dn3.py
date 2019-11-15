import random

# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

secret = random.randint(1, 10)
guess = 0

while guess != secret:
    guess = int(input("Ugani cifro med 1 in 10:"))

    if guess > secret:
        print("Aim lower:)")

    elif guess < secret:
        print("Aim higher:)")

if guess == secret:
    print("Bravo stari !")
else:
    print("Vec srece naslednjic")
