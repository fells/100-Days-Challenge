class QuizzBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.num = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number}: {current_question}. (True/False) ?: ")
