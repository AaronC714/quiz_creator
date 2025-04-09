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

        cont = input("Do you want to add another question? (yes/no): ").lower()
        if cont != 'yes':
            print("Exiting. Questions saved to", filename)
            break


#converting users input to txt file
def question_to_file(filename, question_data):
    with open(filename, "a") as file:
        file.write("Question: " + question_data['question'] + "\n")
        file.write("a) " + question_data['a'] + "\n")
        file.write("b) " + question_data['b'] + "\n")
        file.write("c) " + question_data['c'] + "\n")
        file.write("d) " + question_data['d'] + "\n")
        file.write("Correct Answer: " + question_data['correct'] + "\n")
        file.write("-" * 40 + "\n")


if __name__ == "__main__":
    main()