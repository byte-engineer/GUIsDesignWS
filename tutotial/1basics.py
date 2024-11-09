#!tutotial/basics.py

#|> first we will start by installing the library: `pip install PyQt5`.
#|> Thin will need to import some modules from PyQt5.

from PyQt5 import QtWidgets

# instantiate this class in the beginning if any programe.
app = QtWidgets.QApplication([])

# Create a window on the class.
window = QtWidgets.QMainWindow()

# Add a lable to the window.
label = QtWidgets.QLabel('My First Window!', window)

# Add a button to the window.
btn = QtWidgets.QPushButton('Click Me!', window)
btn.move(100, 0)    # Move the button to the right.

# Show the window :)
window.show()

# Main loop.
app.exec_()