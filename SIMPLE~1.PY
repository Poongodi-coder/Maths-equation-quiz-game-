# Import the random module for generating random numbers.
import random
# Import the tkinter module for creating GUI applications.
import tkinter as tk
# Import specific tkinter components for dialogs and message boxes.
from tkinter import simpledialog, messagebox

def generate_two_randoms_numbers():
    """
    Generate two random integers between 1 and 10, inclusive.

    This function uses the `random.randint` method to generate two random 
    integers within the specified range and returns them as a tuple.

    Returns:
        tuple: A tuple containing two random integers between 1 and 10.
    """
    first_number = random.randint(1,10)
    second_number = random.randint(1,10)
    return first_number, second_number

def form_equation(first_number, second_number): 
    """
    Form an equation of the form 'a * x = b', eg: 3 x 𝑥 = 12.

    This function takes two numbers as input and returns a string representing
    an equation where the first number is multiplied by 'x' and set equal to 
    the second number.

    Args:
        first_number (int or float): The coefficient of 'x'.
        second_number (int or float): The constant term on the right side of the equation.

    Returns:
        str: A string representing the equation in the form 'a * x = b'.
    """
    equation = f"{first_number} * 𝑥 = {second_number}"
    return equation


def display_equation(equation):
    """
    Display the equation using Tkinter GUI and get the user's answer.

    This function uses Tkinter to display a dialog box with the given equation
    and prompts the user to enter a floating-point number as the answer. If the 
    user cancels the input, a message is displayed, and the function returns None.
    If an error occurs while getting the input, an error message is displayed.

    Args:
        equation (str): The equation to be displayed in the dialog box.

    Returns:
        float or None: The user's answer as a floating-point number, or None if 
        the input is cancelled or an error occurs.
    """
    try:
        user_answer = simpledialog.askfloat("Solve", equation)
  
        if user_answer is None:
            messagebox.showinfo("Cancelled", "You cancelled the input.")
            return None

    except Exception as e:
        messagebox.showinfo("An error occurred: {e}. Please enter a valid number")
    return user_answer


def check_answer(first_number, second_number, user_answer):
    """
    Check the user's answer against the correct answer and return the result as a boolean.

    This function calculates the correct answer by dividing the second number by the first number.
    It then formats both the user's answer and the correct answer to one decimal place and compares them.

    Args:
        first_number (int or float): The coefficient of 'x' in the equation.
        second_number (int or float): The constant term on the right side of the equation.
        user_answer (float): The user's answer to the equation.

    Returns:
        bool: True if the formatted user's answer matches the formatted correct answer, False otherwise.
    """
    correct_answer =  second_number / first_number
    format_user_answer = f"{user_answer:.1f}"
    format_correct_answer = f"{correct_answer:.1f}"
    return format_correct_answer == format_user_answer

def display_useranswer_correct_or_incorrect(score, iscorrect):
    """
    Display a message indicating whether the user's answer is correct or not.

    This function uses Tkinter to display a message box with the result of the user's answer.
    If the answer is correct, a congratulatory message is shown and the score is incremented by 1.
    If the answer is incorrect, an encouragement message is shown.

    Args:
        score (int): The current score of the user.
        iscorrect (bool): A boolean indicating whether the user's answer is correct.

    Returns:
        int: The updated score after evaluating the user's answer.
    """
    if iscorrect == True:
        messagebox.showinfo("Result", "Your answer is correct, well done.")
        score += 1
    else:
        messagebox.showinfo("Result", "Your answer is wrong, better luck next time.")          
    return score 
