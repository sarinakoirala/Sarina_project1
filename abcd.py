while True:
    try:
        num = int(input("Enter a number (0 to exit): "))

        if num == 0:
            print("Program ended.")
            break

        if num % 2 == 0:
            print("The number is Even.")
        else:
            print("The number is Odd.")

    except ValueError:
        print("Please enter a valid number!")