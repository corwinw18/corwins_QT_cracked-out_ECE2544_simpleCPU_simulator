import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QFont

class MIPSWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setGeometry(100, 100, 800, 300)
        self.setWindowTitle("MIPS Simulator")

        # Add a label for the input
        self.inputLabel = QLabel("Enter MIPS Instructions:")
        self.inputLabel.setFont(QFont("Arial", 12))

        # Add a text edit for the input
        self.textEdit = QTextEdit()
        self.textEdit.setFont(QFont("Arial", 12))

        # Add a label for the output
        self.outputLabel = QLabel()
        self.outputLabel.setWordWrap(True)
        self.outputLabel.setFont(QFont("Arial", 12))

        # Add a button to run the simulator
        self.button = QPushButton("Simulate")
        self.button.clicked.connect(self.simulate)

        # Add a button to step through the simulation
        self.stepButton = QPushButton("Step")
        self.stepButton.setEnabled(False)
        self.stepButton.clicked.connect(self.step)

        # Create a list to store the instructions
        self.instructions = []

        # Create a dictionary to store the register contents
        self.register_contents = {
            "$zero": 0,
            "$v0": 0,
            "$a0": 0,
            "$a1": 0,
        }

        # Initialize the program counter
        self.pc = 0

        # Add the input box and register content to a horizontal layout
        inputLayout = QVBoxLayout()
        inputLayout.addWidget(self.inputLabel)
        inputLayout.addWidget(self.textEdit)

        registerLayout = QVBoxLayout()
        registerLayout.addWidget(QLabel("Register Contents:"))
        for register, content in self.register_contents.items():
            registerLabel = QLabel(f"{register}: {content}")
            registerLabel.setObjectName(register)
            registerLayout.addWidget(registerLabel)

        layout = QHBoxLayout()
        layout.addLayout(inputLayout)
        layout.addLayout(registerLayout)

        # Add the buttons and layout to the main vertical layout
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layout)
        mainLayout.addWidget(self.button)
        mainLayout.addWidget(self.outputLabel)
        mainLayout.addWidget(self.stepButton)

        self.setLayout(mainLayout)

    def parse_instructions(self):
        # Parse the instructions from the input text
        input_text = self.textEdit.toPlainText()
        self.instructions = input_text.strip().split("\n")
        self.pc = 0

    def simulate(self):
        # Parse the instructions from the input text
        self.parse_instructions()

        # Enable the step button
        self.stepButton.setEnabled(True)

        # Disable the simulate button
        self.button.setEnabled(False)

        # Set the output label text to the contents of the registers
        self.update_output_label()

    def step(self):
        # Simulate the next instruction
        self.simulate_instruction(self.instructions[self.pc])

        # Increment the program counter
        self.pc += 1

        # Check if the simulation is complete
        if self.pc >= len(self.instructions):
            # Disable the step button
            self.stepButton.setEnabled(False)

            # Enable the simulate button
            self.button.setEnabled(True)

        # Update the output label text to the contents of the registers
        self.update_output_label()

    def simulate_instruction(self, instruction):
        # Here you would write the code to simulate the instruction and
        # update the contents of the registers
        # For the purpose of
        # Set the contents of $v0 to 42
        self.register_contents["$v0"] = 42

    def update_output_label(self):
        # Update the text of the register content labels
        for register, content in self.register_contents.items():
            registerLabel = self.findChild(QLabel, register)
            registerLabel.setText(f"{register}: {content}")

        # Update the text of the output label
        output_text = ""
        for register, content in self.register_contents.items():
            output_text += f"{register}: {content}\n"
        self.outputLabel.setText(output_text.strip())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MIPSWindow()
    window.show()
    sys.exit(app.exec())