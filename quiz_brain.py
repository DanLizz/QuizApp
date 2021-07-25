import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.ans = True
        self.question_list = q_list
        self.current_question = None
        self.q = ""
        self.end_of_quiz = True

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            q_text = html.unescape(self.current_question.text)
            self.q = f"Q.{self.question_number}: {q_text} (True/False): "
            self.end_of_quiz = False
            return self.q, self.end_of_quiz
            self.check_answer(ans)
        else:
            self.q = "End of Quiz"
            self.end_of_quiz = True
            return self.q, self.end_of_quiz

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            self.ans = True
        else:
            self.ans = False
        return self.score, self.ans


