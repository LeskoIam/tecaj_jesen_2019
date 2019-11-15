while True:
    print("""
    Please choose math operation you would like to complete:
    + Addition
    - Subtraction
    * Multiplication
    / Division
    """)

    math_operation = input("Enter your choice (+, -, *, /): ")
    try:
        number_1 = float(input("Enter first number: "))
        number_2 = float(input("Enter second number: "))
    except ValueError as exc:
        print("nisi vnesel prav")
        continue

    if math_operation == "+":
        answer = number_1 + number_2
    elif math_operation == "-":
        answer = number_1 - number_2
    elif math_operation == "*":
        answer = number_1 * number_2
    elif math_operation == "/":
        answer = number_1 / number_2

    print(answer)

    calc_again = input("Would you like to calculate again? Enter 'y' or 'n': ")
    if calc_again.lower() == "y":
        continue
    elif calc_again.lower() == "n":
        print("See you later.")
        break
    else:
        print("You didn't choose right letter.")
        break
