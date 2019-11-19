import random

# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

with open("score.txt", "r") as score_file:
    old_scores_raw = score_file.read()
old_scores_raw = old_scores_raw.split("\n")


old_scores = []
for i in old_scores_raw[:-1]:
    old_scores.append(int(i))


# old_scores = [int(x) for x in old_scores_raw[:-1]]  # List comprehension - isto kot zgornja for zanka

min_score = min(old_scores)
print(f"Best result so far {min_score}")

secret_num = random.randint(1, 100)

attempts = 0
while True:
    guess = int(input("Ugibaj stevilo med 1 in 100: "))
    attempts += 1  # attempts = attempts + 1

    if guess < secret_num:
        print("Guess higher")
    elif guess > secret_num:
        print("Guess lower")
    else:
        print("Bravo, you guessed in {0} tries".format(attempts))
        break

with open("score.txt", "a") as score_file:
    score_file.write(f"{attempts}\n")
