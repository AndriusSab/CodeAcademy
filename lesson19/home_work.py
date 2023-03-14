# import random

# class Question:
#         def __init__(self, question: str, answer: str, result: bool,)-> None:
#                self.question = question
#                self.answer = answer
#                self.result = result
        
#         def get_question(self):
#                 pass
        
#         def get_answer(self):
#             pass
        
        

# class Quiz(Question):
    
#         def get_question(self):
#             self.question = random.random(question_dict)
#             return self.question 
        
# uestiona = Questions()
# print (questiona)




# question_dict = {"Is the eart flat:" : "y",
#                  "Krym belongs to Ukraine": "n"}


# import random

# class Question:
#     def __init__(self, question: str, answer: str, result: bool):
#         self.question = question
#         self.answer = answer
#         self.result = result
    
#     def ask_question(self):
#         pass
    
#     def check_answer(self):
#         pass    
        
# class Quiz(Question):
#     def ask_question(self):
#         print(self.question)
#         while True:
#             try:
#                 self.answer = input("Please type y for YES and n for NO: ").strip().lower()
#                 if self.answer not in ["y", "n"]:
#                     raise ValueError("Invalid answer. Please type 'y' for YES or 'n' for NO.")
#                 break
#             except ValueError as e:
#                 print(e)
        
#     def check_answer(self):
#         return self.answer == self.result.lower()

# question_dict = {
#     "Is the earth round?": "y",
#     "Is python an interpreted language?": "y",
#     "Is the capital of France London?": "n"
# }

# questions = []
# for question, result in question_dict.items():
#     q = Quiz(question, result)
#     questions.append(q)

# score = 0
# for q in questions:
#     q.ask_question()
#     if q.check_answer():
#         print("Correct!")
#         score += 1
#     else:
#         print("Wrong!")
    
# print(f"You scored {score}/{len(questions)}")

# Sure! Here is a more detailed explanation of the code:

# score = 0: Initialize the score variable to 0.

# for q in questions:: Iterate over the list of questions.

# q.ask_question(): Call the ask_question() method of the current question object, which displays the question text and prompts the user to answer "yes" or "no". The user's answer is stored in the answer attribute of the question object.

# if q.check_answer():: Call the check_answer() method of the current question object, which checks if the user's answer is correct. If the answer is correct, the method returns True.

# print("Correct!"): If the user's answer is correct, print "Correct!" to the console.

# score += 1: If the user's answer is correct, increment the score variable by 1.

# else:: If the user's answer is incorrect, execute the code in the else block.

# print("Wrong!"): Print "Wrong!" to the console.

# print(f"You scored {score}/{len(questions)}"): After all the questions have been answered, print the user's final score out of the total number of questions.




class Question:
    def __init__(self, question: str, answer: str, result: bool):
        self.question = question
        self.answer = answer
        self.result = result
     
        
class Quiz(Question):
    def ask_question(self):
        print(self.question)
        self.answer = input("Please type y for YES and n for NO: ")
        
    def check_answer(self):
        return self.answer.lower() == self.result.lower()
    
    def get_scores(self):
        score = 0
        for q in self.questions:
            q.ask_question()
            if q.check_answer():
                print("Correct!")
                score += 1
            else:
                print("Wrong!")
        return f"You scored {score}/{len(self.questions)}"

question_dict = {
    "Is the earth round?": "y",
    "Is it true?" : "y",
    "Is the capital of France London?": "n"
}

questions = []
for question, result in question_dict.items():
    q = Quiz(question, result)
    questions.append(q)

quiz = Quiz("", "", "")
quiz.questions = questions

print(quiz.get_scores())

#print(self.question) is a line of code that prints the current question to the console. In the context of the ask_question() method of the Quiz class, this line is responsible for displaying the question to the user so they can read it and decide whether to answer "yes" or "no".

# When q.ask_question() is called later in the code, it will print the current question to the console, and the user will be prompted to type "y" for "yes" or "n" for "no" in response. The user's answer will be stored in the self.answer attribute of the Quiz instance, and later checked against the correct answer to determine whether the user got the question right or wrong.