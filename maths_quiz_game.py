'''
This program will:
Generate equation with random numbers, such as, 3 x 𝑥 = 12.
Use Tkinter to create a GUI for the quiz.
Check if the user’s answer is correct and display an appropriate message.
Repeat the process for five equations, keeping track of the user’s score.
Output the total score after all questions have been answered.
'''

import tkinter as tk
from tkinter import simpledialog, messagebox
import simple_equation_quiz as seq

def launch_quiz():

    # This variable is used to track the user's score.
    score = 0

    # Constant variable, total number of questions will be asked for this quiz is five.
    NUMBER_OF_QUESTION = 5

    #Using for loop to generate three random equation
    for iteration in range(NUMBER_OF_QUESTION):

        # Call function to generating two random numbers and return those two numbers.
        first_number, second_number = seq.generate_two_randoms_numbers()

        # Call function to form the equation, eg: 3 x 𝑥 = 12.
        equation = seq.form_equation(first_number, second_number)

        # Call function to display the equation and get the user answer, using Tkinter, GUI.
        user_answer = seq.display_equation(equation)

        # If the user cancelled an input, then skip the rest of the loop.
        if user_answer == None:
            continue

        # Call function to check the user answer against the correct answer and store as boolean value.
        iscorrect = seq.check_answer(first_number, second_number, user_answer)   
        
        # Call function to display the message of whether the user answer is correct or not
        score = seq.display_useranswer_correct_or_incorrect(score, iscorrect)
        
    # Total score in message box
    messagebox.showinfo("Final score:", f"Your total score is {str(score)}/{str(NUMBER_OF_QUESTION)}")

# Create the main window
root = tk.Tk()

# Hide the main window
root.withdraw()

# Call the function to launch quiz
launch_quiz()

# Destroy the root window
root.destroy()