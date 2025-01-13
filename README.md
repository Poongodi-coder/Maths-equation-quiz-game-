# Maths Equation Quiz Game

## User Manual

### Introduction
Welcome to the Maths equation quiz game! This program will test your math skills by generating random equations for you to solve. You will be presented with five equations, and your task is to solve them correctly. At the end of the quiz, your total score will be displayed.

### How to Use the Program

1. **Starting the Quiz**:
   - When you run the program, a series of pop-up windows will appear, each displaying a math equation.
   - You need to solve the equation and enter your answer in the provided input box.

2. **Answering Questions**:
   - Each equation will be in the form of `a * x = b`, where `a` and `b` are random numbers.
   - You need to find the value of `x` that satisfies the equation and enter it in the input box.

3. **Feedback**:
   - After you submit your answer, a message will appear indicating whether your answer was correct or incorrect.
   - Your score will be updated based on your answers.

4. **Completing the Quiz**:
   - The quiz consists of five questions.
   - After answering all questions, a final message will display your total score out of five.

### Example
- You might see an equation like `3 * x = 12`.
- To solve it, you would calculate `x = 12 / 3`, so `x = 4`.
- Enter `4` in the input box and submit your answer.

### Requirements
- Download Python: If you don’t have Python installed, download it from [official Python site](https://www.python.org/downloads/).
- Download VSC: A code editor. If you don’t have VSC installed, download it from [Visual Studio Code](https://code.visualstudio.com/).
- You also need the `tkinter` library, which is included in Python installations.

### Running the Program
- The program requires Python and Visual Studio Code to be installed on your computer.
- Save the two program files in a folder and name the module file as `simple_equation_quiz.py` and the main file as `maths_quiz_game.py`.
- In VSCode, you can usually run the program by clicking the “Run” button or pressing the `F5` function key on your keyboard.

## Technical Documentation

### Code Overview
The Maths equation quiz game program consists of the following main components:
- **Imports**: Import necessary libraries and modules.
- **launch_quiz function**: Main function to run the quiz.
- **Tkinter setup**: Create and manage the Tkinter main window.
### Detailed Code Explanation of main file - File name: maths_quiz_game.py
```Python
"""
The quiz process program:
1. Generate an equation with random numbers (e.g., 3 x 𝑥 = 12).
2. Use Tkinter to create a GUI for the quiz.
3. Check if the user’s answer is correct and display an appropriate message.
4. Repeat the process for five equations, keeping track of the user’s score.
5. Output the total score after all questions have been answered.
"""

import tkinter as tk 
from tkinter import simpledialog, messagebox
import simple_equation_quiz as seq

def launch_quiz():

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
```
### Module - File name: simple_equation_quiz.py
```Python
'''
This module contains functions such as,
    1. Generating two random numbers.
    2. Forming the equation.
    3. Displaying the equation using Tkinter, GUI and get the user answer.
    4. Check user answer against correct answer
    5. Display the message of whether the user answer is correct or not
'''

import random
import tkinter as tk
from tkinter import simpledialog, messagebox

def generate_two_randoms_numbers():
    first_number = random.randint(1,10)
    second_number = random.randint(1,10)
    return first_number, second_number

def form_equation(first_number, second_number): 
     equation = f"{first_number} * 𝑥 = {second_number}"
    return equation

def display_equation(equation):
    try:
        user_answer = simpledialog.askfloat("Solve", equation)
  
        if user_answer is None:
            messagebox.showinfo("Cancelled", "You cancelled the input.")
            return None

    except Exception as e:
        messagebox.showinfo("An error occurred: {e}. Please enter a valid number")
    return user_answer

def check_answer(first_number, second_number, user_answer):
    correct_answer =  second_number / first_number
    format_user_answer = f"{user_answer:.1f}"
    format_correct_answer = f"{correct_answer:.1f}"
    return format_correct_answer == format_user_answer

def display_useranswer_correct_or_incorrect(score, iscorrect):
    if iscorrect == True:
        messagebox.showinfo("Result", "Your answer is correct, well done.")
        score += 1
    else:
        messagebox.showinfo("Result", "Your answer is wrong, better luck next time.")          
    return score 
```
### Running the Program
1. **Prerequisites**:
   - Ensure that Python and Visual Studio Code (VSCode) are installed on your computer.

2. **File Setup**:
   - Save the two program files in a designated folder.
   - Name the module file `simple_equation_quiz.py`.
   - Name the main file `maths_quiz_game.py`.

3. **Execution**:
   - Open VSCode.
   - Run the program by clicking the “Run” button or pressing the `F5` key on your keyboard.

### Output
   - The program displays the equation as below:
     
     ![image info](https://github.com/Poongodi-coder/Maths-equation-quiz-game-/blob/main/01%20Display%20equation.png)

   - You enter 0.8 as the answer, the press OK button.
     
     ![image info](https://github.com/Poongodi-coder/Maths-equation-quiz-game-/blob/main/02%20Enter%20answer.png)

   - The program informs you that your answer is correct.
     
     ![image info](https://github.com/Poongodi-coder/Maths-equation-quiz-game-/blob/main/03%20Correct%20answer.png)
     
   - If you press the CANCEL button, the program will skip the question, display the message below, and continue to the next question.
     
     ![image info](https://github.com/Poongodi-coder/Maths-equation-quiz-game-/blob/main/04%20Cancelled%20message.png)
     
   - If wrong, program informs you that your answer is wrong.
     
     ![image info](https://github.com/Poongodi-coder/Maths-equation-quiz-game-/blob/main/05%20Wrong%20answer.png)
     
   - If the answer is not a number, the message box below will pop up. Press OK and continue trying to provide the correct answer for the same question.
     
     ![image info](https://github.com/Poongodi-coder/Maths-equation-quiz-game-/blob/main/06%20Not%20a%20number.png)
     
   - This repeats for four more equations.
     
   - Finally, the program displays your total score.
     
      ![image info](https://github.com/Poongodi-coder/Maths-equation-quiz-game-/blob/main/07%20Total%20score.png)
 
### Error Handling
The program includes error handling to manage invalid inputs and other exceptions, ensuring a smooth user experience.

### GUI Elements
   - simpledialog.askfloat: Prompts the user to enter a floating-point number.
   - messagebox.showinfo: Displays messages to inform the user about the correctness of their answers and the final score.

### Conclusion
This program provides a simple and interactive way to practice solving equations. By following the user manual, even those unfamiliar with Python can easily use the quiz. The technical documentation offers a deeper understanding of the code structure and functionality.
