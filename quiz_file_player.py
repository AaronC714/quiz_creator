#START

#INITIALIZE colorama for colored text output

#DEFINE FUNCTION clear_screen
    #IF operating system is Windows
        #EXECUTE "cls" command
    #ELSE
        #EXECUTE "clear" command

#DEFINE FUNCTION get_quiz_file_path
    #RETURN path to "question.txt" on user's Desktop

#DEFINE FUNCTION load_questions(filename)
    #IF file does not exist
        #DISPLAY error message
        #RETURN empty list

import random
import os
import sys
from time import sleep
from colorama import init, Fore, Style

#colorama
init(autoreset=True)

#cross-platform
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def get_quiz_file_path():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    return os.path.join(desktop_path, "quiz.txt")

#get questions from txt file
def load_questions(filename):
    if not os.path.exists(filename):
        print(Fore.RED + "⚠️ No quiz file found.")
        return []
    
    with open(filename, "r", encoding="utf-8") as file:
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
            'a': lines[1].replace("a) ", ""),
            'b': lines[2].replace("b) ", ""),
            'c': lines[3].replace("c) ", ""),
            'd': lines[4].replace("d) ", "")
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

    for index, ques in enumerate(questions, start=1):
        print(Style.BRIGHT + f"\n{'='*70}")
        print(Fore.CYAN + f"Question {index}: {ques['question']}\n")
        for option, text in ques['choices'].items():
            print(f"  {option}) {text}")

        print("\n" + "-" * 70)
        while True:
            answer = input(Fore.YELLOW + "Your answer (a/b/c/d): ").lower()
            if answer in ['a', 'b', 'c', 'd']:
                break
            print(Fore.RED + "❌ Invalid choice. Please select a, b, c, or d.")
        
        if answer == ques['correct']:
            print(Fore.GREEN + "✅ Correct!")
            score += 1
        else:
            correct_option = ques['correct']
            print(Fore.RED + f"❌ Incorrect. The correct answer was '{ques['choices'][correct_option]}'")

        sleep(1.5)
        clear_screen()

    
    #Final Score
    print("\n" + "=" * 70)
    print(Fore.MAGENTA + f"🏁 Quiz Over! You scored {score} out of {len(questions)}.\n")
    if score == len(questions):
        print(Fore.GREEN + "🌟 Perfect score! You're a quiz master!")
    elif score >= len(questions) // 2:
        print(Fore.CYAN + "💡 Good job! Keep practicing.")
    else:
        print(Fore.YELLOW + "📚 Keep studying and try again!")
    print("=" * 70 + "\n")

# Main entry
def main():
    filename = get_quiz_file_path()
    questions = load_questions(filename)
    play_quiz(questions)

if __name__ == "__main__":
    main()