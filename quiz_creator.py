#Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. Write the collected data to a text file. Ask another question until the user chose to exit.

#user input of questions, choices, and answers
def main():
    filename = "questions.txt"
    
    while True:
        print("\nEnter your multiple choice question:")
        question = input("Question: ")