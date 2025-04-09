#Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. Write the collected data to a text file. Ask another question until the user chose to exit.

#user input of questions, choices, and answers
def main():
    filename = "questions.txt"
    
    while True:
        print("\nEnter your multiple choice question:")
        question = input("Question: ")

        a = input("Answer a: ")
        b = input("Answer b: ")
        c = input("Answer c: ")
        d = input("Answer d: ")

        # Ensure correct answer is valid
        while True:
            correct = input("Which is the correct answer? (a/b/c/d): ").lower()
            if correct in ['a', 'b', 'c', 'd']:
                break
            print("Invalid input. Please enter one of a, b, c, or d.")

        question_data = {
            'question': question,
            'a': a,
            'b': b,
            'c': c,
            'd': d,
            'correct': correct
        }

        question_to_file(filename, question_data)