#questions 3
import csv
# Read the questions and answers from the CSV file
questions = []
answers = []
with open('quiz.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        questions.append(row[0])
        answers.append(row[1])
# Ask the user for their name
user_name = input("What is your name? ")
# Initialize the score
score = 0
# Ask the questions and check the user's answers
for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Your answer (T/F): ").upper()
    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is", answers[i])
# Print the user's results
print(f"{user_name}, you scored {score} out of {len(questions)}.")
# Save the user's name and result to the CSV file
with open('quiz_results.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([user_name, score, len(quest