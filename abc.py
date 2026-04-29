password = "admin123"

attempts = 3

while attempts > 0:
    user_input = input("Enter password: ")

    if user_input == password:
        print("Access granted!")
        break
    else:
        attempts -= 1
        print("Incorrect password.")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Access denied!")