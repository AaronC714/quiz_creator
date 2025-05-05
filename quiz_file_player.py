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
    for raw_q in raw_questions:
        lines = [line.strip() for line in raw_q.strip().split("\n") if line.strip()]
        if len(lines) < 6:
            continue