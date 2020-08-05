"""
Quiz interface
help taken from followng:
# https://github.com/cherryWood55/Quiz-Game
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python

"""
import json
import time
import os

os.system("")

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

#qusetion list
QUESTION_LIST = ['quiz']

def post_question(question):
    """
    Method to post question
    """
    print(style.YELLOW +  "your question \n" + style.UNDERLINE + question)
    answer = input(style.GREEN + "Enter Your answer [a/b/c/d]: ")
    while(True):
        if answer.lower() in ['a', 'b', 'c', 'd']:
            return answer
        else:
            print(style.GREEN + "Invalid answer. Enter again")
            answer = input(style.GREEN + "Enter answer [a/b/c/d]: ")

def mark_question(key, value):
    """
    Method to mark questions
    """
    actual = value["answer"]
    if value["user_response"].lower() == actual.lower():
        print(style.GREEN + "Q.{0} Correct!\n".format(key))
        return 2
    else:
        print(style.RED + "Q.{0} Incorrect!".format(key))
        print(style.GREEN + "Correct Answer is ({0})".format(actual))
        print (style.CYAN + "Learn more : " + value["more_info"] + "\n")
        return 0

def take_test(questions):
    """
    Method to take questions
    """
    mark = 0
    print(style.CYAN + "Instructions :\n1. Only one valid answer.\n2. Correct answer 2 marks\n3. Wrong answer 0 marks \n")
    # time.sleep(2)
    for key, value in questions.items():
        questions[key]["user_response"] = post_question(value["question"])
    print("\n---------- PRINTING RESULT----------\n")
    for key, value in questions.items():
        mark += mark_question(key, value)
    print(style.GREEN + "Your mark:", mark, "/", (2 * len(questions)))

def load_question(filename):
    """
    Load the question from the json file
    """
    questions = None
    with open(filename, "r") as read_file:
        questions = json.load(read_file)
    return (questions)

def play_quiz():
    """
    Method for playing quiz
    """
    flag = False
    if not flag:
        questions = load_question('questions/'+QUESTION_LIST[0]+'.json')
        take_test(questions)
    else:
        play_quiz()

if __name__ == '__main__':

    play_quiz()
