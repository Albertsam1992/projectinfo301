# Quiz Questions Dictionary
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"],
        "answer": 3
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["1. Earth", "2. Mars", "3. Venus", "4. Jupiter"],
        "answer": 2
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "choices": ["1. Charles Dickens", "2. J.K. Rowling", "3. William Shakespeare", "4. Mark Twain"],
        "answer": 3
    },
    {
        "question": "What is the largest mammal in the world?",
        "choices": ["1. Elephant", "2. Blue Whale", "3. Great White Shark", "4. Giraffe"],
        "answer": 2
    },
    {
        "question": "What is the smallest prime number?",
        "choices": ["1. 0", "2. 1", "3. 2", "4. 3"],
        "answer": 3
    }
]

# Initialize the score
score = 0

# Start the quiz
print("Welcome to the Quiz Game!")
print("Answer the questions by typing the number corresponding to your choice.\n")

# Loop through the questions
for i, item in enumerate(quiz_questions):
    print(f"Question {i+1}: {item['question']}")
    for choice in item['choices']:
        print(choice)
    
    # Get user's answer
    while True:
        try:
            user_answer = int(input("Your answer (1-4): "))
            if 1 <= user_answer <= 4:
                break
            else:
                print("Please enter a valid option (1-4).")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")

    # Check if the answer is correct
    if user_answer == item['answer']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {item['answer']}. {item['choices'][item['answer'] - 1]}\n")

# Display the final score
print(f"Quiz Over! You scored {score} out of {len(quiz_questions)}.")
