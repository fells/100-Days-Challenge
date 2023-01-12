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
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
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
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz")
            self.correct_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def true_passed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.screen.after(1000, self.get_next_question)
