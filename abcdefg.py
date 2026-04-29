score = 0

print("=== Simple Quiz ===")

questions = [
    ("What is the capital of Nepal? ", "kathmandu"),
    ("5 + 3 = ? ", "8"),
    ("Which language is used in Python? ", "python")
]

for q, ans in questions:
    user = input(q).lower()
    if user == ans:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nYour score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent!")
elif score >= 2:
    print("Good job!")
else:
    print("Try again!")