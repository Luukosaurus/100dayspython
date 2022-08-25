from question_model import question
from data import question_data
from quiz_brain import Quiz
done = False
questionlist = []
for i in question_data:
    new_question = question(i["text"],i["answer"])
    questionlist.append(new_question)
Quiz(questionlist)
