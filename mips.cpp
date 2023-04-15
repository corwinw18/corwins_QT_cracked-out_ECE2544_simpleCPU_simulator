#include <QApplication>
#include <QWidget>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QFont>

class MIPSWindow : public QWidget
{
public:
    MIPSWindow(QWidget *parent = nullptr) : QWidget(parent)
    {
        // Add a label for the input
        QLabel *inputLabel = new QLabel("Enter MIPS Instructions:", this);
        inputLabel->move(10, 10);
        inputLabel->setFont(QFont("Arial", 12));

        // Add a line edit for the input
        m_lineEdit = new QLineEdit(this);
        m_lineEdit->move(10, 35);
        m_lineEdit->setFont(QFont("Arial", 12));
        m_lineEdit->resize(280, 20);

        // Add a button to run the simulator
        m_button = new QPushButton("Simulate", this);
        m_button->move(10, 60);

        // Connect the button to the simulate function
        connect(m_button, &QPushButton::clicked, this, &MIPSWindow::simulate);

        // Add a label for the output
        m_outputLabel = new QLabel(this);
        m_outputLabel->move(10, 90);
        m_outputLabel->setFixedWidth(280);
        m_outputLabel->setWordWrap(true);

        // Set the main window properties
        setGeometry(100, 100, 300, 150);
        setWindowTitle("MIPS Simulator");
        show();
    }

private slots:
    void simulate()
    {
        // Get the input text from the line edit
        QString input_text = m_lineEdit->text();

        // Simulate the MIPS instructions
        // Here you would write the code to simulate the instructions and
        // get the contents of each register
        // For the purpose of this example, we will just assume that the
        // contents of the registers are stored in a QMap<QString, int> called
        // register_contents
        QMap<QString, int> register_contents;
        register_contents["$zero"] = 0;
        register_contents["$v0"] = 10;
        register_contents["$a0"] = 5;
        register_contents["$a1"] = 7;

        // Set the output label text to the contents of the registers
        QString output_text = "Register Contents:\n";
        for (auto it = register_contents.constBegin(); it != register_contents.constEnd(); ++it)
        {
            output_text += it.key() + ": " + QString::number(it.value()) + "\n";
        }
        m_outputLabel->setText(output_text);
    }

private:
    QLineEdit *m_lineEdit;
    QPushButton *m_button;
    QLabel *m_outputLabel;
};

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    MIPSWindow window;
    return app.exec();
}