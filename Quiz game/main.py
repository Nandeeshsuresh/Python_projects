from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for sentence in question_data:
    q_text = sentence["question"]
    q_answer = sentence["correct_answer"]
    question_bank.append(Question(q_text, q_answer))

quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was:  {quiz.score}/{quiz.question_number}")



