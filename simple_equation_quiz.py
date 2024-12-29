'''
This module contains funcions such as,
    1. Generating two random numbers.
    2. Forming the equation.
    3. Displaying the equation using Tkinter, GUI and get the user answer.
    4. Check user answer against correct answer
    5. Display the message of whether the user answer is correct or not
'''

import random
import tkinter as tk
from tkinter import simpledialog, messagebox

# Function to generating two random numbers and return those two numbers.
def generate_two_randoms_numbers():
    first_number = random.randint(1,10)
    second_number = random.randint(1,10)
    return first_number, second_number

# Function to form the equation, eg: 3 x 𝑥 = 12.
def form_equation(first_number, second_number): 
    equation = f"{first_number} * 𝑥 = {second_number}"
    return equation

# Function to display the equation using Tkinter, GUI and get the user answer.
def display_equation(equation):
    try:
        # Get the answer from the user.
        user_answer = simpledialog.askfloat("Solve", equation)
  
        # If the user cancelled an input, display the message and retrun None.
        if user_answer is None:
            messagebox.showinfo("Cancelled", "You cancelled the input.")
            return None

    # Display the message, if any error occured while getting the input.  
    except Exception as e:
        messagebox.showinfo("An error occurred: {e}. Please enter a valid number")
    return user_answer

# Function to check user answer against correct answer and return the value as boolean.
def check_answer(first_number, second_number, user_answer):
    correct_answer =  second_number / first_number
    format_user_answer = f"{user_answer:.1f}"
    format_correct_answer = f"{correct_answer:.1f}"
    return format_correct_answer == format_user_answer

 # Function to display the message of whether the user answer is correct or not
def display_useranswer_correct_or_incorrect(score, iscorrect):
    if iscorrect == True:
        messagebox.showinfo("Result", "Your answer is correct, well done.")
        score += 1
    else:
        messagebox.showinfo("Result", "Your answer is wrong, better luck next time.")          
    return score 