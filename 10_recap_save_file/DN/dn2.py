# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

nadaljuj = True
while True:
    if not nadaljuj:
        break
    operator = input("Enter an operator [+, -, *, /]:  ")
    num_1 = input("Enter number 1: ")
    num_2 = input("Enter number 2: ")

    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
    except (ValueError, TypeError):
        print("Your have to use a number.")


    if operator == "+":
        print(num_1 + num_2)

    elif operator == "-":
        print(num_1 - num_2)

    elif operator == "*":
        print(num_1 * num_2)

    elif operator == "/":
        try:
            print(num_1 / num_2)
        except ZeroDivisionError as err:
            print("Your can't divide a number by 0.")
    else:
        print("operation not supported.")

    while True:
        more = input("Continue [y/n] ")
        if more.lower() == "n":
            print("bye")
            nadaljuj = False
            break
        elif more.lower() == "y":

            break
        else:
            print("please try again")
            continue
