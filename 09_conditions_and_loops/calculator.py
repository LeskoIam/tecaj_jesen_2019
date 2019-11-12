# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

while True:
    operator = input("Vnesi operator [+, -]: ")
    num_a = int(input("Vnesi stevilko 1: "))
    num_b = int(input("Vnesi stevilko 2: "))

    if operator == "+":
        print(num_a + num_b)
    elif operator == "-":
        print(num_a - num_b)
    else:
        print("Operation not supported")

    more = input("Continue [n/y]: ")
    if more == "n":
        print("bye")
        break
