"""
The quiz process program:
1. Generate an equation with random numbers (e.g., 3 x 𝑥 = 12).
2. Use Tkinter to create a GUI for the quiz.
3. Check if the user’s answer is correct and display an appropriate message.
4. Repeat the process for five equations, keeping track of the user’s score.
5. Output the total score after all questions have been answered.
"""

# Importing the Tkinter library for creating graphical user interfaces
import tkinter as tk 
# Importing simple dialog boxes for user input from the Tkinter library
from tkinter import simpledialog, messagebox
# Importing the custom module for generating and handling simple equation quizzes
import simple_equation_quiz as seq

def launch_quiz():
    """
    Launches a simple equation quiz.
    The quiz consists of a series of questions where the user is asked to solve
    simple equations. The user's score is displayed at the end of the quiz.
    """

    score = 0
    NUMBER_OF_QUESTION = 5

    for iteration in range(NUMBER_OF_QUESTION):

        first_number, second_number = seq.generate_two_randoms_numbers()
        equation = seq.form_equation(first_number, second_number)
        user_answer = seq.display_equation(equation)

        if user_answer is None:
            continue

        iscorrect = seq.check_answer(first_number, second_number, user_answer)           
        score = seq.display_useranswer_correct_or_incorrect(score, iscorrect)
        
    messagebox.showinfo("Final score:", f"Your total score is {str(score)}/{str(NUMBER_OF_QUESTION)}")

root = tk.Tk()
root.withdraw()
launch_quiz()
root.destroy()
