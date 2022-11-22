"""
        CLASS
        How to create you're own Class

        class User:
            def __init__(self, user_id, username, height):
                self.id = user_id
                self.username = username
                self.height = height
                self.followers = 0
                self.following = 0

            def follow(self, user):
                '''Function where you tell what user will follow another account'''
                user.followers += 1
                self.following += 1


        user1 = User("001", "Michel", 1.80)
        user2 = User("002", "Fabio", 1.90)
        user2.follow(user1)
        user1.follow(user2)

        print(user1.username)
        print(f"User 2 Followers: {user2.followers}\n"
              f"User 1 Followers: {user1.followers}\n"
              f"User 2 Following: {user2.following}\n"
              f"User 1 Following: {user1.following}")


"""

# FINAL PROJECT
# Building a Quizz Game

import data
from question_model import Question
from quiz_brain import QuizzBrain

data_bank = []

for question in data.question_data:
    question_text = question["text"]
    answers_text = question["answer"]
    new_question = Question(question_text, answers_text)
    data_bank.append(new_question)

quiz = QuizzBrain(data_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
