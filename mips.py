from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QFont


class MIPSWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Add a label for the input
        inputLabel = QLabel('Enter MIPS Instructions:', self)
        inputLabel.move(10, 10)
        inputLabel.setFont(QFont('Arial', 12))

        # Add a line edit for the input
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(10, 35)
        self.lineEdit.setFont(QFont('Arial', 12))
        self.lineEdit.resize(280, 20)

        # Add a button to run the simulator
        self.button = QPushButton('Simulate', self)
        self.button.move(10, 60)

        # Connect the button to the simulate function
        self.button.clicked.connect(self.simulate)

        # Add a label for the output
        self.outputLabel = QLabel(self)
        self.outputLabel.move(10, 90)
        self.outputLabel.setFixedWidth(280)
        self.outputLabel.setWordWrap(True)

        # Set the main window properties
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle('MIPS Simulator')
        self.show()

    def simulate(self):
        # Get the input text from the line edit
        input_text = self.lineEdit.text()

        # Simulate the MIPS instructions
        # Here you would write the code to simulate the instructions and
        # get the contents of each register
        # For the purpose of this example, we will just assume that the
        # contents of the registers are stored in a dictionary called
        # register_contents
        register_contents = {'$zero': 0, '$v0': 10, '$a0': 5, '$a1': 7}

        # Set the output label text to the contents of the registers
        output_text = 'Register Contents:\n'
        for register, content in register_contents.items():
            output_text += f'{register}: {content}\n'
        self.outputLabel.setText(output_text)


if __name__ == '__main__':
    app = QApplication([])
    window = MIPSWindow()
    app.exec()
