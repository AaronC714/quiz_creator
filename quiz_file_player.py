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