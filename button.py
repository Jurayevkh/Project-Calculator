from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from functions import func

class Button:
    def __init__(self,screen,label):
        self.screen=screen
        self.label=label
        self.obj=func(self.label)
        self.button()

    def button(self):
        clear=QPushButton("AC",self.screen)
        clear.setGeometry(5,65,87,50)
        clear.setFont(QFont("Calibri",20))
        clear.setStyleSheet("background-color:#D4D4D2; color:black; border:2px solid #D4D4D2")
        clear.clicked.connect(self.obj.func_clear)

        beminus=QPushButton("%",self.screen)
        beminus.setGeometry(95,65,87,50)
        beminus.setFont(QFont("Calibri",20))
        beminus.setStyleSheet("background-color:#D4D4D2; color:black; border:2px solid #D4D4D2")
        beminus.clicked.connect(self.obj.func_foiz)

        bir=QPushButton("1",self.screen)
        bir.setGeometry(5,120,57,50)
        bir.setFont(QFont("Calibri",20))
        bir.setStyleSheet("background-color:#D4D4D2; color:black; border:2px solid #D4D4D2")
        bir.clicked.connect(self.obj.func_bir)

        ikki=QPushButton("2",self.screen)
        ikki.setGeometry(65,120,57,50)
        ikki.setFont(QFont("Calibri",20))
        ikki.setStyleSheet("background-color:#D4D4D2; color:black; border:2px solid #D4D4D2")
        ikki.clicked.connect(self.obj.func_ikki)

        uch=QPushButton("3",self.screen)
        uch.setGeometry(125,120,57,50)
        uch.setFont(QFont("Calibri",20))
        uch.setStyleSheet("background-color:#D4D4D2; color:black; border:2px solid #D4D4D2")
        uch.clicked.connect(self.obj.func_uch)

        tort=QPushButton("4",self.screen)
        tort.setGeometry(5,175,57,50)
        tort.setFont(QFont("Calibri",20))
        tort.setStyleSheet("background-color:#D4D4D2; color:black; border:2px solid #D4D4D2")
        tort.clicked.connect(self.obj.func_tort)

        besh=QPushButton("5",self.screen)
        besh.setGeometry(65,175,57,50)
        besh.setFont(QFont("Calibri",20))
        besh.setStyleSheet("background-color:#D4D4D2; color:black; border:2px solid #D4D4D2")
        besh.clicked.connect(self.obj.func_besh)

        olti=QPushButton("6",self.screen)
        olti.setGeometry(125,175,57,50)
        olti.setFont(QFont("Calibri",20))
        olti.setStyleSheet("background-color:#D4D4D2; color:black; border:2px solid #D4D4D2")
        olti.clicked.connect(self.obj.func_olti)

        yetti=QPushButton("7",self.screen)
        yetti.setGeometry(5,230,57,50)
        yetti.setFont(QFont("Calibri",20))
        yetti.setStyleSheet("background-color:#D4D4D2; color:black; border:2px solid #D4D4D2")
        yetti.clicked.connect(self.obj.func_yetti)

        sakkiz=QPushButton("8",self.screen)
        sakkiz.setGeometry(65,230,57,50)
        sakkiz.setFont(QFont("Calibri",20))
        sakkiz.setStyleSheet("background-color:#D4D4D2; color:black; border:2px solid #D4D4D2")
        sakkiz.clicked.connect(self.obj.func_sakkiz)

        toqqiz=QPushButton("9",self.screen)
        toqqiz.setGeometry(125,230,57,50)
        toqqiz.setFont(QFont("Calibri",20))
        toqqiz.setStyleSheet("background-color:#D4D4D2; color:black; border:2px solid #D4D4D2")
        toqqiz.clicked.connect(self.obj.func_toqqiz)

        nol=QPushButton("0",self.screen)
        nol.setGeometry(5,285,117,50)
        nol.setFont(QFont("Calibri",20))
        nol.setStyleSheet("background-color:#D4D4D2; color:black; border:2px solid #D4D4D2")
        nol.clicked.connect(self.obj.func_nol)

        nuqta=QPushButton(".",self.screen)
        nuqta.setGeometry(125,285,57,50)
        nuqta.setFont(QFont("Calibri",20))
        nuqta.setStyleSheet("background-color:#D4D4D2; color:black; border:2px solid #D4D4D2 ")
        nuqta.clicked.connect(self.obj.func_nuqta)

        plus=QPushButton("+",self.screen)
        plus.setGeometry(185,230,57,50)
        plus.setFont(QFont("Calibri",20))
        plus.setStyleSheet("background-color:#FF9500; color:white; border:2px solid #FF9500")
        plus.clicked.connect(self.obj.func_plus)

        minus=QPushButton("-",self.screen)
        minus.setGeometry(185,175,57,50)
        minus.setFont(QFont("Calibri",20))
        minus.setStyleSheet("background-color:#FF9500; color:white; border:2px solid #FF9500")
        minus.clicked.connect(self.obj.func_minus)

        kopaytiruv=QPushButton("×",self.screen)
        kopaytiruv.setGeometry(185,120,57,50)
        kopaytiruv.setFont(QFont("Calibri",20))
        kopaytiruv.setStyleSheet("background-color:#FF9500; color:white; border:2px solid #FF9500")
        kopaytiruv.clicked.connect(self.obj.func_kopaytiruv)

        boluv=QPushButton('÷',self.screen)
        boluv.setGeometry(185,65,57,50)
        boluv.setFont(QFont("Calibri",20))
        boluv.setStyleSheet("background-color:#FF9500; color:white; border:2px solid #FF9500")
        boluv.clicked.connect(self.obj.func_boluv)

        equal=QPushButton('=',self.screen)
        equal.setGeometry(185,285,57,50)
        equal.setFont(QFont("Calibri",20))
        equal.setStyleSheet("background-color:#FF9500; color:white; border:2px solid #FF9500")
        equal.clicked.connect(self.obj.func_equal)
