THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Screen
        self.screen = Tk()
        self.screen.title("Quizz game")
        self.screen.config(background=THEME_COLOR, padx=20, pady=20)

        # Scoreboard
        self.score_label = Label(text="Score: {score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Some question text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.correct_btn = Button(image=true_img, highlightthickness=0, command=self.true_passed)
        self.wrong_btn = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.correct_btn.grid(column=0, row=2)
        self.wrong_btn.grid(column=1, row=2)

        self.get_next_question()

        self.screen.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_passed(self):
        self.quiz.check_answer("True")


    def false_pressed(self):
        self.quiz.check_answer("False")