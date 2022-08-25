import os
import random
class Quiz():
    def __init__(self,questions):
        self.points = 0
        self.asked = 0
        input("press enter to start the quiz")
        os.system('cls')
        random.shuffle(questions)
        for question in questions:
            print(f"The statement goes: {question.text}")
            answer = input("Is this True or False\n")
            if answer == question.answer:
                Quiz.correct(self)
            else:
                Quiz.wrong(self)
        input(f"Sorry but this is the end of the quiz your score was: {self.points}/{self.asked}")
    def correct(self):
        self.points +=1
        self.asked += 1
        print(f"Thats correct you score is: {self.points}/{self.asked}")
        input("Press enter for next question")
        os.system('cls')
    def wrong(self):
        self.asked += 1
        print(f"Thats wrong you score is: {self.points}/{self.asked}")
        input("Press enter for next question")
        os.system('cls')