import random

print("=== Keyword-Based Quiz (Final Score + Wrong Answer Message) ===")

quiz = [
    ("What is your favorite sleeping position of all time?", ["side", "back", "stomach"]),
    ("If you could have one superpower, what would it be and why?", ["invisible", "fly", "teleport", "strength"]),
    ("What’s the weirdest thing you’ve ever eaten?", ["insect", "frog", "snail", "weird"]),
    ("Would you rather have intelligence over looks?", ["intelligence", "smart"]),
    ("If you could meet anyone in this world today, who would you meet?", ["elon", "musk", "modi", "taylor", "cristiano"]),
    ("What’s the most absurd thing you’ve been tricked into doing or believing?", ["prank", "fake", "trick"]),
    ("What’s the best thing you’ve ever eaten?", ["pizza", "biryani", "pasta"]),
    ("If you could be a bagel, what type of bagel would you be?", ["cheese", "plain", "blueberry"]),
    ("What’s the first thing you do after getting home from a trip?", ["sleep", "rest", "unpack"]),
    ("What’s the craziest bet you have ever made?", ["money", "dare"]),
    ("If you could only use one word for the rest of your life, which would it be?", ["love", "peace", "fun"]),
    ("What’s the funniest movie you have ever seen?", ["hangover", "bean", "golmaal", "joker"]),
    ("What’s the worst thing you’ve ever done as a child and what was your punishment?", ["punish", "scolded", "grounded"]),
    ("If you could trade lives with anyone for a day, who would it be and why?", ["celebrity", "rich", "famous"]),
    ("What’s the most addictive game for you?", ["pubg", "freefire", "chess", "minecraft"])
]

print("Total Questions:", len(quiz))
num = int(input("How many random questions do you want? : "))

if num > len(quiz) or num <= 0:
    print(f" Please enter a number between 1 and {len(quiz)}.")
else:
    print(f"\n---------- Let's pick {num} random questions for you... ----------\n")

    random_quiz = random.sample(quiz, num)
    correct = 0

    for i, (question, keywords) in enumerate(random_quiz, start=1):
        print(f"Q{i}: {question}")
        answer = input("Your answer: ").lower()

        # Check if any keyword is present in the answer
        if any(k in answer for k in keywords):
            print("✅ Correct answer!\n")
            correct += 1
        else:
            print("❌ Wrong answer! (No matching keyword found)\n")

    # Final results
    percentage = (correct / num) * 100

    print("======================================")
    print(f" You got {correct} out of {num} questions correct!")
    print(f" Your Score: {percentage:.2f}%")

    # Performance description
    if percentage == 100:
        print(" Excellent! You nailed all the answers!")
    elif percentage >= 75:
        print(" Great job! You did really well!")
    elif percentage >= 50:
        print("Not bad! Keep improving.")
    else:
        print(" Needs improvement — try again!")
    print("======================================")
