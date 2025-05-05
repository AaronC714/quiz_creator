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