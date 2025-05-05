import random
import os
import sys
from time import sleep
from colorama import init, Fore, Style

#colorama
init(autoreset=True)

#cross-platform
def clear_screen():
    os.system('cls' if os.name == 'int' else 'clear')

#get questions from txt file
def load_questions(filename):
    if not os.path.exists(filename):
        print(Fore.RED + "⚠️ No quiz file found.")
        return []
    
    with open(filename, "r") as file:
        content = file.read().strip()

    raw_questions = content.split("-" * 40)
    questions = []

    #skip incompete blocks
    for raw_ques in raw_questions:
        lines = [line.strip() for line in raw_ques.strip().split("\n") if line.strip()]
        if len(lines) < 6:
            continue

        ques_text = lines[0].replace("Question: ", "")
        choices = {
            'choice a': lines[1].replace("a) ", ""),
            'chocie b': lines[2].replace("b) ", ""),
            'choice c': lines[3].replace("c) ", ""),
            'choice d': lines[4].replace("d) ", "")
        }
        correct = lines[5].replace("Correct Answer: ", "").lower()

        questions.append({
            'question': ques_text,
            'choices': choices,
            'correct': correct
        })

    return questions

#play quiz
def play_quiz(questions):
    if not questions:
        print("No questions found for the quiz")
        return
    
    clear_screen()
    title = "🎉 Welcome to the Random Quiz Challenge! 🎉"
    print ("\n" + title.center(70, " "))
    print ("Answer the questions below and test your knowledge!\n".center(70))

    random.shuffle(questions)
    score = 0

    for index, questions in enumerate(questions, start=1):
        print(Style.BRIGHT + f"\n{'='*70}")
        print(Fore.CYAN + f"Question {i}: {q['question']}\n")
        for option, text in q['choices'].items():
            print(f"  {option}) {text}")

        print("\n" + "-" * 70)
        while True:
            answer = input(Fore.YELLOW + "Your answer (a/b/c/d): ").lower()
            if answer in ['a', 'b', 'c', 'd']:
                break
            print(Fore.RED + "❌ Invalid choice. Please select a, b, c, or d.")