from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        (self.score, self.ans) = (quiz_brain.score, quiz_brain.ans)
        (self.q_text, self.end_of_quiz) = (quiz_brain.q, quiz_brain.end_of_quiz)

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.score}", font=("Ariel", 10, "italic"))
        self.score_label.grid(column=1, row=0)
        self.score_label.config(bg=THEME_COLOR, fg="white")

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question", fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"))

        right = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right, bd=0, highlightthickness=0, relief="flat", command=self.check_true)
        self.right_button.grid(column=0, row=2, sticky="n")
        self.right_button.config(padx=30, pady=30)

        wrong = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong, bd=0, highlightthickness=0, relief="flat", command=self.check_false)
        self.wrong_button.grid(column=1, row=2, sticky="n")
        self.wrong_button.config(padx=30, pady=30)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        (self.q_text, self.end_of_quiz) = self.quiz.next_question()
        if self.end_of_quiz:
            self.canvas.itemconfig(self.question_text, text=f"{self.q_text}\nFinal Score: {self.score}")
        else:
            self.canvas.itemconfig(self.question_text, text=self.q_text)

    def check_true(self):
        if self.end_of_quiz:
            pass
        else:
            (self.score, self.ans) = self.quiz.check_answer("True")
            self.score_label.config(text=f"Score: {self.score}")
            self.give_feedback()
            self.get_next_question()

    def check_false(self):
        if self.end_of_quiz:
            pass
        else:
            (self.score, self.ans) = self.quiz.check_answer("False")
            self.score_label.config(text=f"Score: {self.score}")
            self.give_feedback()
            self.get_next_question()

    def give_feedback(self):
        self.window.after(1, func=self.ans_fb)

    def ans_fb(self):
        if self.ans:
            self.canvas.config(bg="#C8FFBD")
        else:
            self.canvas.config(bg="#FFBDBD")



