"""
Quiz interface
help taken from followng:
# https://github.com/cherryWood55/Quiz-Game

"""
import json
import time

#qusetion list
QUESTION_LIST = ['quiz']

def post_question(question):
    """
    Method to post question
    """
    print("your question \n" + question)
    answer = input("Enter Your answer [a/b/c/d]: ")
    while(True):
        if answer.lower() in ['a', 'b', 'c', 'd']:
            return answer
        else:
            print("Invalid answer. Enter again")
            answer = input("Enter answer [a/b/c/d]: ")

def mark_question(key, value):
    """
    Method to mark questions
    """
    actual = value["answer"]
    if value["user_response"].lower() == actual.lower():
        print("Q.{0} Correct!\n".format(key))
        return 2
    else:
        print("Q.{0} Incorrect!".format(key))
        print("Correct Answer is ({0})".format(actual))
        print ("Learn more : " + value["more_info"] + "\n")
        return 0

def take_test(questions):
    """
    Method to take questions
    """
    mark = 0
    print("Instructions :\n1. Only one valid answer.\n2. Correct answer 2 marks\n3. Wrong answer 0 marks \n")
    # time.sleep(2)
    for key, value in questions.items():
        questions[key]["user_response"] = post_question(value["question"])
    print("\n---------- PRINTING RESULT----------\n")
    for key, value in questions.items():
        mark += mark_question(key, value)
    print("Your mark:", mark, "/", (2 * len(questions)))

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
