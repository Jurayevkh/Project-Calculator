from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtGui import QFont
from button import Button


if __name__ =="__main__":
    app=QApplication([])
    screen=QWidget()

    screen.setWindowTitle("Calculator")

    procces_screen=QLabel(screen)
    procces_screen.setGeometry(5,10,235,50)
    procces_screen.setFont(QFont("Calibri",20))
    procces_screen.setStyleSheet("color:white;")


    buttons=Button(screen,procces_screen)

    screen.setStyleSheet("background-color:#505050;")
    screen.setFixedSize(247,347)
    screen.show()
    app.exec_()
