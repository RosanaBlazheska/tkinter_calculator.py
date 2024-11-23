**Simple Tkinter Calculator**
**Description**
This is a Python application that creates a basic GUI calculator using the tkinter library. 
The user can enter mathematical expressions into a text box, click the "presmetaj" (calculate) button, and view the result displayed below the button.

Features
A user-friendly graphical interface created using tkinter.
Allows the user to input any mathematical expression (e.g., 2+2, 5*3, 10/2) into a text field.
Displays the calculated result immediately after pressing the "presmetaj" button.
**Installation and Usage**
**Requirements**
_Python 3.x installed on your system._
_The tkinter library (comes pre-installed with Python)._
**Steps to Run the Application**
Clone this repository to your local machine:
git clone https://github.com/RosanaBlazheska/tkinter_calculator.py.git
cd tkinter.calculator.py
_Run the Python script:
python your_script_name.py_

A small GUI window will appear with the following:
A text box for entering mathematical expressions.
A button labeled "presmetaj" to calculate the result.
A label to display the calculated result.


Code Overview
Here's a summary of the code structure:

Entry Field (entry): A text box where users input their mathematical expression.
Button (button): Executes the calculation when clicked. It uses Python's built-in eval() function to evaluate the expression.
Label (label): Displays the result of the calculation.
The main logic is encapsulated in the presmetaj function, which:

Retrieves the user input from the entry field.
Evaluates the expression using eval().
Updates the label with the result.
